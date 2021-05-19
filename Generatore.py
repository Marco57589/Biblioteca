# -*- coding: utf-8 -*-
"""
@author: marco
"""
import random

# Questo script legge dai file presenti nella cartella list e in base ad alcuni parametri personalizzati
# ritornano dei valori rielaborati casualmente
# esempio: il codice autore é ottenuto dalla combinazione di nome, congnome, luogo di nascita + 3 cifre casuali 
# in caso degli autori abbiano lo stesso nome
# NB: questa classe inizialmente era stata disegnata per lavorare sulla prima versione della biblioteca
# fatta interamente in json, quindi potrebbero esserci imprecisioni e funzionamenti poco efficenti.

global alfabeto
global provider
global tipoVia

alfabeto = ["a" ,"b" ,"c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i" ,"j" ,"k" ,"l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" ,"z"]
provider = ["gmail","protonmail","libero","email","ms","outlook","hotmail","mymail","neuromail","airmail","apple","hostIt","aruba"]
tipoVia = ["viale","pz.le","via","strada","piazza"]

def generaNome():    
    fileNomi = open("list/nomi.txt", "r",encoding='utf-8')        
    x = fileNomi.readlines()         
    fileNomi.close()
    indice = random.randint(0,len(x)-1)
    nome = x[indice].replace('\n','')
    return nome

def generaCognome():  
    fileCognomi = open("list/cognomi.txt", "r",encoding='utf-8')        
    x = fileCognomi.readlines()         
    fileCognomi.close()
    indice = random.randint(0,len(x)-1)
    cognome = x[indice].replace('\n','')
    return cognome   

def generaCategoria():
    fileCategoria = open("list/categorie.txt", "r",encoding='utf-8')        
    x = fileCategoria.readlines()         
    fileCategoria.close()    
    indice = random.randint(0,len(x)-1)
    categoria = x[indice].replace('\n','')
    return categoria
   
def generaEditore():
    fileEditori = open("list/editori.txt", "r",encoding='utf-8')        
    x = fileEditori.readlines()         
    fileEditori.close()
    indice = random.randint(0,len(x)-1)
    editore = x[indice].replace('\n','')
    return editore  
 
def generaTitolo():
    fileTitoli = open("list/titoli.txt", "r",encoding='utf-8')        
    x = fileTitoli.readlines()         
    fileTitoli.close()
    indice = random.randint(0,len(x)-1)
    titolo = x[indice].replace('\n','')
    return titolo     

def generaLuogo():
    fileLuogo = open("list/luoghi.txt", "r",encoding='utf-8')        
    x = fileLuogo.readlines()         
    fileLuogo.close()
    indice = random.randint(0,len(x)-1)
    luogo = x[indice].replace('\n','')
    return luogo   
   
def generaTessera():
    tessera = ""    
    for x in range(5):
        tessera += str(random.randint(0,9))            
    tessera += '-'
    for x in range(3):
        tessera += str(alfabeto[random.randint(0,len(alfabeto)-1)])    
    return tessera

def generaCodAutore(nome,cognome,ldn):
    newCodice = ""    
    for x in range(2):
        newCodice += str(nome[x])
    for x in range(2):
        newCodice += str(cognome[x])
    newCodice += "-"
    for x in range(3):
        newCodice += str(ldn[x])         
    newCodice += "-"
    for x in range(3):
        newCodice += alfabeto[random.randint(0, len(alfabeto)-1)]        
    return newCodice

def generaLingua():
    lingue = ["Italiano","Inglese","Tedesco","Spagnolo","Latino","Austriaco"]
    indice = random.randint(0,len(lingue)-1)
    return lingue[indice]

def generaData():    
    giorno = random.randint(1,31)
    mese = random.randint(1,12)
    anno = random.randint(1930,2021)
    if (mese==2):
        giorno = random.randint(1,28)
    data = str(anno)+"-"+str(mese)+"-"+str(giorno)
    return data

def generaDataNascita():    
    giorno = random.randint(1,31)
    mese = random.randint(1,12)
    anno = random.randint(1930,2013)
    if (mese==2):
        giorno = random.randint(1,28)
    data = str(anno)+"-"+str(mese)+"-"+str(giorno)
    return data

def generaNumero():    
    numero = "39"
    for x in range (10):
        numero += str(random.randint(0,9))
    return numero

def generaISBN():    
    isbn = ""    
    for x in range(3):
        isbn += str(random.randint(0,9)) 
    isbn += '-'
    
    for x in range(1):
        isbn += str(random.randint(0,9))        
    isbn += '-'
     
    for i in range(4): 
        isbn += str(random.randint(0,9))
    isbn += '-'
    
    for i in range(4): 
        isbn += str(random.randint(0,9))
    isbn += '-'
    
    for i in range(1): 
        isbn += str(random.randint(0,9))
    return isbn    

def generaIndirizzo():
    newIndirizzo = ""
    newIndirizzo += tipoVia[random.randint(0, len(tipoVia)-1)] +" "
    
    fileVie = open("list/vie.txt", "r",encoding='utf-8')        
    x = fileVie.readlines()         
    fileVie.close()
    indice = random.randint(0,len(x)-1)

    newIndirizzo += x[indice].replace('\n','')
    newIndirizzo += " "
    newIndirizzo += str(random.randint(0, 60)) #numero civico
    return newIndirizzo
    
def generaEmail(nome,cognome):
    newEmail = ""    
    for x in range(random.randint(1, len(nome)-1)):
        newEmail += str(nome[x])
    for x in range(random.randint(1, len(cognome)-1)):
        newEmail += str(cognome[x])
    newEmail += "@"
    newEmail += provider[random.randint(0, len(provider)-1)]
    newEmail += ".com"
    return newEmail