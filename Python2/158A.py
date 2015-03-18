# -*- coding: utf-8 -*-
"""

@author: Greenwicher
http://codeforces.com/problemset/problem/158/A

"""

# version 1
n,k = map(int, raw_input().split())
score = map(int, raw_input().split())
print len(filter(lambda x:x>0 and x>=score[k-1], score))




