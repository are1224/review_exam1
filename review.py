import requests
from bs4 import BeautifulSoup
import csv

# def get_news_soup_objects():
soup_objects = []

URL = 'https://movie.naver.com/movie/running/current.nhn'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

review_section = soup.select(
'div[id=container] > div[id=content] > div[class=article] > div[class=obj_section] > div[class=lst_wrap] > ul[class=lst_detail_t1] > li'
)

for review in review_section:
        
        a_tag = review.select_one('dl > dt > a')

        review_title = a_tag.get_text()
        review_link = a_tag['href']

        data = {
            'title' : review_title,
            'link' : review_link
        }
        print(data)

        # with open('review.csv', 'a', encoding='utf-8-sig', newline="") as csvfile:
        #     fieldname = ['title', 'link']
        #     csvwriter = csv.DictWriter(csvfile, fieldname)
        #     csvwriter.writerow(data)