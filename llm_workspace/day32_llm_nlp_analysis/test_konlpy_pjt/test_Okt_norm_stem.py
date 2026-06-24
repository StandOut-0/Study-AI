from konlpy.tag import Okt
from konlpy.utils import read_txt


okt = Okt()
text = read_txt('./data/sample.txt', encoding='utf-8')
# print('norm= True, stem = True-------------')
mal_list = okt.pos(text, norm=True, stem=True)
# print(mal_list)

# print('norm= False, stem = False-------------')
mal_list = okt.pos(text, norm=False, stem=False)
# print(mal_list)