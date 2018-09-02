class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        elif not(A):
            return False
        C = A
        for i in range(len(A)):
            if C == B:
                return True
            else:
                C = C[1:] + C[0]
        return False