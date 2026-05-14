import urllib.request, bs4
web_page_movie = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EA%B0%9C%EB%B4%89%EC%98%81%ED%99%94&oquery=%EA%B0%9C%EB%B4%89%EC%98%81%ED%98%B8%E3%85%93&tqi=jlSa3wqX5Ewssgw9lUV-251724&ackey=p51q9m1d')

result_code = bs4.BeautifulSoup(web_page_movie, "html.parser")
    # print(result_code)

data_box = result_code.find("div", {"class": "data_box"})
# print(data_box)
# print(len(data_box))

movie_title = result_code.find("a", {"class": "this_text"})
# print(movie_title)
# print('-------------------------')

movie_titles = result_code.find_all("a", {"class": "this_text"})
for movie_title in movie_titles:
    # print(movie_title)
    # print(movie_title.text)
    # print(movie_title.attrs)
    pass

movie_div = result_code.find_all("div", {"class": "data_area"})
# print("movie_div: ", len(movie_div))
# print(movie_div)

button_div = result_code.find_all("div", {"class": "button_area"})
# print("button_div: ", len(button_div))

movie_list = list()
for idx in range(len(movie_div)):
    data_box = movie_div[idx].find("div", {"class": "data_box"})
    # print(data_box)
    preview_tag = button_div[idx].find("a", {"class": "btn_preview"})
    # print(preview_tag)
    movie_title = data_box.find("a", {"class": "this_text"}).text
    # print(movie_title)

    movie_link = preview_tag["href"] if preview_tag else None
    # print(movie_link)
    # movie_list.append(movie_link)

    movie_genre = None
    movie_open_date = None
    star_point = 0.0

    info_group = data_box.find_all('dl', class_='info_group')
    for dl_tag in info_group:
        dt_tags = dl_tag.find_all('dt')
        for dt in dt_tags:
            label = dt.text.strip()
            
            dd = dt.find_next_sibling('dd')
            if label == '개요':
                movie_genre = dd.text.strip()
            elif label == '개봉':
                movie_open_date = dd.text.strip()

            if dd.find('span', class_='num') != None:
                star_point = round(float(dd.find('span', class_='num').text.strip()), 2)
                # print(star_point)
                
    movie = dict()
    movie['title'] = movie_title
    movie['link'] = movie_link
    movie['genre'] = movie_genre
    movie['star_point'] = star_point
    movie['open_date'] = movie_open_date
    movie_list.append(movie)


# for i, x in enumerate(movie_list):
#     print(i, type(x), x)


# 항목을 하나씩 꺼내서 lambda x , x를 key로해서 내림차순 정렬
sort_list = sorted(movie_list, key=lambda x: x['star_point'], reverse=True)
# sort_list = sorted(movie_list, key=lambda x: float(x['star_point']), reverse=True)

# print(sort_list)

for idx in range(len(movie_list)):
    movie = movie_list[idx]
    movie['rank'] = idx + 1
    print(movie)
    print('/n')