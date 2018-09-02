class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = "".join(S.upper().split("-"))
        m, n = len(S) // K, len(S) % K
        if n:
            res = [S[:n]]
        else:
            res = []
        for i in range(m):
            res.append(S[n+K*i:n+K*(i+1)])
        return "-".join(res)