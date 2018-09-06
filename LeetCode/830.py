class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []
        i, j = 0, 0
        for j in range(len(S)-1):
            if S[j] != S[j+1]:
                if j - i + 1 >= 3:
                    res.append([i, j])
                i = j + 1
        if (j == len(S) - 2) and (S[j] == S[j+1]) and (j - i + 2 >= 3):
            res.append([i, j+1])
        return res