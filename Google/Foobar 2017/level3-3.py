__author__ = 'liuweizhi'

def minimum(n):
    """
    :param n: int, the minimum value of largest height given n bricks, k*(k+1)/2 >= n
    :return:
    """
    return int(-(-((1+8*n)**.5-1)//2))

def answer(n):
    # your code here
    # dp[i][j] represents the number of different staircases given i bricks and the largest height j
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[3][2] = 1
    for i in range(n+1):
        dp[i][i] = 1
    for i in range(4, n+1):
        for j in range(minimum(i), i):
            for k in range(minimum(i-j), min(j, i-j+1)):
                dp[i][j] += dp[i-j][k]
    return sum(dp[n]) - 1

print(answer(3),1)
print(answer(4),1)
print(answer(5),2)
print(answer(6),3)
print(answer(7),4)
print(answer(8),5)
print(answer(9),7)
print(answer(10),9)
print(answer(11),11)
print(answer(200),487067745)