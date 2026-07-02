import torch
import re
from src.config import MODEL_PATH, META_PATH, EMBED_SIZE, HIDDEN_SIZE, MAX_OUTPUT_LEN, SOS_TOKEN, EOS_TOKEN, DATA_PATH, UNK_TOKEN
from src.data_utils import normalize_text, encode_text
from src.model import Seq2SeqTranslator

def detect_language(text) -> str:
    if re.search(r'[가-힣]', text):
        return 'ko'
    return 'en'

def build_direction_source(text: str, source_lang: str) -> str:
    if source_lang == 'en':
        return '<EN2KO>' + normalize_text(text)
    return '<KO2EN>' + normalize_text(text)

def load_model():
    if not MODEL_PATH.exists() or not META_PATH.exists():
        raise FileNotFoundError("학습된 모델 파일이 없습니다. python -m src.train")
    meta = torch.load(META_PATH, map_location="cpu")
    char2idx = meta["char2idx"]
    idx2char = meta["idx2char"]
    model = Seq2SeqTranslator(len(char2idx), meta.get("embed_size", EMBED_SIZE), meta.get("hidden_size", HIDDEN_SIZE))
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    model.eval()
    return model, char2idx, idx2char

def load_exact_dictionary():
    import csv
    mapping = {}
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            en = normalize_text(row["en"])
            ko = normalize_text(row["ko"])
            mapping['en', en] = ko
            mapping['ko', ko] = en
    return mapping

def translate(text:str, model=None, char2idx=None, idx2char=None) -> str:
    if not text or not text.strip():
        return "번역할문장을 입력하세요"
    source_lang = detect_language(text)
    exact_dict = load_exact_dictionary()
    exact_key = (source_lang, normalize_text(text))
    if exact_key in exact_dict:
        return exact_dict[exact_key]

    if model is None or char2idx is None or idx2char is None:
        model, char2idx, idx2char = load_model()

    source_text = build_direction_source(text, source_lang)
    source_idx = encode_text(source_text, char2idx, add_eos=True)
    source_tensor = torch.tensor(source_idx, dtype=torch.long).unsqueeze(0)
    with torch.no_grad():
        hidden = model.encoder(source_tensor)
        decoder_input = torch.tensor([[char2idx[SOS_TOKEN]]], dtype=torch.long)
        result_chars = []

        for _ in range(MAX_OUTPUT_LEN):
            logits, hidden = model.decoder(decoder_input, hidden)
            next_id = int(torch.argmax(logits[:, -1, :], dim=1).item())
            next_char = idx2char.get(next_id, UNK_TOKEN)
            if next_char == EOS_TOKEN:
                break
            if next_char not in {"<PAD>", SOS_TOKEN, UNK_TOKEN}:
                result_chars.append(next_char)
            decoder_input = torch.tensor([[next_id]], dtype=torch.long)
        result = "".join(result_chars).strip()

        if not result:
            return "번역 결과를 생성하지 못했습니다. 학습 데이터를 늘리거나 epoch를 증가시켜주세요"

        return result
