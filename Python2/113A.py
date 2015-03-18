# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 18:21:03 2015

@author: liuweizhi
"""

## version 1
word = raw_input()
print [word, ''.join(map(lambda x:[x.lower(), x.upper()][x.islower()], word))][word[1:].isupper() or len(word)==1]