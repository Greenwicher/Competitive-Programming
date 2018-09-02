class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        from collections import Counter
        count = Counter(letters)
        for i in range(1, 27):
            ascii = (ord(target) - 97 + i) % 26 + 97
            if chr(ascii) in count:
                return chr(ascii)