"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True

        sortedIntervals = intervals.sort(key=lambda interval: interval.start)
        l = 0
        r = 1
        while r < len(intervals):
            firstInterval = intervals[l]
            secondInterval = intervals[r]
            if firstInterval.end > secondInterval.start:
                return False            
            
            l+=1
            r+=1
        return True 