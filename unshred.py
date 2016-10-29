#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:46:30 2016

@author: root
"""
import numpy as np
import scipy
from scipy import misc
from random import shuffle
from os import listdir
import matplotlib.pyplot as plt


"""
computes the difference between the edges of two pictures
'r' compares image1's right edge with image2's left edge
'l' does the opposite
"""


def sim(image1, image2, d):
    if d == 'r':
        c1 = -1
        c2 = 0
    elif d == 'l':
        c1 = 0
        c2 = -1
    else:
        return 'Error'
    difference = 0
    for i in range(len(image1)):
        difference = abs(int(image1[i][c1][0]) + int(image1[i][c1][1]) + int(image1[i][c1][2]) - \
            (int(image2[i][c2][0]) + int(image2[i][c2][1]) + int(image2[i][c2][2])))
    return abs(difference)


def costfunction(strips):
    errors = [sim(strips[i], strips[i + 1], 'r') for i in range(len(strips) - 1)]
    return errors

def merge(strips):
    merged=[]
    for c in range(strips[0].shape[0]):
        mergedline=[]
        for image in strips:
            for pixel in image[c]:
                mergedline.append(pixel)
        merged.append(mergedline)
    print(len(merged),len(merged[0]),len(merged[0][0]))
    return merged

def permute(strips,i,j):
    a=strips[i]
    strips[i]=strips[j]
    strips[j]=a
    return strips


"""
loading strips from examples folder into an array
"""
files=listdir('./examples')
files.sort()
strips = [misc.imread('./examples/' + f) for f in files]
"""errors = costfunction(strips)
print(errors)
print(sum(errors))
merged=merge(strips)
plt.imshow(merged)
plt.show()


for i in range(len(strips)-1):
    m=sim(strips[i],strips[i+1],'r')
    for j in range(i+1,len(strips)):
        if sim(strips[i],strips[j],'r') <=m-10:
            strips=permute(strips,i+1,j)


errors = costfunction(strips)
print(errors)
print(sum(errors))
merged=merge(strips)
plt.imshow(merged)
plt.show()"""
import itertools
errors = costfunction(strips)
m=sum(errors)
for f in itertools.permutations(strips):
    errors = costfunction(f)
    m=min(m,sum(errors))
    print(str(sum(errors))
        +'/min='+str(m))


