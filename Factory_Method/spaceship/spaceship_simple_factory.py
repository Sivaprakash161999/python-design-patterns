from abc import ABC, abstractmethod
from enum import Enum

class SpaceShipType(Enum):
    MILLINIUM_FALCON = 'millinium_falcon'
    UNSC_INFINITY = 'unsc_infinity'
    USS_ENTERPRISE = 'uss_enterprise'
    SERENITY = 'serenity'


class SpaceShipAbstract(ABC):
    def __init__(self, position, size, displayName, speed):
        self.position = position
        self.size = size
        self.displayName = displayName
        self.speed = speed

    @abstractmethod
    def get_info(self):
        pass

class MilliniumFalcon(SpaceShipAbstract):
    def get_info(self):
        print(f"{self.displayName} is a Millinium Falcon")

class UNSCInfinity(SpaceShipAbstract):
    def get_info(self):
        print(f"{self.displayName} is a UNSCInfinity")

class USSEnterprise(SpaceShipAbstract):
    def get_info(self):
        print(f"{self.displayName} is an USS Enterprise")

class Serenity(SpaceShipAbstract):
    def get_info(self):
        print(f"{self.displayName} is a Serenity")


class SpaceShipFactory:
    @staticmethod
    def create_spaceship(context):
        if context.spaceship_type == SpaceShipType.MILLINIUM_FALCON:
            return MilliniumFalcon(context.position, context.size,
                                    context.display_name, context.speed)
        elif context.spaceship_type == SpaceShipType.UNSC_INFINITY:
            return UNSCInfinity(context.position, context.size,
                                context.display_name, context.speed)
        elif context.spaceship_type == SpaceShipType.USS_ENTERPRISE:
            return USSEnterprise(context.position, context.size,
                                context.display_name, context.speed)
        elif context.spaceship_type == SpaceShipType.SERENITY:
            return Serenity(context.position, context.size,
                                context.display_name, context.speed)
        else:
            raise ValueError(f"{context.spaceship_type} is invalid spaceship")

class SpaceshipContext:
    def __init__(self, type, position, size, display_name, speed):
        self.spaceship_type = type
        self.position = position
        self.size = size
        self.display_name = display_name
        self.speed = speed


data = [
    [SpaceShipType.MILLINIUM_FALCON, (1, 2), (1, 2), 'ABC', (1, 2)],
    [SpaceShipType.UNSC_INFINITY, (2, 3), (2, 3), 'DEF', (2, 3)],
    [SpaceShipType.USS_ENTERPRISE, (3, 4), (3, 4), 'GHI', (3, 4)],
    [SpaceShipType.SERENITY, (4, 5), (4, 5), 'JKL', (4, 5)],
    ["fsjl", (5, 6), (6, 7), 'MNO', (5, 6)]
]

ss_f = SpaceShipFactory()

for spaceship_info in data:
    c = SpaceshipContext(*spaceship_info)
    try:
        ss = ss_f.create_spaceship(c)
        ss.get_info()
    except ValueError as e:
        print(e)


        

