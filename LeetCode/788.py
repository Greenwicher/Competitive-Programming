class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        rotate = {'0':'0', '1':'1', '2':'5', '5':'2', '6':'9', '8':'8', '9':'6'}
        for i in range(1, N+1):
            stri, strj = str(i), ''
            if not(set(stri) & set(str(347))):
                for s in stri:
                    strj += rotate[s]
                if stri != strj:
                    res += 1
        return res