class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] <= nums[i+1]:
                i += 1
            else:
                break
        if i == len(nums)-1:
            return True
        else:
            flag1 = True
            m = nums[i]
            j = i + 2
            while j < len(nums):
                if nums[j] >= m:
                    m = nums[j]
                    j += 1
                else:
                    flag1 = False
                    break
            flag2 = True
            if i == 0:
                m = -1e100
            else:
                m = nums[i-1]
            j = i + 1
            while j < len(nums):
                if nums[j] >= m:
                    m = nums[j]
                    j += 1
                else:
                    flag2 = False
                    break
            if flag1 or flag2:
                return True
            else:
                return False


s = Solution()
s.checkPossibility([2,3,3,2,4])