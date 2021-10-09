import requests
import datetime

api_bank_gov = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

bank_gov = requests.request('GET', api_bank_gov)
bank_gov.json()


with open('Bank_gov.txt', encoding='utf-8') as f:
    data = f.readlines()

file = open('exchanger.txt', 'w', encoding='utf-8')

def Time_Request():
    """
    Функция добавляющая время в начало текстового файла
    :return:
    """
    file.write(f'[{datetime.datetime.now()}]' + '\n')

def Currencies():
    """
    Функция которая выводит курс валют в текстовый файл
    :return:
    """
    counter = 0
    for line in data:

        if len(line) < 5:
            continue

        counter += 1

        first_name = line.find('"txt":')
        first_price = line.find('","rate":')
        second_price = line.find(',"cc"')

        Currency_name = (line[first_name+7:first_price])
        Currency_price = (line[first_price+9:second_price])

        file.write(f'{counter}. {Currency_name} to UAH: {Currency_price}' + '\n')

Time_Request()
Currencies()

file.close()
