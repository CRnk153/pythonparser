import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import date

url = 'https://weather.com/uk-UA/weather/today/l/aef1ae844a5a6d6514dd32c8f723d7cd1ad4e49f08085207b5c0b336a9d0116d'
resp = requests.get(url)
today = str(date.today()).split('-')
today[0] += ' року '
today[1] += ' місяця '
today[2] += ' числа'
today = ''.join(today)
today_weather = []

def parse(r):
    soup = BeautifulSoup(r.text, 'lxml')
    values = soup.find('ul', class_='WeatherTable--columns--6JrVO WeatherTable--wide--KY3eP').findAll('li', class_='''Column--column--3tAuz''')

    for value in values:
        time = value.find('a').find('h3')
        degree = value.find('a').find('div', attrs={'data-testid': 'SegmentHighTemp'})
        data = [today, {time.text: degree.text}]
        string = f'{data[0]}: {list(data[1].keys())[0].lower()} {list(data[1].values())[0]}'
        today_weather.append(string)
    csv_write([today_weather])
def csv_file():
    return open(f'{os.getcwd()}\\Погода.csv', 'w', newline='')

def csv_write(rows):
    w = csv.writer(csv_file())
    for row in rows:
        w.writerows(row)

if __name__ == '__main__':
    parse(resp)
