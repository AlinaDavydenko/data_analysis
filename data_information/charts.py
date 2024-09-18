import matplotlib.pyplot as plt
import numpy as np
from data_parsing import years, prise_office, retail_space, garages


# 1 график Line Plots
def line_plots():
    """ функция реализует график Line Plots, показывает динамику ценообразования недвижимости на Московском рынке"""
    x = years
    y1 = prise_office
    y2 = retail_space
    y3 = garages
    plt.plot(x, y1, label="offices")
    plt.plot(x, y2, label="retail_space")
    plt.plot(x, y3, label="garages")
    plt.plot()

    plt.xlabel("years")
    plt.ylabel("prices")
    plt.title("Analysis of Moscow building's prices")
    plt.legend()
    plt.show()


# 2 график Bar Plots
def bar_plots():
    """ функция реализует график Bar Plots, показывает соотношение цен """
    x1 = years  # список годы
    # цены по годам
    y1 = prise_office
    y2 = retail_space
    y3 = garages

    width = 0.35  # ширина столбца
    fig, ax = plt.subplots()

    ax.bar(x1, y1, width, label='Office', color='b')
    # Указываем с помощью параметра bottom, что значения в столбце должны быть выше значений переменной
    ax.bar(x1, y2, width, bottom=y1, label='Retail space', color='g')
    ax.bar(x1, y3, width, bottom=y2, label='Garages', color='r')

    ax.set_ylabel('Соотношение в стоимости')
    ax.set_title('Анализ ценообразования недвижимости в Москве')

    # Сдвигаем легенду в нижний левый угол, чтобы она не перекрывала часть графика
    ax.legend(loc='lower left', title='Недвижимость')

    plt.show()


# 3 график Pie Charts
def pie_charts():
    """ функция реализует график Pie Charts, круговая диаграмма """
    x = years
    y = garages

    plt.pie(y, labels=x)
    plt.title('Изменение стоимости гаражей по годам')
    plt.show()


# 4 диаграмма scatterplot
def d_scatterplot():
    """ функция реализует диаграмму рассеяния - scatterplot"""
    x = years
    y = prise_office

    plt.scatter(x, y)
    plt.show()


# 5 Stack Plots
def stack_plots():
    """ Stack Plots graphs"""
    idxes = years
    arr1 = prise_office
    arr2 = retail_space
    arr3 = garages

    # Adding legend for stack plots is tricky.
    plt.plot([], [], color='r', label='D 1')
    plt.plot([], [], color='g', label='D 2')
    plt.plot([], [], color='b', label='D 3')

    plt.stackplot(idxes, arr1, arr2, arr3, colors=['r', 'g', 'b'])
    plt.title('Изменение стоимости')
    plt.legend()
    plt.show()


# 6 one line
def one_line():
    """ graphs for office price """
    plt.plot(years, prise_office)
    plt.show()


#7 Combining charts
def combining_charts():
    """ Combining charts of Line Plots and Bar Plots """
    x = years
    y = retail_space

    plt.bar(x, y, label='Prices of retail space')  # Параметр label позволяет задать название величины для легенды
    plt.plot(x, y, color='green', marker='o', markersize=7)

    plt.xlabel('Years')
    plt.ylabel('Price')
    plt.title('Combining charts')
    plt.legend()
    plt.show()
