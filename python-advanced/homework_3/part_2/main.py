
import re
import collections
from collections import Counter

def count_unique_words(value_str: str) -> int:
    """Количество уникальных слов в строке, игнорируя знаки препинания и пробелы"""
    value_str = re.sub(r'[^\w\s]', '', value_str)
    return len(list(collections.Counter(value_str.split(' '))))

if __name__ == '__main__':
    print(count_unique_words(value_str="Строка, со словами словами"))