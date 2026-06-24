import codecs
import csv
from konlpy.tag import Okt
from test_Okt_norm_stem import mal_list

okt = Okt()
word_dic = {}
lines = []

with open('./data/sample2.csv', "r", encoding="cp949") as raws:
    render = csv.reader(raws)
    for row in render:
        lines.append(row)
        # print(row)

for line in lines:
    # print(''.join(line))
    mal_list = okt.pos(' '.join(line))
    # print(mal_list)

for word in mal_list:
    # print(word)
    pass

for word in mal_list:
    if word[1] == 'Noun':
        if not word[0] in word_dic:
            word_dic[word[0]] = 0
        word_dic[word[0]] += 1
# print(word_dic)

# 단어빈도수에 대새 내림차순 정리
keys = sorted(word_dic.items(), key=lambda x : x[1], reverse=True)
for word, count in keys:
    # print(word, count, end=", ")
    pass



from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud(
    font_path="C:/Windows/Fonts/malgun.ttf",
        width=1000,
        height=800,
        background_color="#FFF5F7",
        # colormap="hot"
        # colormap="hot"       # 검정→빨강→주황→노랑
        # colormap="inferno"   # 검정→보라→주황
        # colormap="plasma"    # 보라→핑크→노랑
        # colormap="viridis"   # 파랑→초록→노랑
        # colormap="magma"     # 검정→보라→주황
        # colormap="turbo"     # 무지개 느낌
        # colormap="Pastel1"
        # colormap="Pastel2"
        colormap="Set3"
        # colormap="Accent"
    )
# wordcloud.generate(word_dic[word_dic])
wordcloud.generate_from_frequencies(word_dic)

# plt.figure(figsize=(10,10))
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()

import os
print(os.path.exists("C:/Windows/Fonts/malgun.ttf"))


from PIL import Image
import numpy as np
import random

pink_colors = [
    "#FF69B4",  # 핫핑크
    "#FF85A2",
    "#FFB6C1",  # 라이트핑크
    "#FFC0CB",  # 핑크
    "#FF9EB5",
    "#F8C8DC",  # 파스텔핑크
    "#E6A8D7"   # 연보라핑크
]
def pink_color_func(*args, **kwargs):
    return random.choice(pink_colors)

img= Image.open('./images/heart.png')
imgArray = np.array(img)

wordcloud = WordCloud(
    font_path = r"C:/Windows/Fonts/malgun.ttf",
        width=1000,
        height=800,
        background_color="#FFF5F7",
        colormap = "Set3",
    max_font_size= 100,
    mask = imgArray
)
wordcloud.generate_from_frequencies(word_dic)
wordcloud.recolor(color_func=pink_color_func)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()