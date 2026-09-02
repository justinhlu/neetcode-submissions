class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        n = len(intervals)
        if n == 1:
            return 0
        intervals.sort(key = lambda x: x[0])
        i = 1
        current = intervals[0]

        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]

            if start < current[1]:
                res += 1
                current[1] = min(end, current[1])
            else:
                current = intervals[i]
            i += 1
        
        return res