import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


bot = telegram.Bot(token='995019804:AAFcvvlVXxf82UZCth4ga6F8Sqy2zfNPy8Q')

url25 = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20191225'
url21 = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20191221'
url20 = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20191220'
url18 = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20191218'

t = 10

"""
title_list20 = soup20.select('div.info-movie')
for i in title_list20:
    print(i.select_one('a>strong').text.strip())
"""

def job_function():
    html25 = requests.get(url25)
    html21 = requests.get(url21)
    html20 = requests.get(url20)
    html18 = requests.get(url18)
    soup25 = BeautifulSoup(html25.text, 'html.parser')
    soup21 = BeautifulSoup(html21.text, 'html.parser')
    soup20 = BeautifulSoup(html20.text, 'html.parser')
    soup18 = BeautifulSoup(html18.text, 'html.parser')

    imax25 = soup25.select_one('span.imax')
    imax21 = soup21.select_one('span.imax')
    imax20 = soup20.select_one('span.imax')
    imax18 = soup18.select_one('span.imax')

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if(imax20):
        imax20=imax20.find_parent('div',class_='col-times')
        title = (imax20.select_one('div.info-movie>a>strong').text.strip())
        print(title+ ' 20일 금요일 IMAX가 열렸습니다.('+current_time+')')
        bot.sendMessage(chat_id=933629941, text=title+ ' 20일 금요일 IMAX가 열렸습니다.')
    else:
        global t
        if t == 0:
            print(current_time+': 20일 금요일 IMAX가 아직 열리지 않았습니다.')
            bot.sendMessage(chat_id=933629941, text='20일 금요일 IMAX가 아직 열리지 않았습니다.')
            t += 10
        else:
            print(current_time+': 20일 금요일 IMAX가 아직 열리지 않았습니다.')
            t -= 1

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()

