class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ans, stop = 0, 0
        for t in timeSeries:
            ans += duration - max(stop - t, 0)
            stop = t + duration
        return ans