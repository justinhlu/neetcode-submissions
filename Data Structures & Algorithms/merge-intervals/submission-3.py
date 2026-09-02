class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        current = intervals[0]

        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]

            if start <= current[1]:
                current[1] = max(end, current[1])
            else:
                res.append(current)
                current = intervals[i]
            i += 1
        
        res.append(current)

        return res