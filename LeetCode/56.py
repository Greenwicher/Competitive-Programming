# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# Version 1, Sorting, O(nlogn) time complexity, O(n) space complexity
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        intervals = sorted(intervals, key=lambda x: x.start)
        ans = [intervals[0]]
        for foo in intervals[1:]:
            if foo.start <= ans[-1].end:
                ans[-1].end = max(ans[-1].end, foo.end)
            else:
                ans.append(foo)
        return ans
