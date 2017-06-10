# Version 1, Meet in the middle, O(n) time complexity, O(n) space complexity
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = {}
        for i in range(len(nums)):
            if nums[i] in indices:
                indices[nums[i]].append(i)
            else:
                indices[nums[i]] = [i]
        for i in range(len(nums)):
            if target - nums[i] in indices:
                if 2 * nums[i] == target:
                    if len(indices[nums[i]]) > 1:
                        return indices[nums[i]]
                else:
                    return [i] + indices[target-nums[i]]

# Version 2, Meet in the middle, O(n) time complexity, O(n) space complexity
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
