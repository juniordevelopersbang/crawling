import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('td.info')
rank = 1
for song in songs:
    title = song.find('a', {'class': "title ellipsis"}).text
    singer = song.find('a', {'class': "artist ellipsis"}).text
    print(rank, title.strip(),  singer.strip())
    rank += 1
