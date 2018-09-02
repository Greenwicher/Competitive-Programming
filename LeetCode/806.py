class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        res = [0]
        for s in S:
            width = widths[ord(s)-ord('a')]
            if res[-1] + width <= 100:
                res[-1] += width
            else:
                res.append(width)
        return [len(res), res[-1]]