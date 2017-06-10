# Version 1, Implementation, O(n * k) time complexity, O(1) space complexity, TLE
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            j = i + 1
            while j - i <= k and j < n:
                if nums[i] == nums[j]:
                    return True
                j += 1
        return False

# Version 2, Implementation, O(n) time complexity, O(n) space complexity
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        indices = {}
        for i in range(len(nums)):
            if nums[i] in indices:
                if i - indices[nums[i]][-1] <= k:
                    return True
                else:
                    indices[nums[i]].append(i)
            else:
                indices[nums[i]] = [i]
        return False

# Version 3
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<=k:
            return len(nums) >  len(set(nums))

        hashSet=set(nums[:k])
        if len(hashSet) < k:
            return True

        for i in xrange(k,len(nums)):
            hashSet.add(nums[i])
            if len(hashSet)==k:
                return True
            else:
                hashSet.remove(nums[i-k])
        return False
