from abc import ABC, abstractmethod
 
# Step 1: Create the DiscountStrategy interface
class DiscountStrategy(ABC):
 
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass
 
# Step 2: Implement the discount strategies
class NoDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total
 
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage
 
    def apply_discount(self, total: float) -> float:
        return total * (1 - self.percentage / 100)
 
class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, fixed_amount: float):
        self.fixed_amount = fixed_amount
 
    def apply_discount(self, total: float) -> float:
        return max(total - self.fixed_amount, 0)
 
# Step 3: Implement the ShoppingCart class
class ShoppingCart:
 
    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy
        self.items = {}
 
    def add_item(self, item: str, price: float):
        self.items[item] = price
 
    def remove_item(self, item: str):
        if item in self.items:
            del self.items[item]
 
    def get_total(self) -> float:
        return sum(self.items.values())
 
    def get_total_after_discount(self) -> float:
        total = self.get_total()
        return self.discount_strategy.apply_discount(total)
 
# Step 4: Test your implementation
if __name__ == "__main__":
    # Create a shopping cart with a 10% percentage discount
    cart = ShoppingCart(PercentageDiscount(10))
 
    # Add a few items
    cart.add_item("Item 1", 10.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 3", 30.0)
 
    # Calculate and print the total price before discount
    print("Total before discount:", cart.get_total())
 
    # Calculate and print the total price after applying the discount
    print("Total after discount:", cart.get_total_after_discount())