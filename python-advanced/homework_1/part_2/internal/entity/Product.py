
from dataclasses import dataclass

@dataclass
class Product():

    name: str
    price: int

    """Не очень понимаю, зачем количество товара в самой сущности. Как сущность, должна быть одна, а количество уже на складе указано"""
    """
    count: int
    def count_add(self, value: int) -> None:
        if value < 0:
            return
        self.count += value

    def count_minus(self, value: int) -> None:
        if value > 0:
            return
        self.count -= value
    """