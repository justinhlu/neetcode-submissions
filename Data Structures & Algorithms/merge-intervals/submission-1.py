class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(intervals)
        if n == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])

        current = intervals[0]

        for i in range(1,n):
            start = intervals[i][0]
            end = intervals[i][1]

            if start <= current[1]:
                current[1] = max(end, current[1])
            else:
                res.append(current)
                current = intervals[i]
        res.append(current)

        return res