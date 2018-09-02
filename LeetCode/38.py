class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for _ in range(n-1):
            ix = [-1]+[i for i in range(len(res)-1) if res[i] != res[i+1]]
            seg = [res[ix[i]+1:ix[i+1]+1] for i in range(len(ix)-1)] + [res[ix[-1]+1:]]
            res = ''.join([str(len(foo)) + foo[0] for foo in seg])
        return res