#%% Version 1
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        def check(houses, heaters, m):
            for house in houses:
                flag = False
                for heater in heaters:
                    if heater-m<=house<=heater+m:
                        flag = True
                        break
                if not flag:
                    return False
            return True

        houses, heaters = map(sorted, [houses, heaters])
        l, r = 0, max(max(houses), max(heaters))
        while l != r:
            m = (l + r) // 2
            if check(houses, heaters, m):
                r = m
            else:
                l = m + 1
        return l

#%% Version 2