# -*- coding: utf-8 -*-
"""

@author: Greenwicher
http://codeforces.com/problemset/problem/158/A

"""

[n, k] = raw_input().split(' ')
score = raw_input().split(' ')

print len([i for i in score if i<score[k-1]])





