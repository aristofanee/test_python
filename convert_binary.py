# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 19:28:01 2021

@author: davide notaro
"""



def inverti_lista(x = list()): #inverte la lista
    
    out = list()
    i = 0
    
    for i in range(len(x)):
        out.append(x[len(x)-i-1])
        
    return out

def list_to_string(x=list()): #converte la lista in una stringa
    
    out = ""
    
    for elem in x:
        out = out + str(elem)
        
    return out



        
n = float #numero da inserire

print("inseriisci un numero: ")

while type(n) is not int: #ciclo dell'inserimento
    try:
        n = int(input())
        break
    except:
        print("\ninserire un intero")

bin = list()

b = int()

while n != 0: #trasformazione in binario
    b = n//2
    if b*2 != n:
        bin.append(1)
    else:
        bin.append(0)
    n = b


bin = inverti_lista(bin)


print("\n" + list_to_string(bin))
