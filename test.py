import pytest
from products import Product, LimitedProduct, NonStockedProduct
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount


def test_create_product():
    product = Product("Test Product", price=100, quantity=10)
    assert product.name == "Test Product"
    assert product.price == 100
    assert product.quantity == 10


def test_create_product_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=100, quantity=10)
    with pytest.raises(ValueError):
        Product("Test Product", price=-10, quantity=10)


def test_product_becomes_inactive():
    product = Product("Test Product", price=100, quantity=1)
    product.buy(1)
    assert not product.is_active()


def test_product_purchase_modifies_quantity():
    product = Product("Test Product", price=100, quantity=10)
    product.buy(3)
    assert product.quantity == 7


def test_buy_larger_quantity_than_exists():
    product = Product("Test Product", price=100, quantity=10)
    with pytest.raises(ValueError):
        product.buy(11)


def test_apply_second_half_price_promotion():
    product = Product("Test Product", price=100, quantity=10)
    promotion = SecondHalfPrice("Second Half Price Promotion")
    product.set_promotion(promotion)
    total_price = product.buy(3)  # Buying 3 items
    assert total_price == 250  # (100 * 2) + (100 / 2)


def test_apply_third_one_free_promotion():
    product = Product("Test Product", price=100, quantity=10)
    promotion = ThirdOneFree("Third One Free Promotion")
    product.set_promotion(promotion)
    total_price = product.buy(6)  # Buying 6 items
    assert total_price == 400  # (100 * 2 * 2)


def test_apply_percent_discount_promotion():
    product = Product("Test Product", price=100, quantity=10)
    promotion = PercentDiscount("30% Discount", percent=30)
    product.set_promotion(promotion)
    total_price = product.buy(2)  # Buying 2 items
    assert total_price == 140  # (100 - 30%) * 2
