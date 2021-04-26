# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:53:12 2021

@author: davide notaro
"""

#roulette programma

from random import randint

continua = True
wallet = 1000.00    #conto iniziale
puntata = int()
scommessa = float()

print("saldo iniziale di " + str(wallet) + "€")

while continua is True:  #ciclo del gioco
    print("\nquanto vuoi puntare: ")
    
    while type(puntata) is not float: #ciclo dell'inserimento della puntata
        try:
            puntata = float(input())
            if puntata > wallet:
                puntata = int()
                raise Exception('Portafoglio troppo vuoto')
            break
        except:
            print("\ninserire un importo valido")
            
    wallet = wallet - puntata
            
    print("\nche numero vuoi puntare? ")
    while type(scommessa) is not int: #ciclo dell'inserimento del numero da puntare
        
        try:
            puntata = int(input())
            if puntata > 36:
                puntata = float()
                raise Exception('Non nella ruota')
            break
        except:
            print("\ninserire una puntata corretta")
   
    estratto = randint(0,36) #estrazione randomica
    
    print('\nil numero estratto è  ' + str(estratto))
    
    if estratto == scommessa:
        print("\nhai vinto!")
        wallet = wallet + puntata*36
    else:
        print("\nhai perso!")
        
    puntata = int()   #reset delle variabili per il prossimo ciclo 
    scommessa = float()
            
    
    if wallet == 0: #game over
       print("\nmi spiace ma non hai più soldi sul conto, non è più possibile effettuare scommesse")
       break
    
    
    risposta = str()
    print("\nvuoi continuare? il tuo saldo è di " + str(wallet) + "€")
    
    while risposta != 'si' and risposta != 'no': #ciclo dell'inserimento del "continua?"
        
        risposta = str(input())
        
        if risposta !='si' and risposta != 'no':
            print('\ninserire risposta corretta')
        else:
            break
        
        
    if risposta == 'si':
        continua = True
    elif risposta == 'no':
        continua = False        
             

   
    