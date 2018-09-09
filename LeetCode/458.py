class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        import math
        return int(-(-math.log(buckets) // math.log(minutesToTest//minutesToDie+1)))