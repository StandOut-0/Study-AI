# import bs4
# import urllib.request
import urllib.request, bs4

test_value = ["urllib_homepage_download", "naver_search_movie",
              "urllib_parse" ,"urllib_urlretrieve", "urllib_decode", "request_or_bs4", "use_bs4"]
test = test_value[0]
web_page = urllib.request.urlopen("https://www.naver.com")
web_page_movie = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EA%B0%9C%EB%B4%89%EC%98%81%ED%99%94&oquery=%EA%B0%9C%EB%B4%89%EC%98%81%ED%98%B8%E3%85%93&tqi=jlSa3wqX5Ewssgw9lUV-251724&ackey=p51q9m1d')

if test == "request_or_bs4":

    print(web_page)
    # print(web_page.read(100))
    print(web_page.readlines(5000)[0])
    print(len(web_page.readlines(5000)))

    
    decoding_code = bs4.BeautifulSoup(web_page, "html.parser")
    # print(decoding_code)
elif test == "use_bs4":

    url = input("주소를 입력하세요: ")
    web_page = urllib.request.urlopen(url)
    result_code = bs4.BeautifulSoup(web_page, "html.parser")

    print(web_page)
    print(result_code)
elif test == "urllib_decode":
    byte_data = web_page.read(900)
    text_data = byte_data.decode()
    print(byte_data)
    print("---------------------------")
    print(text_data)
elif test == "urllib_urlretrieve":
    img_url = "https://mimgnews.pstatic.net/image/upload/office_logo/448/2025/03/07/logo_448_100_20250307145622.png?type=nf36_36"
    new_name = "test.png"
    urllib.request.urlretrieve(img_url, new_name)
elif test == "urllib_parse": # 오늘운세
    parse = urllib.parse.urlparse(web_page_movie.url)
    print("parse------------------------------------")
    for item in parse:
        print(item)
    print("parse_qs------------------------------------")
    parse_qs = urllib.parse.parse_qs(web_page_movie.url)
    print(parse_qs)
    print("parse_qsl------------------------------------")
    parse_qsl = urllib.parse.parse_qsl(web_page_movie.url)
    print(parse_qsl)

    print("urlunparse------------------------------------")
    urlunparse = urllib.parse.urlunparse(parse)
    print(urlunparse)

    urlsplit = urllib.parse.urlsplit(web_page_movie.url)
    print("urlsplit------------------------------------")
    for item in urlsplit:
        print(item)
    print("urlunsplit------------------------------------")
    urlunsplit = urllib.parse.urlunsplit(urlsplit)
    print(urlunsplit)

    

    print("urljoin------------------------------------")
    urljoin1 = urllib.parse.urljoin(web_page.url, web_page.url)
    print(urljoin1)
    urljoin2 = urllib.parse.urljoin(web_page.url, '/hi')
    print(urljoin2)
    urljoin3 = urllib.parse.urljoin(web_page.url, 'https://drive.google.com/')
    print(urljoin3)

    print("quote------------------------------------")
    quote = urllib.parse.quote(web_page.url)
    print(web_page.url)
    print(quote)
    print("unquote------------------------------------")
    unquote = urllib.parse.unquote(quote)
    print(quote)
    print(unquote)
elif test == "urllib_homepage_download":

    # header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'}
    # request = urllib.request.Request(web_page.url, headers=header)
    # data = urllib.request.urlopen(request).read()
    # f = open("test.html", "wb")
    # f.write(data)
    # f.close()

    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get(web_page.url)
    data = driver.page_source
    with open("test2.html", "w", encoding="utf-8") as f:
        f.write(data)




    header = {'User-Agent': 'Mozilla/5.0 (iPhone)'}
    request = urllib.request.Request(web_page.url, headers=header)
    data = urllib.request.urlopen(request).read()
    f = open("test_m.html", "wb")
    f.write(data)
    f.close()

    

