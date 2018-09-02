class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ix = [i for i, s in enumerate(S) if s==C]
        res = []
        for i in range(len(S)):
            # can use binary search to locate ix of the nearest character
            res.append(min([abs(i-j) for j in ix]))
        return res