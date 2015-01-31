# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 21:12:46 2015

@author: liuweizhi
"""

## version 1
n,k,l,c,d,p,nl,np=map(int,raw_input().split())
print min(k*l/(n*nl),c*d/n,p/(n*np))

## version 2
n,k,l,c,d,p,N,P=map(int,raw_input().split());print min(k*l/N,p/P,c*d)/n