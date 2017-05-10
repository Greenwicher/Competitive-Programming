class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max([len(foo) for foo in ''.join(list(map(str, nums))).split('0')])