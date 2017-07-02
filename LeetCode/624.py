# Version 1, Greedy, O(N) time complexity, O(N) space complexity
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        list_min, list_max = [], []
        index_min, index_max = 0, 0
        cur_min, cur_max = 1e100, -1e100
        for i, array in enumerate(arrays):
            list_min.append(min(array))
            list_max.append(max(array))
            if list_min[-1] < cur_min:
                cur_min = list_min[-1]
                index_min = i
            if list_max[-1] > cur_max:
                cur_max = list_max[-1]
                index_max = i
        if index_min != index_max:
            return cur_max-cur_min
        else:
            ans = -1e100
            sec_min, sec_max = 1e100, -1e100
            for i in range(len(arrays)):
                if i != index_min:
                    sec_min = min(sec_min, list_min[i])
                if i != index_max:
                    sec_max = max(sec_max, list_max[i])
            return max(cur_max-sec_min,sec_max-cur_min)