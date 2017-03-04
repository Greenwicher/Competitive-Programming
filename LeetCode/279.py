__author__ = 'liuweizhi'

# Version 1, DP, O(n^1.5)
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1e100] * (n+1)
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        for s in squares:
            dp[s] = 1
        for i in range(1, n+1):
            for s in squares:
                if i-s > 0:
                    dp[i] = min(dp[i], dp[i-s]+1)
        return dp[n]


# Version 2, BFS
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = {n}
        squares = [i**2 for i in range(1, int(n**0.5)+1)][::-1]
        ans = 0
        while row:
            zero = False
            for r in row:
                if r == 0:
                    zero = True
                    break
            if zero:
                break
            _row, row = row, set()
            for r in _row:
                import bisect
                j = len(squares) - bisect.bisect(squares[::-1], r)
                print(squares[j], r)
                for s in squares[j:]:
                    if r-s >= 0:
                        row.add(r-s)
            ans += 1
        return ans