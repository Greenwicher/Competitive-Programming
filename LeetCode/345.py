class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = [foo for foo in s]
        ix, vowel = [], []
        for i, foo in enumerate(s):
            if foo.lower() in "aeiou":
                ix.append(i)
                vowel.append(foo)
        for i in range(len(vowel)):
            s[ix[i]] = vowel[-(i+1)]
        return ''.join(s)


s = Solution()
s.reverseVowels("hEllo")