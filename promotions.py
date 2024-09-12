from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for promotions.
    """
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Applies the promotion to product & returns the total discounted price.
        """
        pass


class SecondHalfPrice(Promotion):
    """
    Promotion where the second item is at half price.
    """
    def apply_promotion(self, product, quantity):
        # Check if there is only one item, no promotion
        if quantity < 2:
            return product.price * quantity
        
        # Calculate the price: every second item is at half price
        # For odd quantities, the last item is at full price
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        
        total_price = (full_price_items * product.price) + (half_price_items * product.price / 2)
        return total_price


class ThirdOneFree(Promotion):
    """
    Promotion where the third item is free (buy 2, get 1 free).
    """
    def apply_promotion(self, product, quantity):
        if quantity < 3:
            return product.price * quantity
        # Every third item is free
        total_price = (quantity // 3) * (2 * product.price) + (quantity % 3) * product.price
        return total_price


class PercentDiscount(Promotion):
    """
    Promotion that applies a percentage discount to the product.
    """
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent


    def apply_promotion(self, product, quantity):
        discount = product.price * (self.percent / 100)
        discounted_price = product.price - discount
        return discounted_price * quantity


