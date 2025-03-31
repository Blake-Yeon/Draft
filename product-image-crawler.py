#0 라이브러리 투입

from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import urllib.request as req
import pandas as pd
import numpy as np
import os

Location = '/Users/blaix/Desktop/Coding'
File = 'Product_URL.xlsx'

#1 상품 URL을 리스트화

data_pd = pd.read_excel('{}/{}'.format(Location, File), header=0, index_col=None, names=None, engine='openpyxl')
data_np = pd.DataFrame.to_numpy(data_pd)

url_product = data_np[:,0].tolist()
product_uid = data_np[:,1].tolist()

#5 반복문 처리

number = 0

for url in url_product :
    
#2 해당 리스트 홈페이지 접속 및 이미지 URL 저장

    driver = webdriver.Chrome('/Users/blaix/Desktop/Coding/chromedriver')
    driver.get(url)

    html = driver.page_source
    soup = bs(html, 'html.parser')


    title = str(product_uid[number]) + "_" + soup.find('title').string.strip('[]')
    images = soup.select('.detailimg > img')

#3 경로 설정 및 폴더 생성

    path = "/Users/blaix/Desktop/Coding/chromedriver/Image"
    os.chdir(path)

    folder = os.path.join(title)

    try:
        if not (os.path.isdir(folder)):
            os.makedirs(folder)
    except OSError:
        print('Error: Creating directory ' + title)

    os.chdir(folder)

#4 개별 이미지 다운로드

    i = 1
    for image in images :
        imageUrl = image['src']
        try:
            req.urlretrieve(imageUrl, title +"_" + str(i) + "_" + '.jpg')
        except:
            continue
        i += 1
    
    print(title + " 완료")

    driver.quit()

    number += 1

#5 종료

print("최종 완료")
