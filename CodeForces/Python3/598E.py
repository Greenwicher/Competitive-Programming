# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:59:35 2016

@author: liuweizhi
"""

#%% Version 1 !!!Canot output solutions only after read all input 
import numpy as np
#Read input data
I = lambda: list(map(int,input().split()))
T = lambda k,t: min(t,k-t)
query = []
N,M,K = [-np.inf for i in range(3)]
for _ in range(I()[0]):
    n,m,k = I()
    n,m,k = min(n,m),max(n,m),T(n*m,k)
    query.append((n,m,k))
    N,M,K = list(map(lambda x: max(x[0],x[1]), list(zip([n,m,k],[N,M,K]))))
    
#Solve largest rectangular problem
f = [[[np.inf for k in range(K+1)] for j in range(M+1)] for i in range(N+1)]
for n in range(1,N+1):
    for m in range(n,M+1):
        for k in range(K+1):
            if k:
                #horizontally cut
                minH = np.inf
                for i in range(1,n):
                    for t in range(min(i*m//2,(n-i)*m//2,k)+1):
                        minH = min(minH,f[i][m][T(i*m,t)]+f[n-i][m][T((n-i)*m,k-t)]+m**2)
                #vertically cut      
                minV = np.inf
                for j in range(n,m-n+1):
                    for t in range(min(n*j//2,n*(m-j)//2,k)+1):
                        minV = min(minV,f[n][j][T(n*j,t)]+f[n][m-j][T(n*(m-j),k-t)]+n**2)
                f[n][m][k] = min(minH,minV)
            else:
                #no cut 
                f[n][m][k] = 0
#Output data
for q in query:
    n,m,k = q
    print(f[n][m][k])
    
#%% Version 2
I = lambda: list(map(int, input().split()))
f = [[[0 for k in range(51)] for m in range(31)] for n in range(31)]
# dynamic programming with memoization
def dp(n,m,k):
    # invalid parameter
    if k>n*m or n<=0 or m<=0 or k<=0:
        return float('inf')
    # no need to cut
    elif n*m == k: 
        return 0 
    # cut only once
    elif n==1 or m==1:
        return 1
    # memoization
    elif f[n][m][k]:
        return f[n][m][k]
    # vertically/horizontally cut
    else:
        cost = float('inf')
        m2,n2 =  m**2, n**2
        for i in range(1,n):
            # cut ith vertical line, then consider i*m>=k and i*m<k
            cost = min(cost, dp(i,m,k)+m2, dp(n-i,m,k-m*i)+m2)
        for j in range(1,m):
            # cut jth horizontal line, then consider n*j>=k and n*j<k
            cost = min(cost, dp(n,j,k)+n2, dp(n,m-j,k-n*j)+n2)
        return cost
        
query = []
N,M,K = [-float('inf') for i in range(3)]
for _ in range(I()[0]):
    n,m,k = I()
    query.append((n,m,k))
    N,M,K = list(map(lambda x: max(x[0],x[1]), list(zip([n,m,k],[N,M,K]))))
        
# pre-processing      
for n in range(N+1):
    for m in range(M+1):
        for k in range(K+1):
            f[n][m][k] = dp(n,m,k)
# output          
for q in query:
    n,m,k = q
    print(f[n][m][k])
    
    
