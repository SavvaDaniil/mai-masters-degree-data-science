from typing import List

def summ_of_list_numbers(numbers: List[int]) -> int:
    """Вычислить сумму всех чисел в передаваемом списке"""
    summ: int = 0
    for i in numbers:
        summ += i
    return summ