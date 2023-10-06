from abc import ABC, abstractmethod
import copy

# Product class to represent the products
class Product:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability

# DiscountStrategy interface using the Strategy Pattern
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

# Concrete Discount Strategies
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, price):
        return price - (price * (self.percentage / 100))

class BuyOneGetOneFree(DiscountStrategy):
    def apply_discount(self, price):
        return price

# ProductFactory to create product instances using the Prototype Pattern
class ProductFactory:
    def __init__(self):
        self.products = {}

    def create_product(self, name, price, availability):
        if name not in self.products:
            product = Product(name, price, availability)
            self.products[name] = product
        return copy.deepcopy(self.products[name])

# Cart class to manage the shopping cart
class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity=1):
        self.cart_items.append({"product": product, "quantity": quantity})

    def update_quantity(self, product, quantity):
        for item in self.cart_items:
            if item["product"] == product:
                item["quantity"] = quantity
                break

    def remove_from_cart(self, product):
        self.cart_items = [item for item in self.cart_items if item["product"] != product]

    def calculate_total(self):
        total = 0
        for item in self.cart_items:
            product = item["product"]
            quantity = item["quantity"]
            total += product.price * quantity
        return total

    def checkout(self, discount_strategy=None):
        total = self.calculate_total()
        if discount_strategy:
            total = discount_strategy.apply_discount(total)
        return total

# Main function to demonstrate the E-commerce cart system
def main():
    product_factory = ProductFactory()
    laptop = product_factory.create_product("Laptop", 1000, True)
    headphones = product_factory.create_product("Headphones", 50, True)

    cart = Cart()
    cart.add_to_cart(laptop, 1)
    cart.add_to_cart(headphones, 1)

    print("Possible Inputs:")
    print("Products: [{name: 'Laptop', price: 1000, available: true}, {name: 'Headphones', price: 50, available: true}]")
    print("Add to Cart: 'Laptop'")
    print("Update Quantity: 'Laptop, 2'")
    print("Remove from Cart: 'Headphones'\n")

    # Updated code for inputs
    cart.add_to_cart(laptop, 2)  # Update quantity of 'Laptop' to 2
    cart.remove_from_cart(headphones)  # Remove 'Headphones' from the cart

    print("Cart Items:")
    items_in_cart = []
    for item in cart.cart_items:
        product = item['product']
        quantity = item['quantity']
        items_in_cart.append(f"{quantity} {product.name}")
    
    cart_summary = ", ".join(items_in_cart)
    print(f"You have {cart_summary} in your cart.")

    total_bill = cart.calculate_total()
    print(f"Total Bill: Your total bill is ${total_bill}.")

if __name__ == "__main__":
    main()
