class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt, s0, num = [], s[0], 1
        for i in range(1, len(s)):
            if s[i] == s0:
                num += 1
            else:
                cnt.append(num)
                s0 = s[i]
                num = 1
        cnt.append(num)
        res = 0
        for i in range(len(cnt)-1):
            res += min(cnt[i], cnt[i+1])
        return res