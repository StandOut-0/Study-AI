import torch
import torch.nn as nn
from tenacity import retry_if_not_exception_type

from src.config import PAD_TOKEN, SOS_TOKEN, EOS_TOKEN

# class Encoder(nn.Module):
#     def __init__(self, vocab_size, embed_size, hidden_size):
#         super().__init__()
#         self.embedding = nn.Embedding(vocab_size, embed_size, padding_idx=0)
#         self.gru = nn.GRU(embed_size, hidden_size, batch_first=True)
#
#     def forward(self, source_idx):
#         embedded = self.embedding(source_idx)
#         outputs, hidden = self.gru(embedded)
#         return hidden
#
# class Decoder(nn.Module):
#     def __init__(self, vocab_size, embed_size, hidden_size):
#         super().__init__()
#         self.embedding = nn.Embedding(vocab_size, embed_size, padding_idx=0)
#         self.gru = nn.GRU(embed_size, hidden_size, batch_first=True)
#         self.fc = nn.Linear(hidden_size, vocab_size)
#
#     def forward(self, decoder_input, hidden):
#             embedded = self.embedding(decoder_input)
#             outputs, hidden = self.gru(embedded, hidden)
#             logits = self.fc(outputs)
#             return logits, hidden
#
# class Seq2SeqTranslator(nn.Module):
#     def __init__(self, vocab_size, embed_size, hidden_size):
#         super().__init__()
#         self.encoder = Encoder(vocab_size, embed_size, hidden_size)
#         self.decoder = Decoder(vocab_size, embed_size, hidden_size)
#
#     def forward(self, source_idx, decoder_input_idx):
#         hidden = self.encoder(source_idx)
#         logits, hidden = self.decoder(decoder_input_idx, hidden)
#         return logits


import math

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()

        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len).unsqueeze(1)

        div_term = torch.exp(
            torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model)
        )

        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        self.pe = pe.unsqueeze(0)

    def forward(self, x):
        return x + self.pe[:, :x.size(1)].to(x.device)


class Seq2SeqTranslator(nn.Module):
    def __init__(self, vocab_size, d_model, n_heads, num_layers, dropout=0.1):
        super().__init__()

        self.embedding = nn.Embedding(vocab_size, d_model, padding_idx=0)
        self.pos_encoding = PositionalEncoding(d_model)

        self.transformer = nn.Transformer(
            d_model=d_model,
            nhead=n_heads,
            num_encoder_layers=num_layers,
            num_decoder_layers=num_layers,
            dropout=dropout,
            batch_first=True
        )

        self.fc_out = nn.Linear(d_model, vocab_size)

    def forward(self, src, tgt, tgt_mask=None):
        # embedding
        src = self.embedding(src)
        tgt = self.embedding(tgt)

        # positional encoding
        src = self.pos_encoding(src)
        tgt = self.pos_encoding(tgt)

        # transformer
        output = self.transformer(
            src,
            tgt,
            tgt_mask=tgt_mask
        )

        logits = self.fc_out(output)
        return logits