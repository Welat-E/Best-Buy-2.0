from products import Product, LimitedProduct, NonStockedProduct
from store import Store
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount


# Start the store program with a menu and process user actions


def start(store):
    """
    Display the store menu and process user input to perform actions such as
    listing products, showing total amount, making an order, or quitting the
    program.

    :param store: Store object containing the list of products.
    """
    while True:
        print("\nStore Menu\n----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Please choose a number: ")

        if choice == "1":
            store.show_list_products()
        elif choice == "2":
            total_quantity = store.get_total_quantity()
            print(f"Total quantity in store: {total_quantity}")
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Thank you for your purchase. Honor us again soon, goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


# Facilitate the order process by allowing users to select products


def make_order(store):
    """
    Facilitate the ordering process by allowing users to select products
    and specify quantities. Validate inputs and notify the user if the
    requested quantity exceeds available stock or maximum limit.
    """
    shopping_list = []
    not_enough_stock = False
    while True:
        print("\n------")
        for i, product in enumerate(store.list_products, start=1):
            promotion_info = (
                f" (Promotion: {product.promotion.name})" if product.promotion else ""
            )
            print(
                f"{i}. {product.name}, Price: ${product.price}, "
                f"Quantity: {product.quantity}{promotion_info}"
            )
        print("------")
        product_number = input("Which product do you want? (or 'done' to finish): ")

        if product_number.lower() == "done" or product_number == "":
            break

        try:
            product_index = int(product_number) - 1
            if 0 <= product_index < len(store.list_products):
                selected_product = store.list_products[product_index]
                quantity = int(
                    input(f"Enter the quantity for {selected_product.name}: ")
                )

                # is it a limited product?
                if (
                    isinstance(selected_product, LimitedProduct)
                    and quantity > selected_product.maximum
                ):
                    print(
                        f"You cannot purchase more than {selected_product.maximum} of {selected_product.name} in a single order."
                    )
                    continue

                # check if the requested quantity is available
                if quantity > selected_product.get_quantity():
                    print(
                        f"Requested quantity exceeds available stock for {selected_product.name}."
                    )
                    not_enough_stock = True
                else:
                    shopping_list.append((selected_product, quantity))
            else:
                print("Invalid product number. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    if shopping_list:
        total_price = store.order(shopping_list)
        if not_enough_stock:
            print("There is not enough stock.")
            return
        print(f"Order cost: ${total_price:.2f}")

    """
    Facilitate the ordering process by allowing users to select products
    and specify quantities. Validate inputs and notify the user if the
    requested quantity exceeds available stock or maximum limit.
    """
    shopping_list = []
    not_enough_stock = False
    while True:
        print("\n------")
        for i, product in enumerate(store.list_products, start=1):
            print(
                f"{i}. {product.name}, Price: ${product.price}, "
                f"Quantity: {product.quantity}"
            )
        print("------")
        product_number = input("Which product do you want? (or 'done' to finish): ")

        if product_number.lower() == "done" or product_number == "":
            break

        try:
            product_index = int(product_number) - 1
            if 0 <= product_index < len(store.list_products):
                selected_product = store.list_products[product_index]
                quantity = int(
                    input(f"Enter the quantity for {selected_product.name}: ")
                )

                # is it a limited product?
                if (
                    isinstance(selected_product, LimitedProduct)
                    and quantity > selected_product.maximum
                ):
                    print(
                        f"You cannot purchase more than {selected_product.maximum} of {selected_product.name} in a single order."
                    )
                    continue

                # check if the requested quantity is available
                if quantity > selected_product.get_quantity():
                    print(
                        f"Requested quantity exceeds available stock for {selected_product.name}."
                    )
                    not_enough_stock = True
                else:
                    shopping_list.append((selected_product, quantity))
            else:
                print("Invalid product number. Please try again.")
            total_price = store.order(shopping_list)
            if not_enough_stock:
                print("There is not enough stock.")
                return
            if total_price == 0:
                print(f"Order cost: {total_price} dollars.")

        except ValueError:
            print("Invalid input. Please enter a number.")


# Main function to set up initial stock and start the store program


def main():
    """
    Main func. to setup initial stock of inventory & start the store program.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
