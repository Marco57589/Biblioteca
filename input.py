# -*- coding: utf-8 -*-
"""
@author: marco
"""

import re
import datetime

# in questo script abbiamo le funzione per quasi tutti i tipi di input
# gli input vengono controllati tramite regex.
def idAutoreValidation():
    regex = '([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]+-[a-zA-Z][a-zA-Z][a-zA-Z]+-[a-zA-Z][a-zA-Z][a-zA-Z])'
    while True:
        try:
            idAutore = str(input("Inserisci l'id autore (Formato: abcd-abc-abc) > ")) 
            if(re.search(regex, idAutore)):               
                break   
        except ValueError:
            print("\n[ERRORE] inserimento")
    return idAutore
    

def tesseraUtenteValidation():
    regex = '([0-9][0-9][0-9][0-9][0-9]+-[a-zA-Z][a-zA-Z][a-zA-Z])'
    while True:
        try:
            tessera = str(input("Inserisci la tessera utente (Formato: 12345-abc) > ")) 
            if(re.search(regex, tessera)):               
                break   
        except ValueError:
            print("\n[ERRORE] inserimento")
    return tessera

def phoneValidation():
    regex = '([0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9])'
    while True:
        try:
            telefono = str(input("Inserisci il numero di telefono (Formato: 123456789123 (12)) > ")) 
            if(re.search(regex, telefono)):               
                break   
        except ValueError:
            print("\n[ERRORE] inserimento")
    return telefono
    
    
def isbnValidation(x):
    regex = '([0-9][0-9][0-9]+-[0-9]+-[0-9][0-9][0-9][0-9]+-[0-9][0-9][0-9][0-9]+-[0-9])'
    while True:
        try:
            isbn = str(input("Inserisci "+str(x)+" (Formato: xyz-x-xyzx-xyzx-x) > ")) 
            if(re.search(regex, isbn)):               
                break   
        except ValueError:
            print("\n[ERRORE] inserimento")
    return isbn

def dateValidation(x):
    while True:
        try:
            data = str(input("Inserisci "+str(x)+" (Formato: giorno-mese-anno) > ")) 
            data = datetime.datetime.strptime(data, "%d-%m-%Y").date()                   
            break        
        except ValueError:
            print("\n[ERRORE] inserimento")
    return data

def intValidation(x):
    regex = '^[0-9]+$'
    while True:
        try:
            ins = str(input("Inserisci "+str(x)+"> "))
            if(re.search(regex, ins)):               
                break        
        except ValueError:
            print("\n[ERRORE] inserimento") 
    return ins

def yearValidation(x):
    regex = '^[0-2][0-9][0-9][0-9]+$'
    while True:
        try:
            ins = str(input("Inserisci "+str(x)+"> "))
            if(re.search(regex, ins)):               
                break        
        except ValueError:
            print("\n[ERRORE] inserimento")
    return ins

def stringValidation(x):
    regex = '(^[a-zA-Z]+$)'
    while True:
        try:
            ins = str(input("Inserisci "+str(x)+"> "))
            if(len(ins) > 2):
                if(re.search(regex, ins)):               
                    break        
        except ValueError:
            print("\n[ERRORE] inserimento")  
    return ins
            
def emailValidation():
    regex = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
    while True:
        try:
            email = str(input("Inserisci la mail > "))
            if(re.search(regex, email)):               
                break        
        except ValueError:
            print("\n[ERRORE] inserimento")
    return email            
