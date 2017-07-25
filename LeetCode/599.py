# Version 1, Implementation
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        index = defaultdict(list)
        for i, v in enumerate(list1):
            index[v].append(i)
        for i, v in enumerate(list2):
            index[v].append(i)
        res, min_sum = [], 1e100
        for k, v in index.items():
            if len(v) > 1:
                if sum(v) < min_sum:
                    res = [k]
                    min_sum = sum(v)
                elif sum(v) == min_sum:
                    res.append(k)
        return res
