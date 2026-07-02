"""제공된 Transformer 실습 코드 구조를 바탕으로 만든 한국어 감성 분류 모델입니다."""

# math는 scaled dot-product attention에서 sqrt 계산을 위해 사용합니다.
import math

# torch는 텐서 연산을 수행하기 위해 사용합니다.
import torch

# nn은 PyTorch 신경망 계층을 정의하기 위해 사용합니다.
from torch import nn


# SelfAttention 클래스는 Multi-Head Self-Attention을 직접 구현합니다.
class SelfAttention(nn.Module):
    # __init__ 메서드는 Query, Key, Value, Output 선형 계층을 초기화합니다.
    def __init__(self, d_model: int, n_heads: int):
        # nn.Module의 초기화 기능을 실행합니다.
        super().__init__()
        # 임베딩 차원이 head 개수로 나누어떨어지지 않으면 head별 차원을 만들 수 없습니다.
        assert d_model % n_heads == 0, "d_model은 n_heads로 나누어떨어져야 합니다."
        # 전체 임베딩 차원을 저장합니다.
        self.d_model = d_model
        # attention head 개수를 저장합니다.
        self.n_heads = n_heads
        # head 하나가 담당할 벡터 차원을 계산합니다.
        self.head_dim = d_model // n_heads
        # 입력 벡터를 Query 벡터로 변환하는 선형 계층입니다.
        self.WQ = nn.Linear(d_model, d_model, bias=False)
        # 입력 벡터를 Key 벡터로 변환하는 선형 계층입니다.
        self.WK = nn.Linear(d_model, d_model, bias=False)
        # 입력 벡터를 Value 벡터로 변환하는 선형 계층입니다.
        self.WV = nn.Linear(d_model, d_model, bias=False)
        # 여러 head의 출력을 다시 d_model 차원으로 합치는 선형 계층입니다.
        self.WO = nn.Linear(d_model, d_model, bias=False)

    # forward 메서드는 입력 토큰 시퀀스에 self-attention을 적용합니다.
    def forward(self, x: torch.Tensor, pad_mask: torch.Tensor | None = None) -> torch.Tensor:
        # 입력 텐서에서 배치 크기와 문장 길이를 가져옵니다.
        batch_size, seq_len, _ = x.shape
        # 입력 x에서 Query를 계산하고 head 단위로 모양을 바꿉니다.
        q = self.WQ(x).view(batch_size, seq_len, self.n_heads, self.head_dim).transpose(1, 2)
        # 입력 x에서 Key를 계산하고 head 단위로 모양을 바꿉니다.
        k = self.WK(x).view(batch_size, seq_len, self.n_heads, self.head_dim).transpose(1, 2)
        # 입력 x에서 Value를 계산하고 head 단위로 모양을 바꿉니다.
        v = self.WV(x).view(batch_size, seq_len, self.n_heads, self.head_dim).transpose(1, 2)
        # Query와 Key의 내적으로 토큰 간 관련도 점수를 계산합니다.
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        # pad_mask가 있으면 padding 위치가 attention에 참여하지 못하게 매우 작은 값으로 바꿉니다.
        if pad_mask is not None:
            # pad_mask를 attention score와 broadcasting 가능한 형태로 변환합니다.
            mask = pad_mask[:, None, None, :]
            # padding 위치의 score를 매우 작은 값으로 채워 softmax 결과가 거의 0이 되게 합니다.
            scores = scores.masked_fill(mask, -1e9)
        # score에 softmax를 적용하여 attention 가중치를 계산합니다.
        attn = torch.softmax(scores, dim=-1)
        # attention 가중치를 Value에 곱해 문맥이 반영된 표현을 계산합니다.
        context = torch.matmul(attn, v)
        # head 차원을 다시 하나의 d_model 차원으로 합칩니다.
        context = context.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)
        # 최종 선형 계층을 통과시켜 attention 출력을 반환합니다.
        return self.WO(context)


# TransformerBlock 클래스는 Self-Attention, Residual, LayerNorm, FFN으로 구성된 인코더 블록입니다.
class TransformerBlock(nn.Module):
    # __init__ 메서드는 블록 내부 계층을 초기화합니다.
    def __init__(self, d_model: int, n_heads: int, ff_dim: int, dropout: float):
        # nn.Module의 초기화 기능을 실행합니다.
        super().__init__()
        # Multi-Head Self-Attention 계층을 생성합니다.
        self.attention = SelfAttention(d_model, n_heads)
        # Attention 이후 정규화를 위한 LayerNorm 계층을 생성합니다.
        self.norm1 = nn.LayerNorm(d_model)
        # FFN 이후 정규화를 위한 LayerNorm 계층을 생성합니다.
        self.norm2 = nn.LayerNorm(d_model)
        # 과적합 완화와 안정적인 학습을 위한 Dropout 계층을 생성합니다.
        self.dropout = nn.Dropout(dropout)
        # 각 토큰 위치에 독립적으로 적용되는 Feed Forward Network를 생성합니다.
        self.ff = nn.Sequential(
            # d_model 차원을 ff_dim 차원으로 확장합니다.
            nn.Linear(d_model, ff_dim),
            # 비선형성을 추가하기 위해 ReLU 활성화 함수를 적용합니다.
            nn.ReLU(),
            # 중간 표현에 Dropout을 적용합니다.
            nn.Dropout(dropout),
            # ff_dim 차원을 다시 d_model 차원으로 축소합니다.
            nn.Linear(ff_dim, d_model),
        )

    # forward 메서드는 Transformer Block의 순전파를 수행합니다.
    def forward(self, x: torch.Tensor, pad_mask: torch.Tensor | None = None) -> torch.Tensor:
        # Self-Attention 결과를 계산합니다.
        attn_out = self.attention(x, pad_mask)
        # Residual Connection과 Dropout을 적용한 뒤 LayerNorm으로 안정화합니다.
        x = self.norm1(x + self.dropout(attn_out))
        # Feed Forward Network 결과를 계산합니다.
        ff_out = self.ff(x)
        # Residual Connection과 Dropout을 적용한 뒤 LayerNorm으로 안정화합니다.
        x = self.norm2(x + self.dropout(ff_out))
        # 블록 출력 텐서를 반환합니다.
        return x


# NaverTransformerSentiment 클래스는 한국어 리뷰 감성 분류를 위한 전체 모델입니다.
class NaverTransformerSentiment(nn.Module):
    # __init__ 메서드는 임베딩, 위치 임베딩, Transformer 블록, 분류층을 초기화합니다.
    def __init__(self, vocab_size: int, max_len: int, d_model: int, n_heads: int, n_layers: int, ff_dim: int, dropout: float, num_classes: int = 2):
        # nn.Module의 초기화 기능을 실행합니다.
        super().__init__()
        # padding 토큰 ID를 저장합니다.
        self.pad_id = 0
        # 최대 문장 길이를 저장합니다.
        self.max_len = max_len
        # 단어 ID를 의미 벡터로 바꾸는 Embedding 계층을 생성합니다.
        self.token_emb = nn.Embedding(vocab_size, d_model, padding_idx=self.pad_id)
        # 위치 ID를 위치 벡터로 바꾸는 Embedding 계층을 생성합니다.
        self.pos_emb = nn.Embedding(max_len, d_model)
        # 임베딩 결과에 적용할 Dropout 계층을 생성합니다.
        self.dropout = nn.Dropout(dropout)
        # TransformerBlock을 n_layers개 쌓아 ModuleList로 저장합니다.
        self.blocks = nn.ModuleList([TransformerBlock(d_model, n_heads, ff_dim, dropout) for _ in range(n_layers)])
        # 문장 벡터를 긍정/부정 로짓으로 바꾸는 분류층을 생성합니다.
        self.classifier = nn.Linear(d_model, num_classes)

    # forward 메서드는 토큰 ID 시퀀스를 받아 감성 클래스 점수를 반환합니다.
    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        # 입력 텐서가 위치한 장치를 확인합니다.
        device = input_ids.device
        # 입력 텐서에서 배치 크기와 문장 길이를 가져옵니다.
        batch_size, seq_len = input_ids.shape
        # padding 토큰 위치를 True로 표시하는 마스크를 만듭니다.
        pad_mask = input_ids.eq(self.pad_id)
        # 0부터 seq_len-1까지의 위치 ID를 생성합니다.
        positions = torch.arange(seq_len, device=device).unsqueeze(0).expand(batch_size, seq_len)
        # 단어 임베딩과 위치 임베딩을 더해 순서 정보가 포함된 입력 표현을 만듭니다.
        x = self.token_emb(input_ids) + self.pos_emb(positions)
        # 임베딩 표현에 Dropout을 적용합니다.
        x = self.dropout(x)
        # Transformer Block을 순서대로 통과시킵니다.
        for block in self.blocks:
            # 현재 블록에 입력 표현과 padding mask를 전달합니다.
            x = block(x, pad_mask)
        # padding이 아닌 실제 토큰 위치를 1.0으로 표시하는 마스크를 만듭니다.
        non_pad = (~pad_mask).float().unsqueeze(-1)
        # 실제 토큰 표현만 남기고 padding 위치는 0으로 만듭니다.
        masked_x = x * non_pad
        # 실제 토큰 개수를 계산하되 0으로 나누는 문제를 방지하기 위해 최소값을 1로 제한합니다.
        lengths = non_pad.sum(dim=1).clamp(min=1.0)
        # 실제 토큰들의 평균을 내어 문장 전체를 대표하는 벡터를 만듭니다.
        pooled = masked_x.sum(dim=1) / lengths
        # 문장 벡터를 분류층에 넣어 클래스별 로짓을 계산합니다.
        logits = self.classifier(pooled)
        # 클래스별 로짓을 반환합니다.
        return logits
