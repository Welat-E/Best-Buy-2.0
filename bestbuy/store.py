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


    # Method to calculate the total quantity of products
    def get_total_quantity(self):
        """
        Returns the total quantity of all products in the store.

        Returns:
            int: Total quantity of all products in the store.
        """
        return sum(product.quantity for product in self.list_products)


    # Method to process the order for a list of products
    def order(self, shopping_list):
        """
        Processes an order for the products in the shopping list.

        Args:
            shopping_list (list): A list of tuples, each containing a product 
                                  and quantity.

        Returns:
            float: The total price of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if product.quantity >= quantity:
                product.set_quantity(product.quantity - quantity)
                total_price += product.price * quantity
            else:
                print(f"Not enough stock for {product.name}.")
        return total_price
