# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:11:07 2015

@author: liuweizhi
"""

## version 1
''' 
The apparaent stopping criterion is that the number
of character whose number is odd is less or equal to
one. In the other case, the player should remove all
the character whose number is even such that the number
of each character will become odd finally. Then based on
the number of odd groups and previous steps, we could 
decide which player will win.
'''
a=[0]*26
for c in raw_input():
    a[ord(c)-ord('a')]+=1
n=sum([i>0 for i in a])
b=[(i>0)*(1*(i%2==1)-1*(i%2==0)) for i in a]
m=b.count(-1)
print ['Second','First'][(n-m<2) or (n+m)%2]

## version 2
''' Actually, I don't think the follownig code is right becasue 
it only concerns the number of the character whose number is odd.
But the optimal policy for each player should remove the character
whose number is even. Despite the only two stopping criterion (the 
number of character whose number is odd is less or equal to one), 
then the number of each character must reach a state when they are
all odd. Then the analysis below is adopted after this odd convergence.'''
s=raw_input()
p=sum(s.count(x)%2 for x in set(s))
print'First'if p&1 or p==0 else'Second'

## version 3
''' 
Use dictionary to store the status of odd for 
each character.
'''
c={}
for x in raw_input():c[x]=c.get(x,0)^1
k=sum(c.values())
print ('Second','First')[k<1 or k&1]