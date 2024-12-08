from itertools import count, cycle, chain
from typing import Any

def print_value_and_type(value: Any) -> None:
    """Печать переменной и типом данных"""
    print(f'{value} с типом {type(value)}')

if __name__ == '__main__':

    #Бесконечный генератор чисел
    iter_numbers: count = count(0, 3)

    index_numbers: int = 0
    for value in iter_numbers:
        if index_numbers > 10:
            break

        #Применение функций к каждому элементу в итераторе.
        print_value_and_type(value=value)
        index_numbers += 1

    print("##############")
    range_6 = range(1, 6)
    range_10_20 = range(10, 20)

    #Объединение нескольких итераторов в один
    iter_chain: chain = chain(range_6, range_10_20)
    index_numbers: int
    for value in iter_chain:
        print_value_and_type(value=value)