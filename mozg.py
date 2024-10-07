import requests
from bs4 import BeautifulSoup
import pyttsx3
import datetime

engine = pyttsx3.init()
engine.setProperty('rate',150)#скорость озвучки
engine.setProperty('voice','ru')#казали что будт руский голос и скорость
def synthesize_text(text):
    engine.say(text)
    engine.runAndWait()

def weather():
    url = 'https://tengrinews.kz/weather/ust-kamenogorsk/day/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,'lxml')
    now = soup.find(class_= 'weather-city-all-temp-value').text.replace(' ','').replace('\n','')
    ostolnoe = soup.find(class_='weather-city-other').text.replace(' ','').replace('\n','').split()
    text = 'температура сейчас',now.replace('°C','градусов'),'ветер',ostolnoe[0].replace('м/с','метров в секунду'), 'вероятность осадков', ostolnoe[1], 'давление', ostolnoe[2].replace('мм', 'милиметров')
    synthesize_text(text)
# weather()
#     return text
# print(weather())


# w = weather()#запук функции через переменную

def news():
    url1 = 'https://tengrinews.kz/'
    req = requests.get(url1 +'/')
    soup = BeautifulSoup(req.content,'lxml')
    popular_news = soup.find_all(class_='main-news_top_item_title')


    for numbe in range(5):
        synthesize_text(popular_news[numbe])

def tim():
    tims = datetime.datetime.today().strftime('%H-%M-%S').split('-')
    text=f'сейчас {tims[0]} часов {tims[1]} мин {tims[2]} секунд'
    synthesize_text(text)
#     return text
# print(tim())
# tim()

def today():
    day= datetime.datetime.today().strftime('%d-%m-%Y').split('-')
    wecks= ['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье']
    w = datetime.date.today()
    wec= datetime.datetime.weekday(w)
    text = f'сегодня {day[0]} день, {day[1]} месяц, {day[2]} год, {wecks[wec]}'
    # print(text)
#     synthesize_text(text)
# today()

def rospisanie():
    w = datetime.date.today()
    wec = datetime.datetime.weekday(w)
    if wec== 0:
        synthesize_text('Сегодня увас 2 физики, 2 биологии, физра, алгебра , география, класный час')
    elif wec == 1:
        synthesize_text('Сегодня у вас 2 истории казахстана, 2 биологии, 2 алгебры и физра')
    elif wec == 2:
        synthesize_text('Сегодня у вас русский , русская литиратура, 2 английских, алгебра , право , труды')
    elif wec == 3:
        synthesize_text('Сегодня у вас 2 казахских, всемирная история, геометрия, stem,  и география')
    elif wec == 4:
        synthesize_text('Сегодня у вас русский , русская литиратура, биология, глобюкомпет, информатика, казахский, английский')