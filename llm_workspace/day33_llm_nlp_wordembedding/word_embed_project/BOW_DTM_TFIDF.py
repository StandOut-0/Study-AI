import sys
import subprocess
from math import log
try:
    from sklearn.feature_extraction.text import CountVectorizer
except ModuleNotFoundError:
    raise ModuleNotFoundError("Please install the sklearn package.")

try:
    from konlpy.tag import Okt
    okt = Okt()
    KONLPY_AVAILABLE = True
except Exception as e:
    okt = None
    KONLPY_AVAILABLE = False
    KONLPY_ERROR = e

try:
    import nltk
    from nltk.corpus import stopwords
    NLTK_AVAILABLE = True
except ModuleNotFoundError:
    nltk = None
    stopwords = None
    NLTK_AVAILABLE = False
    raise ModuleNotFoundError("Please install the nltk package.")

def print_section(title):
    print('\n' + '='*80)
    print(title)
    print('='*80)

print_section('1. BOW 구현: 한국어 문장을 빈도 벡털 변환')
if not KONLPY_AVAILABLE:
    print('[안내] konlpy.Okt 실행에 실패했습니다. 현재 코드는 공백기반 토큰화를 사용하여 계속 실행합니다. ')

# 한국어 문장을 토큰 리스트로 변환하는 함수
def tokenize_korean(document):
    cleaned_document = document.replace('.', '')
    cleaned_document = cleaned_document.replace(',', '')
    if KONLPY_AVAILABLE:
        return okt.morphs(cleaned_document)
    return cleaned_document.split()

# 하나의 문서에서 BOW 사전과 빈도벡터를 만드는 함수
def build_bag_of_words(document):
    tokenize_document = tokenize_korean(document)
    word_to_index = {}
    bow = []
    for word in tokenize_document:
        if word not in word_to_index:
            word_to_index[word] = len(word_to_index)
            bow.append(1)
        else:
            index = word_to_index[word]
            bow[index] += 1
    return word_to_index, bow

doc1 = "파이썬을 이용한 텍스트 빈도수 카운트 실습을 진행합니다 ."
vocab, bow = build_bag_of_words(doc1)
print("입력문장: ", doc1)
print("Vocab: ", vocab)
print('Vocab size: ', len(vocab))
print('BoW size: ', len(bow))
print("BOW: ", bow)


print_section("2. CountVectorizer를 이용한 BOW 생성")
corpus = ["you know i want your love. I love you"]
vec = CountVectorizer()
bow_matrix = vec.fit_transform(corpus)
print("입력코퍼스: ", corpus)
print("bag of words: ", bow_matrix.toarray())
print("Vocab: ", vec.vocabulary_)

print_section("3. 사용자가 직접 정의한 불용어 제거")
text = ["Family is not an important thing."]
custom_stop_words = ['the', 'a', 'an', 'is', 'not']
vect_custom = CountVectorizer(stop_words=custom_stop_words)
custom_matrix = vect_custom.fit_transform(text)
print("입력문장: ", text)
print("bow vector: ", custom_matrix)
print("Vocab: ", vect_custom.vocabulary_)


print_section("4. DTM과 TF-IDF을 위한 전처리 단계")
docs = [
    "배우고 싶은 자연어",
    "딥러닝 머신러닝 배우고 싶은 강화학습",
    "자연어 처리 좋아요",
    "배우고 싶은 딥러닝"
]
vocab = sorted(set(word for doc in docs for word in doc.split()))
N = len(vocab)
print("문서목록")
for idx, doc in enumerate(docs, start=1):
    print(f'문서{idx} : {doc}')
print("vocab: ", vocab)
print("문서개수 N: ", N)