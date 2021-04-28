# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 19:51:52 2021

@author: davide notaro
"""

#insert sorting ricorsivo molto poco elegante ma perfettamente funzionante e
#senza bug o possibilità di crash relativi ad input errati

def insertsorting(lista, new, i):
    try:
        if lista[0] > new:
            lista.insert(0, new)
        elif lista[i] <= new and lista[i+1] >= new:
            lista.insert(i+1, new)         
        else:
            lista = insertsorting(lista, new, i+1)     
    except:
        if lista == []:
            lista.append(new)
        else:
            if lista[i] > new:
                lista.insert(i, new)   
            else:
                lista.append(new)
    finally:
        return lista
            
    
nuova_lista = list()    

print("inserire i numeri: ")

while True:
    nuovo_numero = input()
    
    if nuovo_numero == "stop":
        break
    
    try:
        nuova_lista = insertsorting(nuova_lista, float(nuovo_numero), 0)
    except:
        print("\ninserire un numero valido ")
        continue
    
    print(nuova_lista)
    
    

    
        
    
    
    
    
    
    


