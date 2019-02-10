#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:58:56 2019

@author: karan
"""
subjects = ["Americans", "Indians"]
verbs = ["play","watch"]
objects = ["Baseball","Cricket"]
for i in subjects:
    for j in verbs:
        for k in objects:
            print("{} {} {}".format(i,j,k))

