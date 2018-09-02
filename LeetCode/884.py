class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import Counter
        A = Counter(A.split())
        B = Counter(B.split())
        res = []
        for k, v in A.items():
            if v==1 and not(k in B):
                res.append(k)
        for k, v in B.items():
            if v==1 and not(k in A):
                res.append(k)
        return res