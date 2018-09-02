class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a, b = sum(A), sum(B)
        c = (a+b) // 2
        dict_B = {}
        for foo in B:
            try:
                dict_B[foo] += 1
            except:
                dict_B[foo] = 1
        for foo in A:
            if c-a+foo in dict_B:
                return [foo, c-a+foo]