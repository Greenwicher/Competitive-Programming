class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        cnt1 = sum([A[i]>=A[i+1] for i in range(len(A)-1)])
        cnt2 = sum([A[i]<=A[i+1] for i in range(len(A)-1)])
        if (cnt1==len(A)-1) or (cnt2==len(A)-1):
            return True
        else:
            return False