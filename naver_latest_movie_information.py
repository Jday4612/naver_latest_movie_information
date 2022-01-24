import requests
from bs4 import BeautifulSoup

url = f"https://movie.naver.com/movie/running/current.naver"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.select("#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li")
    for item in data:
        image = item.select_one('img').get('src')
        link = item.select_one('a').get('href')
        title = item.select_one('img').get('alt')
        film_rate = item.select_one('span').text
        ticket_sales = item.select_one('span.num:nth-child(1)').text + "%"
        rating = item.select_one('span.num').text
        genre = ' '.join(item.select_one('span.link_txt').text.split())

        c = -1
        for d in item.select_one('dd:nth-child(3)').text.split():
            c -= 1
            if '분' in d:
                showtimes = d
                c = 2
            if c == 0:
                release = d
                break

        director = item.select_one('dd:nth-child(4)').text.strip()
        if item.select_one('dd:nth-child(6)') != None:
            cast = ' '.join(item.select_one('dd:nth-child(6)').text.split())

        print("영화 포스터 : ", image)
        print("url       : ", link)
        print("영화 제목   : ", title)
        print("등급       : ", film_rate)
        print("예매율      : ", ticket_sales)
        print("평점       : ", rating)
        print("장르       : ", genre)
        print("상영 시간   : ", showtimes)
        print("개봉 날짜   : ", release)
        print("감독       : ", director)
        print("출연       : ", cast)
        print("*-----------------------------------------------------------------------*")

else:
    print(response.status_code)