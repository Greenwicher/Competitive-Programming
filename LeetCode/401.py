# Version 1
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        import itertools
        hour = [1, 2, 4, 8]
        minute = [1, 2, 4, 8, 16, 32]
        res = []
        if num > 10:
            return []
        else:
            for i in range(min(num+1, 5)):
                _hour = [sum(list(foo)+[0]) for foo in itertools.combinations(hour, i)]
                _minute = [sum(list(foo)+[0]) for foo in itertools.combinations(minute, num-i)]
                res += [str(_h)+':'+'0'*(_m<10)+str(_m) for _h in _hour for _m in _minute if _h < 12 and _m < 60]
        return list(set(res))