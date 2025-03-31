# Library

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = input("PC URL : ")

driver = webdriver.Chrome('/Users/blaix/Desktop/Coding/chromedriver')
driver.implicitly_wait(1)
driver.get(url)
driver.implicitly_wait(1)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Get ID

id = soup.find(class_='crema-fit-product-combined-detail crema-applied')['data-product-code']

# Get Title

title_description = soup.select('.tit-prd')
real_title_description = title_description[0]
real_description = real_title_description.select(".subNameAdd")
for span in real_description:
    span.decompose()
title = title_description[0].text
title = title.strip('\n')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Get Review

url_review = driver.find_element_by_xpath('//*[@id="crema-product-reviews-1"]')
url_review_source = url_review.get_attribute('src')
driver.get(url_review_source)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

reviews = []

while True:
    try:
        reviewArray = soup.find_all("div", {"class" : "review_message review_message--collapsed review_message--collapsed3 js-translate-review-message"})
        for data in reviewArray:
            reviews.append(data.get_text())
        temp = reviewArray
        next_page_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[3]/div/div/a[last()]').click()
        time.sleep(1)
        driver.get(driver.current_url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
    except:
        print("리뷰수집끝남")
        break

print(len(reviews))

df = pd.DataFrame({'Review' : reviews})
df = df.replace('\n', ' ', regex=True)
df.to_csv(f'{id}_{title}_Reviews.csv', encoding='utf-8-sig')

driver.quit()
