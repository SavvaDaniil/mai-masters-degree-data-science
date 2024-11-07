

from internal.singleton.Warehouse import Warehouse
from internal.singleton.SalesReport import SalesReport
from internal.entity.Product import Product
from internal.entity.Seller import Seller

warehouse: Warehouse = Warehouse()
product: Product = Product(name="Вилка", price=30)


warehouse.add_product(product=product, count=12)
warehouse.remove_product(product=product, count=2)
print(warehouse.shelfs)


seller: Seller = Seller(name="Продавец 1")

seller.sale(product=product, count=6)

print(warehouse.calculation_of_the_total_amount())

print("Выручка за продажи продавца {seller_name} равна: {profit}".format(
    seller_name=seller.name,
    profit=seller.profit
))

salesReport: SalesReport = SalesReport()
salesReport.print_sales()