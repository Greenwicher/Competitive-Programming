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
import numpy as np
def F(ln,un,lm,um,lk,uk):
    for n in range(ln,un+1):
        for m in range(lm,um+1):
            for k in range(lk,uk+1):
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
    return 
#Read input data
I = lambda: list(map(int,input().split()))
T = lambda k,t: min(t,k-t)
f = [[[np.inf for k in range(51)] for j in range(31)] for i in range(31)]
N1,M1,N2,M2,K = [-np.inf for i in range(5)]
for _ in range(I()[0]):
    n,m,k = I()
    n,m,k = min(n,m),max(n,m),T(n*m,k)
    query.append((n,m,k))
    if 
    
#Solve largest rectangular problem

#Output data
for q in query:
    n,m,k = q
    print(f[n][m][k])
    
