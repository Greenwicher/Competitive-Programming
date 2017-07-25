# Version 1
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        for k in c1:
            if not(k in c2 and c2[k] >= c1[k]):
                return False
        return True