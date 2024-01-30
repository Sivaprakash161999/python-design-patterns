from abc import ABC, abstractmethod


class Publisher(ABC):
    @abstractmethod
    def notify_observers(self):
        pass


class WeatherData(Publisher):
    def __init__(self, temperature=None, pressure=None, humidity=None):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self.temperature, self.pressure, self.humidity)

    def set_measurements(self, temperature, pressure, humidity):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        self.notify_observers()


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class CurrentConditionsDisplay(Observer):
    def update(self, temperature, pressure, humidity):
        print(f"Current Conditions:: Temperature: {temperature}deg, "
               + f"Pressure: {pressure} psi, humidity: {humidity}")


class StatisticsDisplay(Observer):
    def update(self, temperature, pressure, humidity):
        print(f"Statistics:: Temperature: {temperature}deg, "
               + f"Pressure: {pressure} psi, humidity: {humidity}")


class ForecastDisplay(Observer):
    def update(self, temperature, pressure, humidity):
        print(f"Forecast:: Temperature: {temperature}deg, "
               + f"Pressure: {pressure} psi, humidity: {humidity}")
        

publisher = WeatherData()

observer1 = CurrentConditionsDisplay()
observer2 = StatisticsDisplay()
observer3 = ForecastDisplay()

publisher.attach(observer1)
publisher.attach(observer2)
publisher.attach(observer3)

publisher.set_measurements(37, 80, 45)


