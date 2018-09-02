class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in [0, 1, 2]:
            return 0
        isprime = [1] * n
        for i in range(2, n):
            if isprime[i]:
                j = 2
                while j*i < n:
                    isprime[j*i] = 0
                    j += 1
        return sum(isprime) - 2


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        isprime = [1] * n
        for i in range(2, int(n**0.5)+1):
            if isprime[i]:
                j = i
                while j*i < n:
                    isprime[j*i] = 0
                    j += 1
        return sum(isprime) - 2



class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)