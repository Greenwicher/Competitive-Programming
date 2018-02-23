class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        for i in range(L, R+1):
            bits = bin(i)[2:].count("1")
            if bits == 2:
                res += 1
            elif bits > 2:
                flag = True
                for j in range(2, int(bits**0.5)+1):
                    if bits % j == 0:
                        flag = False
                        break
                if flag:
                    res += 1
        return res