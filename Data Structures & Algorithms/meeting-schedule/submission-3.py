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

        intervals.sort(key = lambda x:x.start)
        current = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i].start < current.end:
                return False
            current = intervals[i]
            
        return True