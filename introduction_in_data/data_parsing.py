import requests
from bs4 import BeautifulSoup

# списки
years = []  # список годов
labels = []  # список названий
price_matrix = []  # матрица для результатов

# цены
prise_office = []  # офисы
retail_space = []  # торговые площадки
garages = []  # гаражи


# реализация библиотек requests и BeautifulSoup
URL_TEMPLATE = 'https://rosrealt.ru/moskva/cena/?t=dinamika'
r = requests.get(URL_TEMPLATE)
src = r.text  # считываем текст HTML-документа

soup = BeautifulSoup(src, 'lxml')  # применяем парсер 'lxml' к src (в переменной src находится текст)
t = 'table publication__table'  # переменная t содержит название класса для переменной table_data
table_data = soup.find_all('table', class_=t)[1]  # используем функцию soup.find_all("тэг поиска", "класс")

all_trs = table_data.find_all('tr')  # в table_data находим все переменные с тэгом 'tr'
# print(type(all_trs))  # вывод типа переменной all_trs


# сбор данных в таблицы
lables_of_table = table_data.find_all('th')
for th in lables_of_table:  # получаем таблицу с общими названиями
    lable_of_table = th.text  # переводим в текст
    lable_of_table = lable_of_table.replace('₽/м²', '')  # производим замену лишнего
    lable_of_table = lable_of_table.replace('/год', '')
    labels.append(lable_of_table)  # дополняем таблицу новыми данными
    labels_table = labels[1:4]  # новая таблица на выходе с наименовниями

for tr in all_trs:  # для всех тэгов tr в all_trs покажи
    # print(tr.find_all('td'))
    results = []
    all_tds = tr.find_all('td')  # цены в строке по именованиями (пример: 2013, 5 (офис), 6 (дом), 3 (квартира) ...)
    for td in all_tds:  # вытаскиваем цены в текстовом формате
        elements = td.text
        element = elements.replace(' ', '')
        results.append(element)
    price_matrix.append(results)
price_matrix = price_matrix[1:-1]

for i in price_matrix:
    years.append(int(i[0]))
    prise_office.append(int(i[1]))
    retail_space.append(int(i[2]))
    garages.append(int(i[3]))

