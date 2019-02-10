#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:14:19 2019

@author: karan
"""
def nd(n):
    try:
        res = n/0
        print(res)
    except:
        print("Division by 0 is not defined")
nd(5)
    
