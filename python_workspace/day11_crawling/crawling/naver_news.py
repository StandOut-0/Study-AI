import requests

url = "https://news.naver.com/"
response = requests.get(url)
html_data = response.text
# print(html_data)

# print(html_data.find('<span class="cjs_main">')) # 33730
# print(html_data[33730:33730+50]) # <span class="cjs_main">언론사편집</span>

import re
body = re.search('<span class="cjs_main.*span>', html_data)
body = body.group()
# print(body)

title = re.sub('<.+?>', '', body)
print("title: ", title)


title_sub =  html_data.split('<em class="cnf_journal_name">')[1]
title_sub = title_sub.split('</em>')[0]
# print("title_sub: ", title_sub)

items =  html_data.split('<em class="cnf_journal_name">')
for item in items:
    if item.find('</em>') != -1:
        item = item.split('</em>')[0]
        print("title_sub: ", item, end=', ')


