#Version 1, Implementation with caching, O(n) time complexity, O(n) space complexity
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        ans, n = 0, len(nums)
        visited = defaultdict(int)
        for i in range(n):
            if visited[i]:
                continue
            s = []
            while not s or nums[s[-1]] != s[0]:
                if s:
                    s.append(nums[s[-1]])
                else:
                    s.append(nums[i])
                visited[s[-1]] = 1
            ans = max(ans, len(s))
        return ans


#Version 2, Implementation with caching, O(n) time complexity, O(1) space complexity
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, n, flag = 0, len(nums), False
        for i in range(n):
            if nums[i] < 0 or (nums[i] == 0 and flag):
                continue
            s = []
            while not s or abs(nums[s[-1]]) != s[0]:
                if s:
                    j = s[-1]
                    s.append(nums[s[-1]])
                else:
                    j = i
                    s.append(nums[i])
                nums[j] *= -1
                if nums[j] == 0:
                    flag = True
            ans = max(ans, len(s))
        return ans


