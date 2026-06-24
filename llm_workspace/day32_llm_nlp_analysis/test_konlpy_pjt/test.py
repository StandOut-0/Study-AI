# KAIST 말뭉치를 이용해 생성된 사전 분석기

from konlpy.tag import Hannanum
han = Hannanum()

text = u"길동 마트의 흑마늘 양념 치킨이 논란이 되고있다. "
print("KAIST","------"*5)
print(han.analyze(text))
print(han.morphs(text))
print(han.nouns(text))
print(han.pos(text))

from konlpy.tag import Kkma
kkma = Kkma()
print("Kkma","------"*5)
print(kkma.sentences(text))
print(kkma.morphs(text))
print(kkma.nouns(text))
print(kkma.pos(text))

from konlpy.tag import Komoran
kom = Komoran()
print("문장 분리:", kom.morphs(text))
print("형태소 분석:", kom.morphs(text))
print("명사 추출:", kom.nouns(text))
print("품사 태깅:", kom.pos(text))

from konlpy.tag import Okt

okt = Okt()
print("Okt", "------"*5)
print("형태소 분석:", okt.morphs(text))
print("명사 추출:", okt.nouns(text))
print("품사 태깅:", okt.pos(text))