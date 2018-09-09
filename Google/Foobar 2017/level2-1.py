__author__ = 'liuweizhi'

def answer(l, t):
    # your code here
    l = [0] + l
    size = len(l)
    for i in range(1, size):
        l[i] += l[i-1]
    for i in range(size):
        for j in range(i+1, size):
            if l[j] - l[i] == t:
                return [i, j-1]
            elif l[j] - l[i] > t:
                break
    return [-1,-1]

assert answer([4, 3, 10, 2, 8], 12) == [2,3], "Error"
assert answer([1, 2, 3, 4], 15) == [-1,-1], "Error"
print(answer([1,2,3,4,5,6,7], 28))