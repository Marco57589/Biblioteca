# -*- coding: utf-8 -*-
"""
@author: marco
"""

import Main as m
import Generatore as gen
import sql as sql
import input as i

class Autore():
    
    def generaAutore(nome,cognome,data_nasc,luogo_nasc):#creiamo una lista con i dati dell'autore assegnando una descrizione statica
        descrizione=" AUTORE PREGENERATO - NO DESC"
        newAutore = [gen.generaCodAutore(nome,cognome,luogo_nasc),nome,cognome,data_nasc,luogo_nasc,descrizione]
        return newAutore

    def aggAutore(nome,cognome,data_nasc,luogo_nasc,descrizione): #creiamo una lista con tutti i dati dell'autore che abbiamo creato
        newAutore = [gen.generaCodAutore(nome,cognome,luogo_nasc),nome,cognome,data_nasc,luogo_nasc,descrizione]
        return newAutore     
    
    def menuAutore():
        print("-------------------------------------------------------------\n")
        print("MENU BIBLIOTECARIO -> AUTORE \n >0) Indietro \n >1) Mostra Autori \n >2) Mostra autore e relativi libri \n >3) Inserisci Autore\n >4) Rimuovi Autore \n >>5) STOP")
        tipo = i.intValidation("Cosa vuoi fare? ")  
        
        if tipo == '0': 
            m.Main.menuBibliotecario()  #V
        elif tipo == '1': 
            Autore.mostraAutori()   #V                     
        elif tipo == '2':
            Autore.mostraLibroAutore() # <-----------------
        elif tipo == '3':
            Autore.inserisciAutore()    #V
        elif tipo == '4':
            Autore.rimuoviAutore()  #V
        elif tipo == '5':
            m.Main.quit()
        elif (tipo !="" or tipo>5):
            print('\n[ERRORE] Inserisci un numero valido!\n')
            Autore.menuAutore()
        Autore.menuAutore()
   
    def mostraAutori(): #mostra la tabella Autore
        sql.sqlMain.mostra("Autore")
    
    def mostraLibroAutore():    #Mostriamo tutti i libri scritti da un determinato autore
        x=i.idAutoreValidation()
        sql.sqlMain.mostraLibroAutore(x)
        
    def inserisciAutore(): #creiamo un autore, tutti gli input vengono "validati" dallo script input
        nome = i.stringValidation("nome")
        cognome = i.stringValidation("cognome")
        data_nasc = i.dateValidation("data di nascita")
        luogo_nasc =i.stringValidation("luogo")
        descrizione = i.stringValidation("descrizione")
        sql.sqlMain.inserisciAutore(Autore.aggAutore(nome,cognome,data_nasc,luogo_nasc,descrizione))   
        
    def rimuoviAutoreT(): #rimuoviamo dal database l'autore passando i parametri (tabella,colonna,valore)
        x = i.idAutoreValidation()
        sql.sqlMain.rimuovi("Autore","id",x)
        
    def rimuoviAutore(): #scegliamo se rimuovere un autore data la tessera o un nome
        #se più autore hanno lo stesso nome il programma stampera la lista di essi e permetterà la scelta
        print("-------------------------------------------------------------\n")
        print("MENU Autore -> Rimuovi Autore \n >0) Indietro \n >1) id \n >2) Nome e Cognome  \n >>3) STOP")
        tipo = i.intValidation("Cosa vuoi fare? ")  
        
        if tipo == '0': 
            Autore.menuAutore() 
        elif tipo == '1': #by id
            tessera = i.idAutoreValidation()
            sql.sqlMain.rimuovi("Autore","id",tessera)             
        elif tipo == '2': #by nome e cognome
            nome = i.stringValidation("nome autore")
            cognome = i.stringValidation("cognome autore")
            sql.sqlMain.rimuoviAutore(nome,cognome)
        elif tipo == '3':
            m.Main.quit()
        elif (tipo !="" or tipo>3):
            print('\n[ERRORE] Inserisci un numero valido!\n')
            Autore.rimuoviAutore()
        Autore.rimuoviAutore()      
        
    def trovaAutore(nAutore,cAutore): #troviamo l'id dell'autore dato il suo nome e il suo conogme
        autore = sql.sqlMain.trovaAutore(nAutore,cAutore)
        return autore   
    
    if __name__ == "__main__":
        trovaAutore("valerio","alberti")