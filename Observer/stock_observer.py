from abc import ABC, abstractmethod


class Publisher(ABC):
    @abstractmethod
    def notify_observers(self):
        pass

class Stock(Publisher):
    def __init__(self, symbol, price, change_in_price=0):
        self.symbol = symbol
        self.price = price
        self.change_in_price = change_in_price
        self._observers = []

    def notify_observers(self):
        for observer in self._observers:
            if isinstance(observer, PriceDisplay):
                observer.update(self.price)
            elif isinstance(observer, ChangeDisplay):
                observer.update(self.change_in_price)

    def set_price(self, price):
        prev = self.price
        self.price = price
        self.change_in_price = self.price - prev
        self.notify_observers()

    def attach(self, observer):
        self._observers.append(observer)


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class PriceDisplay(Observer):
    def update(self, price):
        print(f"Stocks current price is {price}")


class ChangeDisplay(Observer):
    def update(self, change_in_price):
        print(f"The stocks price changed by {change_in_price}")


stock_publisher = Stock("xy", 100)

price_observer = PriceDisplay()
change_observer = ChangeDisplay()

stock_publisher.attach(price_observer)
stock_publisher.attach(change_observer)

stock_publisher.set_price(200)
stock_publisher.set_price(50)

