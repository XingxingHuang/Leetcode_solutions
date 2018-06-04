# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda interval: interval.start)
        rooms = [intervals[0].end]
        max_room_num = len(rooms)
        for interval in intervals[1:]:
            rooms = [end for end in rooms if end > interval.start] + [interval.end]
            max_room_num = max(len(rooms), max_room_num)
        return max_room_num
