# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:18:26 2021

@author: davide notaro
"""

from random import random

def punto_random():
    out = [0,0]
    out[0] = random() - 0.5
    out[1] = random() - 0.5
    return out

def distanza(input):
    x=input[0]
    y=input[1]
    return (x**2 + y**2)**(1/2)


punto = list()


DENTRO = 0
TUTTI = 0

iterazioni = 100000


for i in range(iterazioni):
    punto = punto_random()
    if distanza(punto) < 0.5:
        DENTRO += 1
    TUTTI += 1
    
pi = 4 * DENTRO/TUTTI

print(pi)
