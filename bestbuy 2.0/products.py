class Product:
    """
    Represents a product in the store.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a new Product instance.
        """
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0
        self.promotion = None  # Initialize with no promotion

    def get_quantity(self):
        """
        Returns the quantity of the product in stock.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product in stock.
        """
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")
        self.quantity = quantity
        self.active = self.quantity > 0

    def is_active(self):
        """
        Checks if the product is active (in stock).
        """
        return self.active

    def set_promotion(self, promotion):
        """
        Sets a promotion for the product.
        """
        self.promotion = promotion

    def get_promotion(self):
        """
        Returns the current promotion of the product.
        """
        return self.promotion

    def buy(self, quantity):
        """
        Processes the purchase of the product with promotion if applicable.
        """
        if quantity > self.quantity:
            raise ValueError("Requested quantity exceeds available stock")
        
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price
        
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        
        return total_price

    def show(self):
        """
        Returns a string representation of the product details.
        """
        promotion_info = f" Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promotion_info}"



class NonStockedProduct(Product):
    """
    Represents a non-stocked product (e.g., software licenses) in the store.
    """

    def __init__(self, name, price):
        """
        Initializes a new NonStockedProduct instance.

        Args:
            name (str): The name of the non-stocked product.
            price (float): The price of the non-stocked product.
        """
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """
        Prevents changing the quantity of a non-stocked product.
        """
        pass  # Non-stocked products do not track quantity

    def buy(self, quantity):
        """
        Processes the purchase of a non-stocked product.

        Args:
            quantity (int): The quantity to purchase.

        Returns:
            float: The total price of the purchase.
        """
        return quantity * self.price

    def show(self):
        """
        Returns a string representation of the non-stocked product details.
        """
        return f"{self.name} (Non-Stocked), Price: ${self.price}"


class LimitedProduct(Product):
    """
    Represents a product with a purchase limit in the store.
    """

    def __init__(self, name, price, quantity, maximum):
        """
        Initializes a new LimitedProduct instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
            maximum (int): The maximum quantity that can be purchased
            in a single order.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """
        Processes the purchase of the product with a quantity limit.

        Args:
            quantity (int): The quantity to purchase.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the requested quantity exceeds the maximum limit.
        """
        if quantity > self.maximum:
            raise ValueError(
                f"Cannot purchase more than {self.maximum} of {self.name} in a single order"
            )
        return super().buy(quantity)

    def show(self):
        """
        Returns a string representation of the limited product details.
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Max per order: {self.maximum}"
