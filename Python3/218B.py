# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:43:52 2015

@author: liuweizhi
"""

# version 1
I=lambda:list(map(int,input().split()))
n,m=I();a=sorted(I());b=[]
for i in a:b+=list(range(1,i+1))
b=sorted(b)
i=mini=p=0
while((i<m)and(p+a[i]<=n)):
    p+=a[i]
    mini+=(1+a[i])*a[i]//2
    i+=1
if p<n: mini+=(2*a[i]-n+p+1)*(n-p)//2
print(sum(b[-n:]),mini)



  

