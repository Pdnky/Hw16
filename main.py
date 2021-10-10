import functional

api_bank_gov = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

functional.API_check(api_bank_gov)

file = open('exchanger.txt', 'w', encoding='utf-8')
functional.Currencies()
file.close()