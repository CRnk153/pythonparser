import requests
from bs4 import BeautifulSoup
import os
from datetime import date
import csv

url = 'https://weather.com/uk-UA/weather/today/l/aef1ae844a5a6d6514dd32c8f723d7cd1ad4e49f08085207b5c0b336a9d0116d'
resp = requests.get(url)
today = str(date.today())
today_weather = []

def parse(r):
    soup = BeautifulSoup(r.text, 'lxml')
    values = soup.find('ul', class_='WeatherTable--columns--6JrVO WeatherTable--wide--KY3eP').findAll('li', class_='''Column--column--3tAuz''')

    for value in values:
        time = value.find('a').find('h3')
        degree = value.find('a').find('div', attrs={'data-testid': 'SegmentHighTemp'})
        data = [today, {time.text: degree.text}]
        string = f'{list(data[1].keys())[0]} - {list(data[1].values())[0]}'
        today_weather.append(string)
        csv_write([[data[0], list(data[1].keys())[0], list(data[1].values())[0]]])
    txt_write(today_weather)


def txt_file():
    return open(f'{os.getcwd()}\\Погода.txt', 'w', newline='')
def txt_write(rows):
    with open(f'{os.getcwd()}\\Погода.txt', 'a', newline='') as file:
        file.write(f'\nУ {today}: \n')
        for row in rows:
            file.write('\n'+row+'\n')

def os_if_txt(path):
    if os.path.exists(path):
        pass
    else:
        txt_file()

def os_if_csv(path):
    if os.path.exists(path):
        pass
    else:
        csv_file()
def csv_file():
    f = open(f'{os.getcwd()}\\Погода.csv', 'w', newline='')
    with open(f'{os.getcwd()}\\Погода.csv', 'a', newline='') as file:
        w = csv.writer(file)
        w.writerows([['data', 'time', 'value']])

def csv_write(rows):
    with open(f'{os.getcwd()}\\Погода.csv', 'a', newline='') as file:
        w = csv.writer(file)
        w.writerows(rows)

if __name__ == '__main__':
    os_if_txt(f'{os.getcwd()}\\Погода.txt')
    os_if_csv(f'{os.getcwd()}\\Погода.csv')
    parse(resp)
