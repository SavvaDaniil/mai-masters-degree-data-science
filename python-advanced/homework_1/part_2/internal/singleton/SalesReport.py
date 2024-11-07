from internal.singleton.SingletonMeta import SingletonMeta
from internal.entity.Product import Product
from internal.model.ShelfProductData import ShelfProductData

class SalesReport(metaclass=SingletonMeta):
    """Отчёт о продажах"""

    sales: dict = {}
    """Словарь с данными о продажах в формате "имя продукта" => ShelfProductData"""

    def add_sale(self, product: Product, count: int) -> None:
        """Добавить покупку в отчёт о продажах"""
        if self.sales is None:
            self.sales = {}
        if count < 0:
            return
        
        if product.name not in self.sales:
            self.sales[product.name] = ShelfProductData(count=0, price=product.price)

        self.sales[product.name].count =+ count

    def print_sales(self) -> None:
        """Распечатать в консоль отчёт о продажах"""

        print("\nОтчёт о продажах")
        for product_name, product_data in self.sales.items():
            print(product_name + " - " + str(product_data.price) + " у.е. - " + str(product_data.count) + " шт. - " + str(product_data.price * product_data.count) + "  у.е.")
        print("\n")