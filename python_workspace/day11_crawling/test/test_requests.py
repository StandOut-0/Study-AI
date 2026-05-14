import requests
# url = "https://www.naver.com"
# response = requests.get(url)
# print(response.status_code)
# print(response.text)

url = "https://search.naver.com/search.naver"
params = {"query": "오늘운세"}
response = requests.get(url, params=params)
# print(response.text)

mod_card_bx = response.text.find("mod_card_bx")
# print(mod_card_bx)


from selenium import webdriver
import time

params = {"query": "오늘운세"}
full_url = requests.Request("GET", url, params=params).prepare().url

driver = webdriver.Chrome()
driver.get(full_url)
time.sleep(5)
elem = driver.find_element("class name", "mod_card_bx")
print(elem.text)