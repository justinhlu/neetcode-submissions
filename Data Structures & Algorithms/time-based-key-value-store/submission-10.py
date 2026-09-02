class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((timestamp, value))
        else:
            self.timeMap[key] = []
            self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key in self.timeMap:
            for i in range(len(self.timeMap[key])):
                if self.timeMap[key][i][0] <= timestamp:
                    res = self.timeMap[key][i][1]
                 

        return res
        
