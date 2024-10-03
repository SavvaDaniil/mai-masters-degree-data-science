"""
Савва Даниил
Лабораторная работа №1. Часть 1.
"""

import pandas
from pandas import DataFrame
import matplotlib.pyplot as pyplot
from statistics import median, mode


calculated_column_name: str = "Да, ежедневно"
"""Наименование колонки в файле Excel, для которой производятся расчёты"""


def __print_lab_countings(dataFrame: DataFrame, column_name: str, string_to_console_about_average: str) -> None:
    """Печать в консоль расчетов для лабораторной работы"""
    average: float = sum(dataFrame[column_name]) / len(dataFrame[column_name])
    print(string_to_console_about_average + ": " + str(round(number=average, ndigits=2)))
    print("Моды (наиболее часто встречающего значения): " + str(round(number=mode(data=dataFrame[column_name].astype('int').to_list()), ndigits=2)))
    calculated_median: float = round(number=median(data=dataFrame[column_name].to_list()), ndigits=1)
    print("Медиана: " + str(calculated_median))

    shift: float = abs((calculated_median - average)) / ((calculated_median + average) / 2) * 100
    print("Процент смещения медианы от среднего: " + 
        str(
            round(
                number=shift, 
                ndigits=2
            )
        ) + "% (" + ("меньше 15%" if shift < 15 else "больше 15%") + ")")


if __name__ == "__main__":

    figure, ax = pyplot.subplots(nrows=3, ncols=3)#(ax_plot, ax_hist, ax_pie)
    figure.suptitle("Лабораторная работа №1. Часть 1. Савва Даниил", fontsize=14)

    dataFrame: DataFrame = pandas.read_excel(io="stat_smoke_22_2022.xlsx", index_col=0, header=0)

    print("Исследование нормального распределения процента курящих ежедневно по возрастам за 2022 год\n")
    __print_lab_countings(
        dataFrame=dataFrame, 
        column_name=calculated_column_name, 
        string_to_console_about_average="Среднее значение процента ежедневно курящих"
    )
    
    dataFrame[calculated_column_name].plot(ax=ax[0, 0])
    ax[0, 0].set_title(label="Нормальное распределение процента курящих\nежедневно по возрастам за 2022 год", fontsize=8)
    ax[0, 0].set_ylabel("Процент курящих ежедневно", fontsize=6)
    ax[0, 0].set_xlabel("Возраст", fontsize=6)
    ax[0, 0].tick_params(axis='both', which='major', labelsize=8)
    ax[0, 0].grid(True)
    
    dataFrame[calculated_column_name].hist(ax=ax[1, 0])
    ax[1, 0].set_xlabel("Распределение процентов курящих", fontsize=6)
    ax[1, 0].tick_params(axis='both', which='major', labelsize=6)
    
    ax[2, 0].pie(
        dataFrame[calculated_column_name], 
        labels=dataFrame.index, 
        textprops={
            'fontsize':6
        }
    )

    print("\n---\n")

    dataFrame_2: DataFrame = pandas.read_excel(io="stat_ordinators_2023.xlsx", index_col=0, header=3)
    calculated_column_name = "Всего"

    print("Исследование нормального распределения численности ординаторов по возрастам за 2023 год\n")
    __print_lab_countings(
        dataFrame=dataFrame_2, 
        column_name=calculated_column_name, 
        string_to_console_about_average="Среднее значение количества ординаторов по возрасту"
    )
    
    dataFrame_2[calculated_column_name].plot(ax=ax[0, 1])
    ax[0, 1].set_title(label="Нормальное распределение численности ординаторов\nпо возрастам за 2023 год", fontsize=8)
    ax[0, 1].set_ylabel("Количество", fontsize=6)
    ax[0, 1].set_xlabel("Возраст", fontsize=6)
    ax[0, 1].tick_params(axis='both', which='major', labelsize=6)
    ax[0, 1].grid(True)
    
    dataFrame_2[calculated_column_name].hist(ax=ax[1, 1])
    ax[1, 1].set_xlabel("Соотношение количества", fontsize=6)
    ax[1, 1].tick_params(axis='both', which='major', labelsize=6)
    
    ax[2, 1].pie(
        dataFrame_2[calculated_column_name], 
        labels=dataFrame_2.index, 
        textprops={
            'fontsize':6
        }
    )

    #Исследование равномерного распределения индекса
    print("\n---\n")

    dataFrame_3: DataFrame = pandas.read_excel(io="stat_for_meat_index_price_2024.xlsx", index_col=0, header=1)
    calculated_column_name = "Индекс в % к предыдущей дате регистрации"

    print("Исследование равномерного распределения изменения индекса потребительских цен (тарифов) на говядину за 2024 год\n")
    __print_lab_countings(
        dataFrame=dataFrame_3, 
        column_name=calculated_column_name, 
        string_to_console_about_average="Индексы потребительских цен (тарифов) на говядину"
    )
    
    dataFrame_3[calculated_column_name].plot(ax=ax[0, 2])
    ax[0, 2].set_title(label="Равномерное распределение изменения индекса\nпотребительских цен (тарифов) на говядину за 2024 год", fontsize=8)
    ax[0, 2].set_xlabel("На даты", fontsize=6)
    ax[0, 2].set_ylabel("Изменение индекса в %\nк предыдущей дате регистрации", fontsize=6)
    ax[0, 2].set_ylim([0, 110])
    ax[0, 2].tick_params(axis='both', which='major', labelsize=6)
    ax[0, 2].grid(True)
    
    dataFrame_3[calculated_column_name].hist(ax=ax[1, 2])
    ax[1, 2].set_xlabel("Соотношение количества", fontsize=6)
    ax[1, 2].tick_params(axis='both', which='major', labelsize=6)
    
    ax[2, 2].pie(
        dataFrame_3[calculated_column_name], 
        labels=dataFrame_3.index, 
        textprops={
            'fontsize':6
        }
    )
    

    

    pyplot.show()




