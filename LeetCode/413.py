# Version 1, Simulation
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def num(n):
            res = n*(n+1) // 2 - (2*n-1)
            return res
        if len(A) < 3: return 0
        len_arithmetic = []
        current_arithmetic = A[:2]
        for i in range(2, len(A)):
            if 2*current_arithmetic[-1] == current_arithmetic[-2] + A[i]:
                current_arithmetic.append(A[i])
            else:
                if len(current_arithmetic) >= 3:
                    len_arithmetic.append(len(current_arithmetic))
                current_arithmetic = A[i-1:i+1]
        if len(current_arithmetic) >= 3:
            len_arithmetic.append(len(current_arithmetic))
        res = sum([num(n) for n in len_arithmetic]+[0])
        return res

# Version 2, Dynamic Progamming
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        curr, sum = 0, 0
        for i in range(2,len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                curr += 1
                sum += curr
            else:
                curr = 0
        return sum