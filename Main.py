# -*- coding: utf-8 -*-
"""
@author: marco
"""
import sys

import Database as db
import Categoria as cat
import Libro as l
import Prestito as p
import Utente as u
import Autore as a 
import Main as m
import input as i
class Main():

    def menuStart():
        
        print("-------------------------------------------------------------\n")
        print("Benvenuto alla biblioteca San Paskoly\n >1) Accedi come bibliotecario \n >2) Accedi come utente \n >3) PRIMO AVVIO! \n >>4) STOP")
        tipo = i.intValidation("Cosa vuoi fare?")      
     
        if tipo == '1': 
            m.Main.menuBibliotecario()                              
        elif tipo == '2':
            m.Main.loginUtente()            
        elif tipo == '3':
            while True:
                try:
                    n = int(input("Per il primo avvio é richiesto un parametro che comporterà un popolamento esponenziale \n (per rendere più semplica la correzione per via delle stampe in console \ne' consigliabile un valore tra 5-10) > "))
                    break
                except ValueError:
                    print("\nERRORE inserimento")               
            db.Database.primoAvvio(n)  
            m.Main.menuStart()
        elif tipo == '4':
            m.Main.quit()
        elif (tipo !="" or tipo>4):
            print('\n[ERRORE] Inserisci un numero valido!\n')
            m.Main.menuStart()
        m.Main.menuStart()
        
#--------------------------------------------------------------------------------------------------------------------
        
    def menuBibliotecario():
        print("-------------------------------------------------------------\n")
        print("MENU BIBLIOTECARIO \n >0) Indietro \n >1) Mostra Catalogo \n >2) Categorie \n >3) Autori\n >4) Libro \n >5) Utenti \n >>6) STOP")
        tipo = i.intValidation("Cosa vuoi fare? ")      
        
        if tipo == '0': 
            m.Main.menuStart()
        elif tipo == '1': 
            db.Database.mostraCatalogo()                            
        elif tipo == '2':
            cat.GestioneCategorie.menuCategoria()
        elif tipo == '3':
            a.Autore.menuAutore()
        elif tipo == '4':
            l.Libro.menuLibro()
        elif tipo == '5':            
            u.Utente.menuUtente()
        elif tipo == '6':
            m.Main.quit()
        elif (tipo !="" or tipo>5):
            print('\n[ERRORE] Inserisci un numero valido!\n')
            m.Main.menuBibliotecario()
        m.Main.menuBibliotecario()          

#--------------------------------------------------------------------------------------------------------------------
          
    def loginUtente():
        while True:
            print("Effettua l'accesso all'area utente (inserisci il numero della tua tessera) > ")    
            tessera = i.tesseraUtenteValidation()
            n = u.Utente.trovaUtente(tessera)
            if n > 0:
                m.Main.menuUtente(tessera)
                break
            else:
                print("Utente non trovato")       
        
    
    def menuUtente(tessera):
        print("-------------------------------------------------------------\n")
        print("Benvenuto "+tessera+" alla biblioteca San Paskoly\n >0) Disconnetti \n >1) Mostra dati \n >2) Prestiti \n >3) Visualizza Catalogo \n>>4) STOP")
        tipo = i.intValidation("Cosa vuoi fare? ")      
        
        if tipo == '0': 
            m.Main.menuStart()
        elif tipo == '1': 
            u.Utente.trova(tessera)                           
        elif tipo == '2':
            p.Prestito.menuUtentePrestiti(tessera)
        elif tipo == '3':
            db.Database.mostraCatalogo()
        elif tipo == '4':
            m.Main.quit()
        elif (tipo !="" or tipo>4):
            print('\n[ERRORE] Inserisci un numero valido!\n')
            m.Main.menuUtente(tessera)
        m.Main.menuUtente(tessera)        
    

#--------------------------------------------------------------------------------------------------------------------
             
    def quit():
        sys.exit()
           

    if __name__ == "__main__":   
        menuStart()                 
        
