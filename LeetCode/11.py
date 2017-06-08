# Version 1, O(n^2) time complexity, O(1) space complexity
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans, n = 0, len(height)
        for i in range(n-1):
            for j in range(i+1, n):
                ans = max((j - i) * min(height[i], height[j]), ans)
        return ans

# Version 2, O(n^2) time complexity, O(1) space complexity
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        ans, i, j = 0, 0, n - 1
        while i < n - 1:
            while j > i:
                ans = max(ans, (j - i) * min(height[i], height[j]))
                if height[j] >= height[i]:
                    break
                j -= 1
            j = i + 1
            while j < n - 1 and height[j] <= height[i]:
                j += 1
            i, j = j, n - 1
        return ans

# Version 3, O(n) time complexity, O(1) space complexity
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        ans, i, j = 0, 0, n - 1
        while i < j:
            ans = max(ans, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans