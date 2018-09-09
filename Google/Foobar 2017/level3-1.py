__author__ = 'liuweizhi'

# def answer(start, length):
#     # your code here
#     ans = 0
#     for i in range(length):
#         for j in range(length-i):
#             ans ^= start + j + i * length
#         print(ans)
#     return ans


def answer(start, length):
    # your code here
    ans = 0
    for i in range(length):
        size = length - i
        s, e = start + i * length, start + length - i - 1 + i * length
        if size == 1:
            ans ^= s
        else:
            if s % 2 == 0 and e % 2 == 1:
                ans ^= [0, 1][size//2 % 2]
            if s % 2 == 0 and e % 2 == 0:
                ans ^= [e, 1 ^ e][(size-1)//2 % 2]
            if s % 2 == 1 and e % 2 == 1:
                ans ^= [s, s ^ 1][(size-1)//2 % 2]
            if s % 2 == 1 and e % 2 == 0:
                ans ^= [s ^ e, s ^ 1 ^ e][(size-2)//2 % 2]
    return ans


print(answer(0,3),2)
print(answer(17,4),14)
print(answer(0,int(1e3)),"NA")