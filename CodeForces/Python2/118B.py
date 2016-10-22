# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 15:07:04 2015

@author: liuweizhi
"""

## version 1
n=input();seq=[]
for i in range(n+1):
    seq.append(' '*2*(n-i)+' '.join(map(str,range(i+1))))
for i in range(n+1):
    print seq[i]+seq[i][-2::-1][:2*i]
for i in range(n)[::-1]:
    print seq[i]+seq[i][-2::-1][:2*i]
    
## version 2
n=input()
seq=[]
for i in range(2*n+1):
    seq1=' '*2*(n-i)+' '.join(map(str,range(i+1)))
    seq1=seq1+seq1[-2::-1][:2*i]
    seq2=' '*2*(i-n)+' '.join(map(str,range(2*n-i+1)))
    seq2=seq2+seq2[-2::-1][:2*(2*n-i)]
    seq.append(seq2)
    print [seq1,seq2][i>n]