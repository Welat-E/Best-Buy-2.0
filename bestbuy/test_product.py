import pytest
from products import Product
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount

def test_apply_second_half_price_promotion():
    product = Product("Test Product", price=100, quantity=10)
    promotion = SecondHalfPrice("Second Half Price Promotion")
    product.set_promotion(promotion)
    total_price = product.buy(3)  # Buying 3 items
    assert total_price == 200  # (100 / 2) + 100

def test_apply_third_one_free_promotion():
    product = Product("Test Product", price=100, quantity=10)
    promotion = ThirdOneFree("Third One Free Promotion")
    product.set_promotion(promotion)
    total_price = product.buy(6)  # Buying 6 items
    assert total_price == 400  # (100 * 2 * 2) + (100 * 2) = 400

def test_apply_percent_discount_promotion():
    product = Product("Test Product", price=100, quantity=10)
    promotion = PercentDiscount("30% Discount", percent=30)
    product.set_promotion(promotion)
    total_price = product.buy(2)  # Buying 2 items
    assert total_price == 140  # (100 - 30%) * 2
