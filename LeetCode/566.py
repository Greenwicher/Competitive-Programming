class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        _r, _c = len(nums), len(nums[0])
        if r * c == _r * _c:
            ans = [[0] * c for _ in range(r)]
            for i in range(_r):
                for j in range(_c):
                    id = j + _c * i
                    ans[id // c][id % c] = nums[i][j]
            return ans
        else:
            return nums