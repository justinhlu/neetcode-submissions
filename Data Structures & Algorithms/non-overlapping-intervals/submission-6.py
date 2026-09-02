class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        
        res = 0

        intervals.sort(key=lambda x:x[0])
        current = intervals[0]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start < current[1]:
                current[1] = min(end, current[1]) # Remove the bigger end to leave room for more intervals
                res += 1
            else:
                current = intervals[i]
            
        return res