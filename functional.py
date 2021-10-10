import requests
import datetime

def API_check(api):
    bank_gov = requests.request('GET', api)

    if 200 >= bank_gov.status_code < 300:
        file = open('Bank_gov.txt', 'w', encoding='utf-8')
        file.write(bank_gov.text)
        file.close()
    else:
        raise(f'Error: {bank_gov.status_code}')


def Currencies():
    counter = 0

    with open('Bank_gov.txt', encoding='utf-8') as f:
        data = f.readlines()

    file = open('exchanger.txt', 'a', encoding='utf-8')

    file.write(f'[{datetime.datetime.now()}]' + '\n')

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

