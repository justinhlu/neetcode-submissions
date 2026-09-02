class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                self.cache.append(tmp)
                return tmp[1]
        
        return -1

    def put(self, key: int, value: int) -> None:
        # Check if key is in cache and update
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                tmp[1] = value
                self.cache.append(tmp)
                return
        # If not in cache then check if capacity is exceeded
        if len(self.cache) >= self.capacity:
            self.cache.pop(0)
        
        # Finally add to the stack
        self.cache.append([key,value])
        return