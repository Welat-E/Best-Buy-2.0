import pytest
from products import Product
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount


#test for applying the Second Half Price promo
def test_apply_second_half_price_promotion():
    """
    Test the Second Half Price promotion for a product. It checks if the 
    promotion correctly calculates the total price when buying multiple items.
    """
    product = Product("Test Product", price=100, quantity=10)
    promotion = SecondHalfPrice("Second Half Price Promotion")
    product.set_promotion(promotion)
    total_price = product.buy(3)  # Buying 3 items
    assert total_price == 250  # (100 / 2) + 100 + 100


#test for applying the Third One Free promo
def test_apply_third_one_free_promotion():
    """
    Test the Third One Free promotion for a product. It verifies the correct 
    total price when buying multiple items where every third item is free.
    """
    product = Product("Test Product", price=100, quantity=10)
    promotion = ThirdOneFree("Third One Free Promotion")
    product.set_promotion(promotion)
    total_price = product.buy(6)  # Buying 6 items
    assert total_price == 400  # (100 * 2 * 2)


#test for applying the Percent Discount promotion
def test_apply_percent_discount_promotion():
    """
    Test the Percent Discount promotion for a product. It ensures the correct 
    total price when a percentage discount is applied to each item.
    """
    product = Product("Test Product", price=100, quantity=10)
    promotion = PercentDiscount("30% Discount", percent=30)
    product.set_promotion(promotion)
    total_price = product.buy(2)  # Buying 2 items
    assert total_price == 140  # (100 - 30%) * 2
