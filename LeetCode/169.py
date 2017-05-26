class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        counter = collections.defaultdict(int)
        ans, counts = 0, 0
        for foo in nums:
            counter[foo] += 1
            if counter[foo] > counts:
                counts = counter[foo]
                ans = foo
        return ans

# Version 2
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]
