"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 1
        if len(intervals) < 1:
            return 0
        elif len(intervals) < 2:
            return res

        startTimes = []
        endTimes = []
        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)
        
        startTimes.sort()
        endTimes.sort()
        print(startTimes)
        print(endTimes)
        s = 0
        e = 0
        count = 0
        while s < len(startTimes):
            if startTimes[s] < endTimes[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1

            res = max(res, count)
        return res