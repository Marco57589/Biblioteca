# -*- coding: utf-8 -*-
"""
@author: marco
"""
import Prestito as p
import input as i
import Main as m
import sql as sql
import datetime

class Prestito():  
    
    def menuUtentePrestiti(tessera):
        print("-------------------------------------------------------------\n")
        print("MENU UTENTE --> PRESTITI ("+tessera+")\n >0) Indietro \n >1) Stato Presiti \n >2) Nuovo Prestito\n >3) Salda Prestito \n>>4) STOP")
        tipo = i.intValidation("Cosa vuoi fare? ")      
        
        if tipo == '0': 
            m.Main.menuUtente(tessera)
        elif tipo == '1':  
            p.Prestito.stato(tessera)                            
        elif tipo == '2':
            p.Prestito.newPrestito(tessera)
        elif tipo == '3':
            p.Prestito.saldaPrestito(tessera)
        elif tipo == '4':
            m.Main.quit()
        elif (tipo !="" or tipo>4):
            print('\n[ERRORE] Inserisci un numero valido!\n')
            Prestito.menuUtentePrestiti(tessera)
        Prestito.menuUtentePrestiti(tessera)
    
    def stato(tessera): 
        sql.sqlMain.statoPrestiti(tessera)
        
    def newPrestito(tessera): # creiamo un prestito basato su una data fittizzia simulando di aver richiesto il prestito in quella
    # data, NB: quando si restituisce un prestito il ritardo viene calcolato in base ALLA DATA ATTUALE DEL SISTEMA!
        di = i.dateValidation("inserisci la data di 'oggi' (fittizzia, ovvero quando chiedi il prestito)")
        isbn = i.isbnValidation("inserisci l'isbn del libro che vuoi chiedere in prestito")
        print("NB: quando si restituisce un prestito il ritardo viene calcolato in base ALLA DATA ATTUALE DEL SISTEMA!")
        while True:
            q = i.intValidation("quanti libri vuoi prendere?")
            if 5 >= int(q) >0:
                break
        sql.sqlMain.newPrestito(tessera,di,isbn,q)

        
    def saldaPrestito(tessera):
        print("\n")
        dr = datetime.date.today()
        print(dr)
        sql.sqlMain.statoPrestiti(tessera)
        isbn = i.isbnValidation("\n inserisci l'isbn del libro che vuoi restituire")
        n = sql.sqlMain.countPrestito(isbn,tessera)
        print(n)
        if n > 0:
            while True:
                q = i.intValidation("quanti libri vuoi restituire?")
                if int(n) >= int(q) >0:
                    print("Operazione eseguita con successo!")
                    sql.sqlMain.saldaPrestito(tessera,dr,isbn,q)
                    break
                else:
                    print("Operazione non valida, controlla bene il numero di copie")
        else:
            print("Non devi restituire questo libro")       
