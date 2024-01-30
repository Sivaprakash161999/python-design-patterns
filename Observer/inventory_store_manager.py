from abc import ABC, abstractmethod
 
# Define the Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, product_name: str, new_stock: int) -> None:
        """Notify the observer with a product's updated stock level."""
        pass
 
# Define the Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attach an observer."""
        pass
 
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Detach an observer."""
        pass
 
    @abstractmethod
    def notify(self) -> None:
        """Notify all attached observers."""
        pass
 
# Define the StoreManager class which implements the Observer interface
class StoreManager(Observer):
    def __init__(self, name: str):
        """Initialize with the manager's name."""
        self._name = name
 
    def update(self, product_name: str, new_stock: int) -> None:
        """Print the notification when the manager gets updated about stock changes."""
        print(f"{self._name} was notified that {product_name} stock level is now {new_stock}")
 
# Define the Inventory class which implements the Subject interface
class Inventory(Subject):
    def __init__(self, threshold: int = 10):
        """Initialize with a threshold, empty observers list and empty products dictionary."""
        self._observers = []
        self._products = {}
        self._threshold = threshold
 
    def attach(self, observer: Observer) -> None:
        """Add an observer to the list of observers."""
        self._observers.append(observer)
 
    def detach(self, observer: Observer) -> None:
        """Remove an observer from the list of observers."""
        self._observers.remove(observer)
 
    def notify(self, product_name: str, new_stock: int) -> None:
        """Notify each observer about the stock change of a product."""
        for observer in self._observers:
            observer.update(product_name, new_stock)
 
    def update_stock(self, product_name: str, new_stock: int) -> None:
        """Update the stock level of a product and notify if it's below the threshold."""
        self._products[product_name] = new_stock
        if new_stock < self._threshold:
            self.notify(product_name, new_stock)
 
# Test the functionality
if __name__ == "__main__":
    # Create a new inventory instance
    inventory = Inventory()
    
    # Manually set initial stock levels
    inventory._products = {
        "Apples": 10,
        "Oranges": 25,
        "Bananas": 50,
    }
    
    # Create two store managers and attach them to the inventory
    manager1 = StoreManager("Alice")
    manager2 = StoreManager("Bob")
    inventory.attach(manager1)
    inventory.attach(manager2)
    
    # Test the notification mechanism with stock updates
    print("Stock level update 1:")
    inventory.update_stock("Apples", 5)  # Should notify both managers
    print("\nStock level update 2:")
    inventory.update_stock("Bananas", 60)  # Should not notify as stock level increased
    
    # Detach one manager and test notifications again
    inventory.detach(manager1)
    print("\nStock level update 3:")
    inventory.update_stock("Oranges", 8)  # Should notify only manager2