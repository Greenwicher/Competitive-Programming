# Version 1
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = len(s)
        res = ''
        for i in range(-(-l//(2*k))):
            a = i*2*k
            b = min(a+k, l)
            c = min((i+1)*2*k, l)
            res += s[a:b][::-1] + s[b:c]
        return res