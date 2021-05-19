# -*- coding: utf-8 -*-
"""
@author: marco
"""
import input as i
import sql as sql
import Main as m
import Autore as a

class Libro():
    
    def menuLibro():    #menu gestione libri per il bibliotecario
        print("-------------------------------------------------------------\n")
        print("MENU BIBLIOTECARIO -> LIBRO \n >0) Indietro \n >1) Mostra Libri \n >2) Aggiungi Libro \n >3) Rimuovi Libro\n >4) Modifica Libro \n >>5) STOP")
        tipo = i.intValidation("Cosa vuoi fare? ")  
        
        if tipo == '0': 
            m.Main.menuBibliotecario() 
        elif tipo == '1': 
            Libro.mostraLibri()                     
        elif tipo == '2':
            Libro.inserisciLibro() 
        elif tipo == '3':
            Libro.rimuoviLibro()  
        elif tipo == '4':
            Libro.modificaLibro() 
        elif tipo == '5':
            m.Main.quit()
        elif (tipo !="" or tipo>5):
            print('\n[ERRORE] Inserisci un numero valido!\n')
            Libro.menuLibro()
        Libro.menuLibro()
    
    def generaLibro(isbn,titolo,lingua,editore,anno_pubb,categoria,nCopDisp):#in base a tutti i parametri ritorna una lista newLibro
        newLibro = [isbn,titolo,lingua,editore,anno_pubb,categoria,nCopDisp]                
        return newLibro
    
    def mostraLibri(): #tramite la funzione mostra (mostra tabella) stampa tutti i libri
        sql.sqlMain.mostra("Libro")
    
    def mostraLibro(p1,p2,p3): #passiamo alla funzione trova dello script sql i parametri (tabella, colonna e valore)
        sql.sqlMain.trova(p1,p2,p3)        
        
    def inserisciLibro(): #inseriamo i dati per la creazione dell'utente, tutti i dati vengono convalidati nello script input
        isbn = i.isbnValidation("isbn")
        titolo = input("titolo > ")
        lingua = i.stringValidation("lingua")
        editore =i.stringValidation("editore")
        anno_pubb = i.yearValidation("anno pubblicazione")
        categoria = i.stringValidation("categoria") 
        nCopDisp = i.intValidation("nCopDisp") 
        while True:
            nAutore = i.stringValidation("nome autore")
            cAutore = i.stringValidation("cognome autore")         
            idAutore = a.Autore.trovaAutore(nAutore,cAutore)
            if idAutore != 0:
                break        
        sql.sqlMain.inserisciLibro(Libro.generaLibro(isbn,titolo,lingua,editore,anno_pubb,categoria,nCopDisp),idAutore)
        while True:  #dato che un libro può avere più categorie
            cat = i.intValidation("Vuoi aggiungere altre categorie al libro? (1=si - 2=no)")
            cat = int(cat)
            if cat == 1:                
                cat = i.stringValidation("categoria da aggiungere al libro"+isbn)
                sql.sqlMain.aggiungiCategoria(isbn,cat)
            elif cat == 2:
                break
                
                
 
       
    def rimuoviLibro(): #possiamo rimuovere un libro per isbn o per titolo
        print("-------------------------------------------------------------\n")
        print("MENU LIBRO -> Rimuovi Libro \n >0) Indietro \n >1) ISBN \n >2) TITOLO \n >>3) STOP")
        tipo = i.intValidation("Cosa vuoi fare? ")  
        
        if tipo == '0': 
            Libro.menuLibro() 
        elif tipo == '1': 
            x = i.isbnValidation("isbn del libro che vuoi rimuovere") 
            sql.sqlMain.rimuovi('Libro','isbn',x)                   
        elif tipo == '2':
            x = input("Titolo del libro che vuoi rimuovere >")
            sql.sqlMain.rimuovi('Libro','titolo',x)
        elif tipo == '3':
            m.Main.quit()
        elif (tipo !="" or tipo>3):
            print('\n[ERRORE] Inserisci un numero valido!\n')
            Libro.rimuoviLibro()
        Libro.rimuoviLibro()
        

    def modificaLibro(): #modifichiamo un libro, per selezionare il libro da modificare inseriamo l'isbn (la ricerca per titolo non é stata implementata)
        print("-------------------------------------------------------------\n")
        print("MENU LIBRO -> Modifica libro \n >0) Indietro \n >1) ISBN \n >-) ---- \n >>3) STOP")
        tipo = i.intValidation("Cosa vuoi fare? ")  
        
        if tipo == '0': 
            Libro.menuLibro() 
        elif tipo == '1': 
            libroDaModificare = i.isbnValidation("isbn del libro che vuoi modificare") 
        #    colIndice = 'isbn'                  
        # elif tipo == '2': #rimosso 
        #     libroDaModificare = i.stringValidation("Titolo del libro che vuoi modificare")
        #     colIndice = 'titolo'
        elif tipo == '3':
            m.Main.quit()
        elif (tipo !="" or tipo>3 or tipo==2):
            print('\n[ERRORE] Inserisci un numero valido!\n')
            Libro.modificaLibro()
            
        while True:
            tipo = input(">>0) FINE \n >-) ----\n >1) Titolo\n >2) Lingua\n >3) Editore\n >4) Anno Publicazione\n >5) Categoria\n >6) nCopie \nQuale campo vuoi modificare? \n (inserisci il numero) > ")  
    
            if tipo == '0': 
                break
            # elif tipo == '1':                     rimossa
            #     campo = "isbn"
            #     modifica = i.isbnValidation("isbn del libro che vuoi modificare")                  
            elif tipo == '1':
                campo = "titolo"
                modifica = i.stringValidation(" il nuovo titolo del libro")
            elif tipo == '2':
                campo = "lingua"
                modifica = i.stringValidation(" la nuova lingua del libro")
            elif tipo == '3':
                campo = "editore"
                modifica = i.stringValidation(" il nuovo editore del libro")
            elif tipo == '4':
                campo = "annoPublicazione"
                modifica = i.yearValidation(" il nuovo anno di publicazione del libro")
            elif tipo == '5':
                campo = "categoria"
                modifica = i.stringValidation(" la nuova categoria del libro")
            elif tipo == '6':
                campo = "copieDisponibili"
                modifica = i.intValidation(" il nuovo numero di copie del libro") 
            
            sql.sqlMain.modificaLibro('isbn',libroDaModificare,campo,modifica)
        Libro.modificaLibro()
        