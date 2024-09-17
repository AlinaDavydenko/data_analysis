import requests
from bs4 import BeautifulSoup
# import pandas as pd

# списки
years = []
labels = []
prise_office = []


URL_TEMPLATE = 'https://rosrealt.ru/moskva/cena/?t=dinamika'
r = requests.get(URL_TEMPLATE)
src = r.text  # считываем текст HTML-документа

soup = BeautifulSoup(src, 'lxml')  # применяем парсер 'lxml' к src (в переменной src находится текст)
t = 'table publication__table'  # переменная t содержит название класса для переменной table_data
table_data = soup.find_all('table', class_=t)[1]  # используем функцию soup.find_all("тэг поиска", "класс")

all_trs = table_data.find_all('tr')  # в table_data находим все переменные с тэгом 'tr'
# print(type(all_trs))  # вывод типа переменной all_trs

lables_of_table = table_data.find_all('th')

for th in lables_of_table:  # получаем таблицу с общими названиями
    lable_of_table = th.text  # переводим в текст
    lable_of_table = lable_of_table.replace('₽/м²', '')  # производим замену лишнего
    lable_of_table = lable_of_table.replace('/год', '')
    labels.append(lable_of_table)  # дополняем таблицу новыми данными
    labels_table = labels[1::]  # новая таблица на выходе с наименовниями




# for tr in all_trs:  # для всех тэгов tr в all_trs покажи
#     print(tr.find_all('td'))
#     all_tds = tr.find_all('td')
#     for td in all_tds:
#         print(td.text)
#     print('***'*50)
