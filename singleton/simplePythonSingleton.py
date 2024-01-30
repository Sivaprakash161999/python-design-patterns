

class Singleton:
    _instance = None

    # override the new method to control
    # how new objects are created
    def __new__(cls):
        if not cls._instance: # Lazy instantiation
            cls._instance = super().__new__(cls)
        return cls._instance
    
s1 = Singleton()
