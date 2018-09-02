class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bit = bin(n)[2:]
        bit = '0' * (32 - len(bit)) + bit
        return int(bit[::-1], 2)


s = Solution()
s.reverseBits(0)