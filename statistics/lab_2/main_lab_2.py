"""
Савва Даниил
Лабораторная работа №2. Часть 1.
"""

import pandas
from pandas import DataFrame
import matplotlib.pyplot as pyplot
from statistics import median, mode
from math import sqrt, pi, e
from typing import List


calculated_column_name: str = "массой тела 500 - 999 г."
"""Наименование колонки в файле Excel, для которой производятся расчёты"""
header_column_name: str = "Года"


def gausa(x: int, average: float, standard_deviation: float) -> float:
    return round(number=(1 / (standard_deviation * sqrt(2 * pi))) * e ** ((-1/2) * ((x - average) / (standard_deviation)) ** 2), ndigits=10)

if __name__ == "__main__":


    dataFrame: DataFrame = pandas.read_excel(io="stat_weights_of_newborns.xlsx", index_col=0, header=0)

    print("Исследование нормального распределения состояния здоровья новорожденных массой тела 500 - 999 г.\n")

    average: float = sum(dataFrame[calculated_column_name]) / len(dataFrame[calculated_column_name])
    print("Среднее значение состояние здоровья новорожденных: " + str(round(number=average, ndigits=2)))
    moda: float = round(number=mode(data=dataFrame[calculated_column_name].astype('int').to_list()), ndigits=2)
    print("Моды (наиболее часто встречающего значения): " + str(moda))
    calculated_median: float = round(number=median(data=dataFrame[calculated_column_name].to_list()), ndigits=1)
    print("Медиана: " + str(calculated_median))

    shift: float = abs((calculated_median - average)) / ((calculated_median + average) / 2) * 100
    print("Процент смещения медианы от среднего: " + 
        str(
            round(
                number=shift, 
                ndigits=2
            )
        ) + "% (" + ("меньше 15%" if shift < 15 else "больше 15%") + ")")
    

    math_waiting: float = 0.0
    dispersion: float = 0.0
    listX: List[int] = []
    empirical_moment_4_prepare: float = 0.0
    for index, value in dataFrame.iterrows():
        math_waiting += value.values[0]
        dispersion += value.values[0] ** 2
        listX.append(value.values[0])
        empirical_moment_4_prepare += (value.values[0] - average) ** 4
    math_waiting = round(number=math_waiting / len(dataFrame.index), ndigits=2)
    print("Математическое ожидание: " + str(math_waiting))

    dispersion = round(number=(dispersion / len(dataFrame.index) - math_waiting ** 2), ndigits=2)
    print("Дисперсия: " + str(dispersion) + " квадратных единиц")

    standard_deviation: float = round(number=sqrt(dispersion), ndigits=2)
    print("Среднее квадратичное отклонение: " + str(standard_deviation))

    asymmetry: float = round(number=(average - moda) / standard_deviation, ndigits=2)
    print("Наблюдается " + ("левосторонняя" if average < moda else "правосторонняя") + " ассиметрия со значением: " + str(asymmetry))

    empirical_moment_4: float = empirical_moment_4_prepare / len(dataFrame.index)
    print("Центральный эмпирический момент четвёртого порядка: ", round(number=empirical_moment_4, ndigits=2))

    excess: float = round(number=empirical_moment_4 / standard_deviation ** 4 - 3, ndigits=2)
    print("Коэффициент эксцесса:", excess)


    listX.sort()
    listY: List[float] = [gausa(x=x, average=average, standard_deviation=standard_deviation) for x in listX]
    #print(listX)
    #print(listY)
    #dataFrameGausa = pandas.DataFrame(data={"y" : listY, "x" : listX})


    """
    figure, ax = pyplot.subplots(nrows=3, ncols=1)#(ax_plot, ax_hist, ax_pie)
    figure.suptitle("Лабораторная работа №2. Савва Даниил", fontsize=14)
    
    dataFrame[calculated_column_name].plot(ax=ax[0])
    ax[0].set_title(label="Нормальное распределение состояния здоровья новорожденных", fontsize=8)
    ax[0].set_ylabel("Количество новорожденных", fontsize=6)
    ax[0].set_xlabel("Года", fontsize=6)
    ax[0].tick_params(axis='both', which='major', labelsize=8)
    ax[0].grid(True)
    
    dataFrame[calculated_column_name].hist(ax=ax[1])
    ax[1].set_xlabel("Распределение состояния здоровья новорожденных", fontsize=6)
    ax[1].tick_params(axis='both', which='major', labelsize=6)
    
    ax[2].pie(
        dataFrame[calculated_column_name], 
        labels=dataFrame.index, 
        textprops={
            'fontsize':6
        }
    )
    """

    pyplot.plot(listX, listY)
    pyplot.hist(x=listX, density=True)

    print("\n---\n")


    

    pyplot.show()



