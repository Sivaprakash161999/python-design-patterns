

class ClassicSingleton:
    # class level variable to store single class instance
    _instance = None

    # override the __init__ method to control initialization
    def __init__(self):
        # raise an error to prevent constructor utilization
        raise RuntimeError("call get_instance() instead")
    
    @classmethod
    def get_instance(cls):
        if not cls._instance: # Lazy instantiation
            # create new instance of the class
            cls._instance = cls.__new__(cls)
        
        # return the single instance either newly created or already existing
        return cls._instance
    

s1 = ClassicSingleton.get_instance()
    


