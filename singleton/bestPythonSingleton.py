# Using Meta-Classes is the best way to implement Singletons in Python

class SingletonMeta(type):
    # Dictionary stores the single instance of class
    # for each subclass of the SingletonMeta metaclass
    _instances = {}

    def __call__(cls, *args, **kwargs): 
        if cls not in cls._instances: # Lazy instantiation
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
# actual Singleton
class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass

s1 = Singleton()


