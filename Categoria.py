# -*- coding: utf-8 -*-
"""
@author: marco
"""
import sql as sql
import Main as m
import input as i

class GestioneCategorie(): 
    
    def menuCategoria(): #menu gestione categorie per bibliotecario
        print("-------------------------------------------------------------\n")
        print("MENU BIBLIOTECARIO -> CATEGORIA \n >0) Indietro \n >1) Mostra Categorie \n >2) Inserisci Categoria \n >3) Rimuovi Categoria\n >4) Ripristina Categorie \n >>5) STOP")
        tipo = i.intValidation("Cosa vuoi fare? ")  
        
        if tipo == '0': 
            m.Main.menuBibliotecario() 
        elif tipo == '1': 
            GestioneCategorie.mostraCategorie()                          
        elif tipo == '2':
            while True:
                try:
                    newCat = str(input("Inserisci la categoria > "))
                    break
                except ValueError:
                    print("\nERRORE inserimento")  
            GestioneCategorie.inserisciCategoria(newCat)  
        elif tipo == '3':
            while True:
                try:
                    delCat = str(input("Inserisci la categoria da rimuovere > "))
                    break
                except ValueError:
                    print("\nERRORE inserimento")  
            GestioneCategorie.rimuoviCategoria(delCat)
        elif tipo == '4':
            GestioneCategorie.ripristinaCategorie()
        elif tipo == '5':
            m.Main.quit()
        elif (tipo !="" or tipo>5):
            print('\n[ERRORE] Inserisci un numero valido!\n')
            GestioneCategorie.menuCategoria()
        GestioneCategorie.menuCategoria()
   
    def mostraCategorie(): #mostriamo la tabella "Categoria"
        sql.sqlMain.mostra("Categoria")
        
    def inserisciCategoria(newCat): #inseriamo una categoria dentro la tabella categoria
        categoria = str(newCat)
        sql.sqlMain.inserisciCategoria(categoria)
        
    def rimuoviCategoria(delCat): #rimuoviamo una categoria dalla tabella categoria
        categoria = str(delCat)
        sql.sqlMain.rimuoviCategoria(categoria)
        
    def ripristinaCategorie():  #re-inseriamo le categorie base nella tabella categoria
        sql.sqlMain.restoreCategoria()
  