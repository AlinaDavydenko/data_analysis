import matplotlib.pyplot as plt
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

