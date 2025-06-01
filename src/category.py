from typing import List
from product import Product

class Category:
    """Класс категории товаров."""

    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.products = []
        for product in products:
            self.add_product(product)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты типа Product или его наследников")
        self.products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {len(self.products)} шт."

    def total_quantity(self) -> int:
        return sum(product.quantity for product in self.products)
