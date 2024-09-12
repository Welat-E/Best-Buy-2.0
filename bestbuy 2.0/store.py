import promotions

# Store class to manage product-related operations


class Store:

    def __init__(self, product_list):
        """
        Initialize the store with a list of products.

        Args:
            product_list (list): A list of product objects.
        """
        self.list_products = product_list

    # Method to print all products in the store
    def show_list_products(self):
        """
        Prints the details of all products in the store.
        """
        for product in self.list_products:
            print(product.show())  # Call the show method of each product

    # Method to process the order for a list of products


    def order(self, shopping_list):
        """
        Processes an order for the products in the shopping list.

        Args:
            shopping_list (list): A list of tuples, each containing a product
                                and quantity.

        Returns:
            float: The total price of the order, or a message if out of stock.
        """
        total_price = 0
        for product, quantity in shopping_list:
            # Check if the requested quantity is greater than the available stock
            if product.quantity < quantity:
                print(f"There is not enough stock for {product.name}.")
                return "There is no stock"  # Exit the function with a stock warning

            # Apply promotion if available
            if product.promotion:
                total_price += product.promotion.apply_promotion(product, quantity)
            else:
                total_price += product.price * quantity

            # Reduce stock after a successful order
            product.set_quantity(product.quantity - quantity)

        return total_price

    # New method to get the total quantity of all products in the store
    def get_total_quantity(self):
        """
        Returns the total quantity of all products in the store.

        Returns:
            int: The sum of quantities for all products.
        """
        total_quantity = sum(product.quantity for product in self.list_products)
        return total_quantity
