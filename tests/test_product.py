import pytest
from product import Product, Smartphone, LawnGrass
from category import Category


def test_product_str():
    p = Product("Товар", "Описание", 1000.0, 10)
    assert str(p) == "Товар, 1000 руб. Остаток: 10 шт."


def test_product_add_same_type():
    p1 = Product("Товар1", "Описание", 100.0, 2)
    p2 = Product("Товар2", "Описание", 200.0, 3)
    assert p1 + p2 == 100 * 2 + 200 * 3


def test_product_add_different_type():
    p1 = Smartphone("iPhone", "desc", 100.0, 2, 99.9, "14", 256, "black")
    p2 = LawnGrass("Трава", "desc", 200.0, 3, "Россия", "7 дней", "зелёный")
    with pytest.raises(TypeError):
        _ = p1 + p2


def test_smartphone_attributes():
    s = Smartphone("Phone", "desc", 999.0, 5, 95.5, "X", 128, "white")
    assert s.model == "X"
    assert s.efficiency == 95.5


def test_lawn_grass_attributes():
    g = LawnGrass("Grass", "desc", 199.0, 10, "США", "5 дней", "зелёный")
    assert g.country == "США"
    assert g.germination_period == "5 дней"


def test_category_add_valid():
    c = Category("Тест", "desc", [])
    p = Product("Тестовый", "desc", 10.0, 1)
    c.add_product(p)
    assert p in c.products


def test_category_add_invalid():
    c = Category("Тест", "desc", [])
    with pytest.raises(TypeError):
        c.add_product("не продукт")


def test_category_product_count():
    Category.product_count = 0  # сброс на случай других тестов
    c = Category("Тест", "desc", [])
    c.add_product(Product("P1", "desc", 100, 1))
    c.add_product(Product("P2", "desc", 100, 1))
    assert Category.product_count == 2


def test_category_str():
    p1 = Product("A", "B", 100, 3)
    p2 = Product("C", "D", 200, 2)
    cat = Category("Категория", "desc", [p1, p2])
    assert str(cat) == "Категория, количество продуктов: 2 шт."
    assert cat.total_quantity() == 5
