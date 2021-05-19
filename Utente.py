# -*- coding: utf-8 -*-
"""
@author: marco
"""
import Prestito as p
import Generatore as gen
import Main as m
import sql as sql
import input as i

class Utente():   

    
    def generaUtente(tessera,nome,cognome,dtr,telefono,indirizzo):  #metodo utilizzato per generare un autore al primo avvio
        newUser= [tessera,nome,cognome,dtr,telefono,indirizzo,gen.generaEmail(nome,cognome)]
        return newUser
     
    def aggUtente(nome,cognome,data_registrazione,telefono,indirizzo,email): #genera la tessera dell'utente e ritorna una lista contenente tutti i dati dell'utente 
        newUser = [gen.generaTessera(),nome,cognome,data_registrazione,telefono,indirizzo,email]        
        return newUser

    def menuUtente():
        print("-------------------------------------------------------------\n")
        print("MENU BIBLIOTECARIO -> UTENTE \n >0) Indietro \n >1) Mostra Utenti \n >2) Aggiungi Utente\n >3) Rimuovi Utente \n >4) Stato Prestiti\n >>5) STOP")
        tipo = i.intValidation("Cosa vuoi fare?")  
        
        if tipo == '0': 
            m.Main.menuBibliotecario()
        elif tipo == '1': 
            Utente.mostraUtenti()                    
        elif tipo == '2':
            Utente.inserisciUtente()
        elif tipo == '3':
            Utente.rimuoviUtente()
        elif tipo == '4':
            x = i.tesseraUtenteValidation()
            p.Prestito.stato(x)
        elif tipo == '5':
            m.Main.quit()            
        elif (tipo !="" or tipo>5):
            print('\n[ERRORE] Inserisci un numero valido!\n')
            Utente.menuUtente()
        Utente.menuUtente()
   
    def mostraUtenti(): #passa alla funzione mostra la tebella Utenti
        sql.sqlMain.mostra("Utenti")    
        
    def trova(tessera): #passiamo alla funzione trova dello script sql i parametri (tabella, colonna e valore)
        sql.sqlMain.trova("Utenti",'tessera',tessera)

    def inserisciUtente(): #inseriamo i dati per la creazione dell'utente, tutti i dati vengono convalidati nello script input
        nome = i.stringValidation("nome utente")
        cognome = i.stringValidation("cognome utente")
        data_registrazione = i.dateValidation("data di registrazione")
        telefono = i.phoneValidation()
        indirizzo = input("Inserisci l'indirizzo utente > ")
        email = i.emailValidation()
        sql.sqlMain.inserisciUtente(Utente.aggUtente(nome,cognome,data_registrazione,telefono,indirizzo,email))
        
    def rimuoviUtente():
        print("-------------------------------------------------------------\n")
        print("MENU Utente -> Rimuovi Utente \n >0) Indietro \n >1) tessera \n >2) Nome e Cognome  \n >>3) STOP")
        tipo = i.intValidation("Cosa vuoi fare? ")  
        
        if tipo == '0': 
            Utente.menuUtente() 
        elif tipo == '1': #by tessera
            tessera = i.tesseraUtenteValidation()
            sql.sqlMain.rimuovi("Utenti","tessera",tessera)             
        elif tipo == '2': #by nome e cognome
            nome = i.stringValidation("nome utente")
            cognome = i.stringValidation("cognome utente")
            sql.sqlMain.rimuoviUtente(nome,cognome)
        elif tipo == '3':
            m.Main.quit()
        elif (tipo !="" or tipo>3):
            print('\n[ERRORE] Inserisci un numero valido!\n')
            Utente.rimuoviUtente()
        Utente.rimuoviUtente()       
    
    def trovaUtente(tessera):
        u = sql.sqlMain.trovaUtente(tessera)
        return u
