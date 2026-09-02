"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 1:
            return 0
        if len(intervals) < 2:
            return 1
        
        res = 1

        startTimes, endTimes = [], []

        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)
        
        startTimes.sort()
        endTimes.sort()

        s = 0
        e = 0
        count = 0

        while s < len(startTimes):
            if startTimes[s] < endTimes[e]:
                count += 1
                s += 1
            elif endTimes[e] <= startTimes[s]:
                e += 1
                count -= 1
            
            res = max(res, count)

        return res