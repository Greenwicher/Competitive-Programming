class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(B) < len(A):
            if B in A:
                return 1
            elif B in A+A:
                return 2
            else:
                return -1
        else:
            if not(A in B):
                if B in A+A:
                    return 2
                else:
                    return -1
            res = 0
            for i in range(len(B)-len(A)+1):
                if B[i:i+len(A)] == A:
                    break
            head = B[:i]
            j = i
            while j+len(A) <= len(B):
                if B[j:j+len(A)] == A:
                    j += len(A)
                    res += 1
                else:
                    break
            if j < len(B):
                tail = B[j:]
            else:
                tail = ''
            if tail:
                if tail == A[:len(tail)]:
                    res += 1
                else:
                    return -1
            if head:
                if head[::-1] == A[::-1][:len(head)]:
                    res += 1
                else:
                    return -1
        return res