import torch
import torch.nn as nn
from tenacity import retry_if_not_exception_type

from src.config import PAD_TOKEN, SOS_TOKEN, EOS_TOKEN

class Encoder(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size, padding_idx=0)
        self.gru = nn.GRU(embed_size, hidden_size, batch_first=True)

    def forward(self, source_idx):
        embedded = self.embedding(source_idx)
        outputs, hidden = self.gru(embedded)
        return hidden

class Decoder(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size, padding_idx=0)
        self.gru = nn.GRU(embed_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, decoder_input, hidden):
            embedded = self.embedding(decoder_input)
            outputs, hidden = self.gru(embedded, hidden)
            logits = self.fc(outputs)
            return logits, hidden

class Seq2SeqTranslator(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size):
        super().__init__()
        self.encoder = Encoder(vocab_size, embed_size, hidden_size)
        self.decoder = Decoder(vocab_size, embed_size, hidden_size)

    def forward(self, source_idx, decoder_input_idx):
        hidden = self.encoder(source_idx)
        logits, hidden = self.decoder(decoder_input_idx, hidden)
        return logits
