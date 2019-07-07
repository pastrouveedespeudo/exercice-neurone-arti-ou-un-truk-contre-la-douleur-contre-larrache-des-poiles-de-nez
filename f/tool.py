# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 00:30:05 2019

@author: jeanbaptiste
"""

import numpy as np
from scipy.misc import derivative 
import sympy as sp



a = [[-1.8659518,  -0.79794514],
     [-1.71525189, -1.73753255],
     [-1.7235007,  -2.7332716 ],
     [-1.16399528, -0.45664089],
     [-1.24119434, -1.11509119],
     [ 1.12271848,  1.13221278],
     [ 0.55912398,  3.23225307],
     [ 1.74582013,  3.39984394],
     [ 1.21808832,  1.56249102],
     [ 2.09542509,  2.92145007]]

b = [0.0607502,  0.21112476]

c = 0


def function(a, b, c):
    #pre activation
    liste = []

    c = 0
    for i in a:

        un = i[0] * b[0]
        deux = i[1] * b[1]

        z = un + deux + c
        
        liste.append(z)


    return liste




def learning_rate(a):

    rate = 0.1

    grad = 2 * a
    grad = -(grad * rate)

    return grad


def sigi(z):
    
     sig = 1 /(1 + np.exp(-z))
     return sig


def derviate(calc):
    x = sp.Symbol('x')
    out = sp.diff(calc, x)
    return out






print(derviate(2*x))


print(function(a, b, c))
print(learning_rate(30))








