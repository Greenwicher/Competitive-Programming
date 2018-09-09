class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            if len(set(A)) == len(A):
                return False
            else:
                return True
        else:
            ix = []
            for i in range(len(A)):
                if A[i] != B[i]:
                    ix.append(i)
            if len(ix) != 2:
                return False
            else:
                i, j = ix
                if A[i] == B[j] and A[j] == B[i]:
                    return True
                else:
                    return False