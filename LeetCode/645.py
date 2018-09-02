class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(sums)
        _sum = sum(nums)
        square_sum = [foo**2 for foo in nums]
        a = _sum - (1 + n) * n // 2
        b = square_sum - n * (n + 1) * (2 * n + 1) // 6
        c = b // a
        x = (a + c) // 2
        y = x - a
        return [x, y]