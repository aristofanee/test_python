# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:10:49 2021

@author: davide notaro
"""

#bubble sort ricorsivo di una lista di float
#manca l'inserimento della lista



def riempi_lista(x):
    return [3, 1, 5.4, 4, 10, 3, 5]

    


def bubble_sort(x, i):
    sost = float()
    
    if i == len(x) - 1:
        return x
   
    if x[i] <= x[i+1]:
        x = bubble_sort(x,i+1)
    else:
        sost = x[i]
        x[i] = x[i+1]
        x[i+1] = sost
        x = bubble_sort(x, 0)
    
    return x
            
        

lista = list()
lista = riempi_lista(lista)
print(lista)


lista = bubble_sort(lista, 0)
print(lista)
