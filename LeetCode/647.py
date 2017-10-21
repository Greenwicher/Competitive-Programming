# Version 1, Dynamic Programming
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_palindromic(s):
            return s == s[::-1]
        if not s: return 0
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            dp[i] = dp[i-1] + sum([is_palindromic(s[j:i+1]) for j in range(i)]) + 1
        return dp[-1]

# Version 2, Simulation, Constant Optimization (Good Insight)
class Solution(object):
    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        for center in xrange(2*N - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

# Version 3, Manacher's Algorithm
class Solution(object):
    def countSubstrings(self, S):
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in xrange(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z

        return sum((v+1)/2 for v in manachers(S))