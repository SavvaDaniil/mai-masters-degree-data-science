
class ProductPriceBelowZeroException(Exception):
    """Цена продукта меньше нуля"""

    def __init__(self):
        super().__init__("product price less than zero")