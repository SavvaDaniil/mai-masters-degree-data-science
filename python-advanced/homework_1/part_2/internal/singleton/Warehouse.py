from internal.singleton.SingletonMeta import SingletonMeta
from internal.entity.Product import Product
from internal.custom_exception.WarehouseException import ProductLessThanNeedRemoveWarehouseException
from typing import List
from dataclasses import dataclass
from internal.util.LoggerUtil import logger
from internal.model.ShelfProductData import ShelfProductData


class Warehouse(metaclass=SingletonMeta):
    """Склад"""

    # Так как нет базы данных, а объект warehouse заменяет таблицу базы данных для хранения, у Product нет идентификатора, что позволял бы отличить один вид product от другого, поэтому будет хранится словарем по свойству product.name и соответствующим данным ShelfProductData

    shelfs: dict = {}

    def add_product(self, product: Product, count: int) -> None:
        """Добавление товара на склад"""
        if self.shelfs is None:
            self.shelfs = {}
        if count < 0:
            return
        
        if product.name not in self.shelfs:
            self.shelfs[product.name] = ShelfProductData(count=0, price=product.price)

        self.shelfs[product.name].count += count
        logger.info(msg="Продукт {name} стоимость {price} и количеством {count} добавлен на склад".format(
            name=product.name,
            price=product.price,
            count=count
        ))

    def remove_product(self, product: Product, count: int) -> None:
        """Удаление товара со склада"""
        if self.shelfs is None:
            self.shelfs = {}
        if count < 0:
            return
        
        #self.products.append(product)
        if product.name not in self.shelfs:
            self.shelfs[product.name] = 0

        if self.shelfs[product.name].count < count:
            raise ProductLessThanNeedRemoveWarehouseException(self.shelfs[product.name].count, count)
        
        self.shelfs[product.name].count -= count
        logger.info(msg="Продукт {name} стоимость {price} и количеством {count} был изъят со склада".format(
            name=product.name,
            price=product.price,
            count=count
        ))

    def calculation_of_the_total_amount(self) -> int:
        """Расчёт общей стоимости товаров на складке"""
        amount: int = 0

        for _, shelfProductData in self.shelfs.items():
            amount += shelfProductData.price * shelfProductData.count

        return amount

    

