import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    # __new__ override
    def __new__(cls):
        # acquire the lock to ensure thread safety
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        
        return cls._instance
    
            
s1 = ThreadSafeSingleton()