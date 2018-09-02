class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        pos = [i for i, d in enumerate(bin(N)) if d == '1']
        if len(pos) < 2:
            return 0
        else:
            return max([pos[i+1]-pos[i] for i in range(len(pos)-1)])