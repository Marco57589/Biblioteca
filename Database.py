# -*- coding: utf-8 -*-
"""
@author: marco
"""
import random

import Libro as l
import Utente as u
import Autore as a 
import Generatore as gen

import sql as sql

class Database():
    

    def mostraCatalogo():
        sql.sqlMain.mostraCatalogo()   
    
    def primoAvvio(n):  #generiamo un database in base al parametro in input
         p2=round(n*random.uniform(0.75, 4.50))
         p3=round(n*random.uniform(0.55, 2.75))
         for x in range(n):   
            sql.sqlMain.inserisciAutore(a.Autore.generaAutore(gen.generaNome(),gen.generaCognome(),gen.generaDataNascita(),gen.generaLuogo()))
            
         for x in range(p2):        
            sql.sqlMain.generaLibro(l.Libro.generaLibro(gen.generaISBN(),gen.generaTitolo(),gen.generaLingua(),gen.generaEditore(),random.randint(1800,2021),gen.generaCategoria(),random.randint(0,50)))

         for x in range(p3):    
            sql.sqlMain.inserisciUtente(u.Utente.generaUtente(gen.generaTessera(),gen.generaNome(),gen.generaCognome(),gen.generaData(),gen.generaNumero(),gen.generaIndirizzo()))

       