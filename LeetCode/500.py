# Version 1, Implementation
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [word for word in words if any([set(word.lower()).issubset(set(r)) for r in ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']])]