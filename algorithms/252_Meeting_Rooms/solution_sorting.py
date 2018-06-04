# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        after soring the meetings by the starting time
        each meetings start time should be later than previous meetings end time
        """
        intervals.sort(key=lambda interval: interval.start)
        return all(intervals[i].start >= intervals[i - 1].end for i in range(1, len(intervals)))
