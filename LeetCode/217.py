class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        import collections
        counter = collections.defaultdict(int)
        for foo in nums:
            counter[foo] += 1
            if counter[foo] > 1:
                return True
        return False


# version 2
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)