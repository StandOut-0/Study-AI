import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
# from src.config import DATA_PATH, MODEL_PATH, META_PATH, EMBED_SIZE, HIDDEN_SIZE, EPOCHS, BATCH_SIZE, LEARNING_RATE
from src.config import DATA_PATH, MODEL_PATH, META_PATH, EMBED_SIZE, EPOCHS, BATCH_SIZE, LEARNING_RATE
from src.data_utils import load_translation_pairs, build_vocab, TranslationDataset, collate_batch
from src.model import Seq2SeqTranslator

def train_model(epochs = EPOCHS, batch_size = BATCH_SIZE):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    pairs = load_translation_pairs(DATA_PATH)
    char2idx, idx2char = build_vocab(pairs)
    vocab_size = len(char2idx)
    dataset = TranslationDataset(pairs, char2idx)
    loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True, collate_fn=collate_batch)

    # 모델생성 수정
    # model = Seq2SeqTranslator(vocab_size, EMBED_SIZE, HIDDEN_SIZE).to(device)
    model = Seq2SeqTranslator(
        vocab_size=vocab_size,
        d_model=EMBED_SIZE,
        n_heads=8,
        num_layers=3,
        dropout=0.1
    ).to(device)


    criterion = nn.CrossEntropyLoss(ignore_index=char2idx['<PAD>'])
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)
    epochs = EPOCHS

    for epoch in range(1, epochs +1):
        model.train()
        total_loss = 0.0
        for source_idx, decoder_input_idx, decoder_target_idx in loader:
            source_idx = source_idx.to(device)
            decoder_input_idx = decoder_input_idx.to(device)
            decoder_target_idx = decoder_target_idx.to(device)

            optimizer.zero_grad()


            # forward 호출 변경
            # logits = model(source_idx, decoder_input_idx)
            tgt_mask = nn.Transformer.generate_square_subsequent_mask(
                decoder_input_idx.size(1)
            ).to(device)

            logits = model(
                source_idx,
                decoder_input_idx,
                tgt_mask
            )



            loss = criterion(logits.reshape(-1, logits.size(-1)), decoder_target_idx.reshape(-1))
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            total_loss += loss.item()
        if epoch == 1 or epoch % 20 == 0:
            print(f"Epoch {epoch:03d} / {epochs} | Loss: {total_loss / len(loader):.4f}")

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), MODEL_PATH)

    # HIDDEN_SIZE히든 삭제
    torch.save({
        "char2idx": char2idx,
        "idx2char": idx2char,
        "embed_size": EMBED_SIZE
        # "hidden_size": HIDDEN_SIZE,
    }, META_PATH)

    print(f"모델저장완료{MODEL_PATH}")
    return model, char2idx, idx2char

if __name__ == "__main__":
    train_model(epochs = EPOCHS)

