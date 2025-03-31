#0_패키지 로드
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import urllib.request as req
import time
import datetime

#1_날짜 설정
now = datetime.datetime.now()
nowDate = now.strftime('%Y-%m-%d')

#2-1_URL 접근
url = input("URL : ")
driver = webdriver.Chrome('/Users/blaix/Desktop/Coding/chromedriver')
driver.maximize_window()
driver.get(url)

#2-2_스크롤 다운
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#2-3_이미지 취합 및 타이틀 획득
html = driver.page_source
soup = bs(html, 'html.parser')
images = soup.find_all(class_= '_7jys img')
title = soup.find(class_= 'qku1pbnj d0wue5ts cu1gti5y pw7auppr te7ihjl9 svz86pwt a53abz89 dnk81rqm gp6ucdfj').string

#2-4_이미지 저장
i = 1
for image in images :
    imageUrl = image['src']
    req.urlretrieve(imageUrl, './Image/' + title +"_" + str(i) + "_" + str(nowDate) + '.jpg')
    i += 1

#3_종료
driver.quit()
print("Complte")
