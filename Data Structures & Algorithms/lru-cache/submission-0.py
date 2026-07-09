from datetime import datetime

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key: (val, timestamp)
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            return self.cache[key][0]

        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity:
            least_recent_key = min(self.cache, key=lambda k: self.cache[k][1]) 
            del self.cache[least_recent_key]

        self.cache[key] = (value, datetime.now())
                
    
