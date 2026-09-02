class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append([value,timestamp])
        else:
            self.timeMap[key] = []
            self.timeMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.timeMap:
            for val, timestamp_prev in self.timeMap[key]:
                if timestamp_prev <= timestamp:
                    res = val
        return res
