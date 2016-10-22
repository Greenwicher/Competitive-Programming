# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 19:01:43 2016

@author: liuweizhi
"""

#%% Version 1
I = lambda: list(map(int, input().split()))
n,m = I()
a,b = I(), {}
# initialize the number of song for the first m bands
for band in range(1,m+1):
    b[band] = 0
# calculate the number of song for each band in current playlist
for band in a:
    b[band] = b.get(band, 1) + 1
# the maximum possible value of the minimum among b
maximum = n // m
# the minimum number of changes in the playlist a Polycarp needs to make
minimum = sum([max(0, maximum-b[i]) for i in range(1,m+1)])
# find the band c that needs more songs
c = [band for band in range(1,m+1) if b[band]<maximum]
# find the replaced playlist d
d = []
for band in a:
    # can be replaced
    if (b[band]>maximum or band>m) and c:
        d.append(c[0])
        b[band] -= 1
        b[c[0]] += 1
        if b[c[0]] == maximum:
            c.pop(0)
    else:
        d.append(band)
print(maximum, minimum)
print(' '.join(map(str, d)))
