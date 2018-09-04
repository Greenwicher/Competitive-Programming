class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        if len(str) != len(pattern):
            return False
        map = {}
        for p, s in zip(pattern, str):
            if (p in map) and (map[p] != s):
                return False
            elif not(p in map):
                map[p] = s
        str = [v for k, v in map.items()]
        if len(str) == len(set(str)):
            return True
        else:
            return False