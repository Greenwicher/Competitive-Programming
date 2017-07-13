# Version 1
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        flag = [w.isupper() for w in word]
        return all(flag) or not(any(flag)) or (flag[0] and not(any(flag[1:])))