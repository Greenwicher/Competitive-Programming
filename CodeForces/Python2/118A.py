# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 12:51:35 2015

@author: liuweizhi
"""

# version 1
word = raw_input().lower()
for vowel in ['a', 'o', 'y', 'e', 'u', 'i']:
    word = word.replace(vowel, '')
print '.'+'.'.join(word)

# version 2
print '.'+'.'.join(raw_input().lower().translate(None,"aeiouy"))