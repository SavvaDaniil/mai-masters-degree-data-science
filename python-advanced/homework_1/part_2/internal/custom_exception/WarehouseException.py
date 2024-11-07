
class ProductLessThanNeedRemoveWarehouseException(Exception):
    """Продукта на складке меньше, чем требуется удалить"""

    def __init__(self, count_exists: int, count_need_delete: int):
        super().__init__("product in warehouse {count_exists} less than need to remove from warehouse {count_need_delete}".format(count_exists=count_exists, count_need_delete=count_need_delete))

class NoProductInWarehouseException(Exception):

    def __init__(self, product_name: str):
        super().__init__("there is no product \"{product_name}\" in warehouse".format(product_name=product_name))


class NotEnoughProductsInWarehouseException(Exception):

    def __init__(self, product_name: str, count_in_warehouse: int, count_need: int):
        super().__init__("not enough products \"{product_name}\" in warehouse, {count_in_warehouse}, but need {count_need}".format(product_name=product_name, count_in_warehouse=count_in_warehouse, count_need=count_need))