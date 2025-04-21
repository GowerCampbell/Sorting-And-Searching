# Import the Enum class to create more structured enumeration types
from enum import Enum

# ENUMERATIONS: These define a set of named constants with specific meanings
# Instead of using strings directly, we use Enums for better type safety and readability
class OrderStatus(Enum):
    # Defines the possible states an order can be in
    PENDING = "Pending"      # Order just created, not yet processed
    PREPARING = "Preparing"  # Order is being made
    READY = "Ready"          # Order is complete and ready for pickup
    COMPLETED = "Completed"  # Order has been fully processed and delivered

class PaymentStatus(Enum):
    # Defines the possible states of payment for an order
    PENDING = "Pending"      # Payment is awaiting processing
    COMPLETED = "Completed"  # Payment has been successfully processed
    CANCELED = "Canceled"    # Payment was stopped or reversed

# PRODUCT CLASS: Represents an individual item that can be ordered
class Product:
    def __init__(self, name, price, id=0):
        # Initialize a product with its core attributes
        self.id = id          # Unique identifier (optional)
        self.name = name      # Name of the product (e.g., "Espresso")
        self.price = price    # Cost of the product

# ORDER ITEM CLASS: Represents a specific product in an order with its quantity
class OrderItem:
    def __init__(self, product, quantity):
        self.product = product    # The actual Product object
        self.quantity = quantity  # Number of this product in the order

    def get_total_price(self):
        # Calculate the total price for this specific item
        # Total = Product price * Quantity
        return self.product.price * self.quantity

# ORDER CLASS: Represents the entire customer order
class Order:
    def __init__(self, order_id):
        self.order_id = order_id               # Unique identifier for the order
        self.items = []                        # List to store OrderItems
        self.status = OrderStatus.PENDING      # Initial status of the order
        self.total_amount = 0.0                # Total cost of the order
        self.payment_status = PaymentStatus.PENDING  # Initial payment status

    def add_item(self, product, quantity):
        # Method to add a new item to the order
        # 1. Create a new OrderItem
        # 2. Add it to the list of items
        # 3. Recalculate the total order cost
        item = OrderItem(product, quantity)
        self.items.append(item)
        self.calculate_total()

    def calculate_total(self):
        # Calculate the total cost of all items in the order
        # Uses a list comprehension to sum the prices of all items
        self.total_amount = sum(item.get_total_price() for item in self.items)
        return self.total_amount

    def update_status(self, status):
        # Method to update the current status of the order
        self.status = status

    def __str__(self):
        # Special method to create a string representation of the order
        # Provides a formatted view of the entire order details
        items_str = "\n".join(
            f"  - {item.product.name} x{item.quantity} = ${item.get_total_price():.2f}"
            for item in self.items
        )
        return (
            f"Order ID: {self.order_id}\n"
            f"Status: {self.status.value}\n"
            f"Payment: {self.payment_status.value}\n"
            f"Items:\n{items_str}\n"
            f"Total: ${self.total_amount:.2f}"
        )

# VIEW CLASS: Handles user interface and interactions
class CafeView:
    def __init__(self, controller):
        # Initialize the view with a reference to the controller
        # This allows the view to interact with the business logic
        self.controller = controller

    @staticmethod
    def display_menu(products):
        # Display the list of available products with their prices
        print("\nAvailable Products:")
        for idx, product in enumerate(products, start=1):
            print(f"{idx}. {product.name} - ${product.price:.2f}")

    @staticmethod
    def display_order_summary(order):
        # Show the details of a specific order
        print(f"\nOrder Summary for Order ID {order.order_id}:")
        print(order)

    @staticmethod
    def display_orders(orders):
        # Display all current orders in the system
        if orders:
            print("\nCurrent Orders:")
            for order in orders:
                print(order)
        else:
            print("\nNo orders yet.")

    @staticmethod
    def display_message(message):
        # Generic method to display messages to the user
        print(message)

    def take_order(self):
        # Method to guide the user through creating a new order
        # 1. Create a new order
        # 2. Allow adding multiple items
        # 3. Validate inputs
        # 4. Show order summary
        order = self.controller.create_order()
        while True:
            # Display menu and get product selection
            self.display_menu(self.controller.products)
            
            # Get valid product index
            product_idx = self.get_valid_input(
                "Select a product (by number): ", 
                int, 1, len(self.controller.products)
            )
            
            # Get valid quantity
            quantity = self.get_valid_input("Enter quantity: ", int, 1)

            # Add the selected item to the order
            product = self.controller.products[product_idx - 1]
            order.add_item(product, quantity)
            print(f"Added {quantity} x {product.name} to your order.")

            # Ask if user wants to add more items
            more = input("Add more items? (yes/no): ").strip().lower()
            if more != "yes":
                break

        # Show the final order summary
        self.display_order_summary(order)

    @staticmethod
    def get_valid_input(prompt, input_type, min_value=None, max_value=None):
        # Robust input validation method
        # Ensures that:
        # 1. Input is of the correct type
        # 2. Input is within specified range (if provided)
        while True:
            try:
                # Convert input to specified type
                value = input_type(input(prompt))
                
                # Check if value is within specified range
                if (min_value is not None and value < min_value) or \
                   (max_value is not None and value > max_value):
                    raise ValueError
                
                return value
            except ValueError:
                print("Invalid input. Please try again.")

# CONTROLLER CLASS: Manages the business logic and coordinates between model and view
class OrderController:
    def __init__(self):
        # Initialize the system with empty orders and predefined products
        self.orders = []                  # List to store all orders
        self.next_order_id = 1            # Counter for generating unique order IDs
        self.products = [                 # Predefined menu of products
            Product("Espresso", 3.0),
            Product("Latte", 4.5),
            Product("Cappuccino", 4.0),
            Product("Mocha", 5.0),
        ]

    def get_order(self, order_id):
        # Find and return an order by its ID
        # Uses next() with a generator expression for efficient searching
        return next((order for order in self.orders if order.order_id == order_id), None)

    def create_order(self):
        # Create a new order with a unique ID
        order = Order(self.next_order_id)
        self.orders.append(order)
        self.next_order_id += 1
        return order

    def add_item_to_order(self, order_id, product_idx, quantity):
        # Add an item to an existing order
        # Includes validation to ensure order and product exist
        order = self.get_order(order_id)
        if not order:
            return False, "Order not found."
        if product_idx < 1 or product_idx > len(self.products):
            return False, "Invalid product selection."
        
        product = self.products[product_idx - 1]
        order.add_item(product, quantity)
        return True, f"Added {quantity} x {product.name} to Order {order_id}."

# MAIN FUNCTION: Entry point of the application
def main():
    # Set up the system components
    controller = OrderController()
    view = CafeView(controller)

    # Main program loop
    while True:
        # Display menu and get user choice
        print("\n=== Coffee Order System ===")
        print("1. New Order")
        print("2. Add Item to Existing Order")
        print("3. View All Orders")
        print("4. Exit")

        choice = input("Please select an option (1-4): ")

        # Handle different user choices
        if choice == "1":
            view.take_order()
        elif choice == "2":
            # Add item to an existing order
            try:
                order_id = int(input("Enter Order ID: "))
                view.display_menu(controller.products)
                product_idx = view.get_valid_input(
                    "Select a product (by number): ", 
                    int, 1, len(controller.products)
                )
                quantity = view.get_valid_input("Enter quantity: ", int, 1)
                success, message = controller.add_item_to_order(order_id, product_idx, quantity)
                view.display_message(message)
            except ValueError:
                view.display_message("Invalid input. Please try again.")
        elif choice == "3":
            view.display_orders(controller.orders)
        elif choice == "4":
            print("Thank you for using the Coffee Order System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Ensure the main function only runs if the script is executed directly
if __name__ == "__main__":
    main()
