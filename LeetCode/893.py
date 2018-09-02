class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def sort(s):
            ord = sorted(s[::2])
            even = sorted(s[1::2])
            res = ''
            for i in range(len(s)):
                if i % 2:
                    res += even[i//2]
                else:
                    res += ord[i//2]
            return res
        from collections import Counter
        for i in range(len(A)):
            A[i] = sort(A[i])
        cnt = Counter(A)
        return len(cnt)

s = Solution()
s.numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"])