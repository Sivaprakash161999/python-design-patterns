from abc import ABC, abstractmethod

class ShippingCarrier(ABC):
    def __init__(self, delivery_charge):
        self.delivery_charge = delivery_charge

    @abstractmethod
    def calculate_shipping_cost(self, weight):
        return weight * self.delivery_charge

class FedexCarrier(ShippingCarrier):

    def calculate_shipping_cost(self, weight):
        return weight * self.delivery_charge


class UPSCarrier(ShippingCarrier):

    def calculate_shipping_cost(self, weight):
        return weight * self.delivery_charge


class DHLCarrier(ShippingCarrier):

    def calculate_shipping_cost(self, weight):
        return weight * self.delivery_charge


class AmazonCarrier(ShippingCarrier):

    def calculate_shipping_cost(self, weight):
        return weight * self.delivery_charge





def calculate_shipping_cost(weight, carrier):
    cost = 0
    if carrier == "FedEx":
        cost = weight * 2.5
    elif carrier == "UPS":
        cost = weight * 3
    elif carrier == "DHL":
        cost = weight * 4
    return cost


carriers = {
    1: ('Fedex', FedexCarrier(2.5)),
    2: ('UPS', UPSCarrier(3)),
    3: ('DHL', DHLCarrier(4)),
    4: ('Amazon', AmazonCarrier(3.25)),
}


print("Select a carrier for shipping:")
print("1. FedEx")
print("2. UPS")
print("3. DHL")
print("4. Amazon")

choice = int(input("Enter the number corresponding to your choice: "))
weight = float(input("Enter the weight of the package (in pounds): "))

try:
    carrier, carrier_obj = carriers[choice]
    shipping_cost = carrier_obj.calculate_shipping_cost(weight)
    print(f"The shipping cost for {carrier} is ${shipping_cost:.2f}")
except KeyError as e:
    # raise ValueError(f'{choice} is not a valid choice')
    raise ValueError(f"{e} is not a valid choice.")