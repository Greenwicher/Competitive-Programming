__author__ = 'liuweizhi'

def answer(s):
    # your code here
    size = len(s)
    left = [0] * size
    # left[i] represents the number of '<' after s[i] (excluded)
    for i in range(size-1)[::-1]:
        left[i] += left[i+1] + 1 * (s[i+1] == '<')
    ans = 0
    for i in range(size):
        if s[i] == '>':
            ans += left[i]
    return 2 * ans

assert answer(">----<") == 2, "Error"
assert answer("<<>><") == 4, "Error"
assert answer("--->-><-><-->-") == 10, "Error"
print(answer(">>><<<"))