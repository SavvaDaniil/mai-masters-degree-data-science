import pandas as pd
from pandas import DataFrame
import numpy
import matplotlib.pyplot as plt
from scipy import stats

data_general: DataFrame = pd.read_excel('viborki.xlsx', header=0, sheet_name="Генеральная совокупность")
data_random: DataFrame = pd.read_excel('viborki.xlsx', header=0, sheet_name="Случайная выборка")
data_stratified: DataFrame = pd.read_excel('viborki.xlsx', header=0, sheet_name="Белгородская область")

#print(data.head())

COLUMN_NAME: str = "Количество мужчин и женщин"

# Среднего значения по выборкам
print(f"Среднее значение (генеральная совокупность): {data_general[COLUMN_NAME].mean():.2f}")
print(f"Среднее значение (случайная выборка): {data_random[COLUMN_NAME].mean():.2f}")
print(f"Среднее значение (стратифицированная выборка): {data_stratified[COLUMN_NAME].mean():.2f}")


def confidence_interval(data: DataFrame, confidence: float) -> tuple:
    """Расчет доверительного интервала"""
    length = len(data)
    mean = numpy.mean(data)
    sem = stats.sem(data)  # standard error of the mean
    margin = sem * stats.t.ppf((1 + confidence) / 2, length - 1)
    return mean - margin, mean + margin

# Доверительные интервалы для случайной выборки
print("\n")
print(f"Доверительный интервал - случайная выборка 90%: {confidence_interval(data=data_random[COLUMN_NAME], confidence=0.90)}")
print(f"Доверительный интервал - случайная выборка 95%: {confidence_interval(data=data_random[COLUMN_NAME], confidence=0.95)}")
print(f"Доверительный интервал - случайная выборка 99%: {confidence_interval(data=data_random[COLUMN_NAME], confidence=0.99)}")

# Доверительные интервалы для стратифицированной выборки
print("\n")
print(f"Доверительный интервал - стратифицированная выборка 90%: {confidence_interval(data=data_stratified[COLUMN_NAME], confidence=0.90)}")
print(f"Доверительный интервал - стратифицированная выборка 95%: {confidence_interval(data=data_stratified[COLUMN_NAME], confidence=0.95)}")
print(f"Доверительный интервал - стратифицированная выборка 99%: {confidence_interval(data=data_stratified[COLUMN_NAME], confidence=0.99)}")