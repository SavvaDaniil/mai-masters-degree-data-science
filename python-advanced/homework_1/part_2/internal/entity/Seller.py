from dataclasses import dataclass

from internal.entity.Product import Product
from internal.singleton.Warehouse import Warehouse
from internal.singleton.SalesReport import SalesReport
from internal.custom_exception.WarehouseException import NoProductInWarehouseException, NotEnoughProductsInWarehouseException
from internal.util.LoggerUtil import logger

@dataclass
class Seller:
    """Продавец"""

    name: str

    profit: int = 0
    """Выручка"""

    def sale(self, product: Product, count: int) -> None:
        """Продажа товара со складка"""

        warehouse: Warehouse = Warehouse()
        if product.name not in warehouse.shelfs:
            raise NoProductInWarehouseException(product_name=product.name)
        
        if count > warehouse.shelfs[product.name].count:
            raise NotEnoughProductsInWarehouseException(
                product_name=product.name,
                count_in_warehouse=warehouse.shelfs[product.name].count,
                count_need=count
            )

        warehouse.remove_product(product=product, count=count)

        salesReport: SalesReport = SalesReport()
        salesReport.add_sale(product=product, count=count)

        self.profit +=  warehouse.shelfs[product.name].count *  warehouse.shelfs[product.name].price

        logger.info(msg="Выполнена продажа товара {product_name} стоимостью {product_price} и количеством {product_count} продавцом \"{seller_name}\"".format(
            product_name=product.name,
            product_price=product.price,
            product_count=count,
            seller_name=self.name
        ))
