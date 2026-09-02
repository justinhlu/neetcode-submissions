class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append([timestamp, value])
        else:
            self.timeMap[key] = []
            self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        vals = self.timeMap.get(key, [])

        l = 0
        r = len(vals)-1

        while l <= r:
            m = (l+r) // 2
            if vals[m][0] <= timestamp:
                res = vals[m][1]
                l = m + 1
            else:
                r = m - 1

        return res
