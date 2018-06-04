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

        watch out for the boundary condition
        draw pictures of how overlaps looks like:
        1 s      e     s       e        s     e
          |------|     |-------|        |-----|
          |---|     |-------|        |--|
        2 s   e     s       e        s  e
        overlap:
        e2 > s1 >= s2
        non-overlap:
        e2 >= s1 >=s2

        bruteforce, time limit exceed
        """
        for idx1, interval1 in enumerate(intervals[:-1]):
            for idx2, interval2 in enumerate(intervals[1:]):
                if interval1.start <= interval2.start < interval1.end:
                    return False
                if interval2.start <= interval1.start < interval2.end:
                    return False
        return True

        # return all(not(interval1.start <= interval2.start < interval1.end or
        #                interval2.start <= interval1.start < interval2.end)
        #            for idx, interval1 in enumerate(intervals[:-1])
        #            for interval2 in intervals[idx+1:])