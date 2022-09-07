import requests
from bs4 import BeautifulSoup as bs

urls =  ['https://www.geeksforgeeks.org/','https://google.com','https://evil.com']
for url in urls:
    print(f'🐽 URL : {url}\n')
    response = requests.get(url,timeout=10)
    soup = bs(response.text,'html.parser')
    headers = response.headers
    print(f'title : { soup.title.string }\n')