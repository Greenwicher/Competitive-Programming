# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 16:48:37 2015

@author: liuweizhi
"""

## version 1
x=raw_input()
ans=''.join(str(min(int(i),9-int(i))) for i in x)
print [ans.lstrip('0'),'9'+ans[1:]][x[0]=='9']