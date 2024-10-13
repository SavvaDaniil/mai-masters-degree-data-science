"""
Савва Даниил
Лабораторная работа №1. Часть 2.
"""

import pandas
from pandas import DataFrame
import matplotlib.pyplot as pyplot
from statistics import median, mode

calculated_column_name: str = "Всего"
"""Наименование колонки в файле Excel, для которой производятся расчёты"""


if __name__ == "__main__":
    dataFrame: DataFrame = pandas.read_excel(io="stat_ordinators_2023.xlsx", index_col=0, header=3)

    pyplot.boxplot(x=dataFrame[calculated_column_name])
    pyplot.title("Диаграмма размаха 'ящик с усами' численности ординаторов по возрастам за 2023 год", fontsize=14)
    pyplot.show()

    """
    figure, ax = pyplot.subplots(nrows=2, ncols=1)
    figure.suptitle("Лабораторная работа №1. Часть 2. Савва Даниил", fontsize=14)

    dataFrame[calculated_column_name].plot(ax=ax[0])
    ax[0].set_title(label="Нормальное распределение численности ординаторов\nпо возрастам за 2023 год", fontsize=8)
    ax[0].set_ylabel("Количество", fontsize=6)
    ax[0].set_xlabel("Возраст", fontsize=6)
    ax[0].tick_params(axis='both', which='major', labelsize=6)
    ax[0].grid(True)
    
    dataFrame[calculated_column_name].boxplot(ax=ax[1])
    ax[1].set_title(label="Диаграмма размаха 'ящик с усами' численности ординаторов по возрастам за 2023 год", fontsize=8)
    """

    pyplot.show()
