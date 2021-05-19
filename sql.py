# NB: il programma utilizzato per il db é heidiSQL con sqlite3 https://www.heidisql.com/
# nei test non é risultato nessun problema con l'apertura del file chinooki.sqlite con sqlitebrowser
# in caso di problemi di lettura nella cartella Backup c'é uno script per creare totalmente un database già popolato

import os
import sqlite3
import datetime
import input as i

class sqlMain():    

    global db_filename
    global schema_filename
    
    db_filename = 'chinooki.sqlite' #se non presente si auto-genera       
    schema_filename = 'dbScript/createDB.sql' #da popolare con PRIMO AVVIO NEL MAIN MENU
    #db_filename = 'backup/chinooki.sqlite'
    #schema_filename = 'dbScript/createDbPopolato.sql'
    
    global msgDb
    msgDb= "\n -- \n DATABASE NON PRESENTE... CREAZIONE IN CORSO DI: "+db_filename+"\n -- \n"
    
        
    def mostraCatalogo(): #mestra il catalogo tra libro-autore stampando più autori se presenti nello stesso libro
        query = "SELECT * FROM Libro"           
        
        db_is_new = not os.path.exists(db_filename)       
        
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)        
            catalogo = conn.execute(query)
            
        colDescr = list(map(lambda x: x[0], catalogo.description))

        print("Catalogo BIBLIOTECA \n\n")
        for row in catalogo.fetchall():  
            print("----------------------------------------")
            print("Libro:")
            for x in range(len(row)): 
                if colDescr[x] == 'categoria':
                    categorie = conn.execute("SELECT LibroCategoria.categoria FROM LibroCategoria INNER JOIN Libro ON Libro.isbn = LibroCategoria.isbn WHERE Libro.isbn ='"+str(row[0])+"'").fetchall()                           
                    print("categorie:"+str(categorie))
                else:
                    print(colDescr[x]+" > "+str(row[x]))                  
                
            autori = conn.execute("SELECT Autore.* FROM LibroAutore INNER JOIN Autore ON LibroAutore.id = Autore.id WHERE isbn ='"+str(row[0])+"'")
            colDescrAutori = list(map(lambda x: x[0], autori.description))

            for row2 in autori.fetchall():   
                print("\nAutore: ")
                for x in range(len(row2)):                    
                    print(colDescrAutori[x]+" > "+str(row2[x])) 
                
        conn.close()

    def mostra(tabella):  #metodo generico per mostrare interamente una tabella
        query = "SELECT * FROM "+tabella
        db_is_new = not os.path.exists(db_filename)            
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)        
            lista = conn.execute(query)
            
        colDescr = list(map(lambda x: x[0], lista.description))     
        print(tabella+":\n")
        for row in lista.fetchall():  
            print("----------------------------------------")
           
            for x in range(len(row)):
                print(colDescr[x]+" > "+str(row[x]))
            #print("[DEBUG SQL] > "+query)
        conn.close()
        
    def trova(p1,p2,p3):   #metodo generico per "select" da (tabella, colonna, dove)      
        query = "SELECT * FROM "+p1+" WHERE "+p2+" = '"+p3+"'"
        print(query)
        db_is_new = not os.path.exists(db_filename)            
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)        
            lista = conn.execute(query)
            
        colDescr = list(map(lambda x: x[0], lista.description))     

        for row in lista.fetchall():  
            print("----------------------------------------")
            print(p1+":\n")
            for x in range(len(row)):
                print(colDescr[x]+" > "+str(row[x]))       
            
        conn.close()
        
    def rimuovi(p1,p2,p3): #metodo generico per rimuovere da (tabella, colonna, dove)
        query = "DELETE FROM "+str(p1)+" WHERE "+str(p2)+" LIKE '"+str(p3)+"'"
        print(query)
        db_is_new = not os.path.exists(db_filename)            
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)        
            conn.execute(query)           
        conn.close()           
        
#----------------------------------------------------------------------------------
   
    def generaLibro(data): #classe che genera e crea un collegamento libro-autore con un autore causale tra quelli
    # già presenti nel database
        query2 = "INSERT INTO LibroCategoria VALUES ('"+str(data[0])+"','"+str(data[5])+"')"
        db_is_new = not os.path.exists(db_filename)
        data2=[]
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)        
            query="SELECT id FROM Autore ORDER BY RANDOM()"
            idAutore = conn.execute(query)
            idAutore = idAutore.fetchone()[0]      
            data2.append(str(data[0]))
            data2.append(str(idAutore))
            
            conn.execute("INSERT INTO libro VALUES (?, ?, ?, ?, ?, ?, ?);", (data))
            print("INSERT INTO Libro VALUES "+str(data))
            query= "INSERT INTO LibroAutore VALUES ('"+str(data[0])+"','"+str(idAutore)+"')"        
            conn.execute(query)
            print("[DEBUG SQL] > "+query)
            conn.execute(query2)
            print("[DEBUG SQL] > "+query2)
        conn.close()
        
    def inserisciLibro(libro,autore): #inseriamo un libro data la lista passata e creiamo il collegamento tra libro e autore
    # nella tabella Libro-Autore (dato che un autore può scrivere più libri) e se si inserisce una categoria non presente
    # il programma ci consente di crearla durante l'inserimento
        query = "INSERT INTO LibroAutore VALUES ('"+str(libro[0])+"','"+str(autore)+"')"  
        query2 = "INSERT INTO LibroCategoria VALUES ('"+str(libro[0])+"','"+str(libro[5])+"')"
        db_is_new = not os.path.exists(db_filename)

        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)                
            
            n = conn.execute("SELECT count(nome) FROM Categoria WHERE nome LIKE '"+str(libro[5])+"'").fetchone()      
            n = int(''.join(map(str, n)))
            
            categoria = libro[5]
            if n > 0:
                conn.execute("INSERT INTO Categoria VALUES ('"+str(categoria)+"')")
                conn.execute("INSERT INTO libro VALUES (?, ?, ?, ?, ?, ?, ?);", (libro))
                conn.execute(query)
                print("[DEBUG SQL] > "+query)
                conn.execute(query2)
                print("[DEBUG SQL] > "+query2)  
                print("Libro aggiunto con successo!")
            else:
                while True:
                    x = i.intValidation("Categoria non presente nella biblioteca, vuoi aggiungerla? (1=si o 2=no)")
                    x = int(x)
                    if x == 1:
                        conn.execute("INSERT INTO Categoria VALUES ('"+str(categoria)+"')")
                        conn.execute("INSERT INTO Libro VALUES (?, ?, ?, ?, ?, ?, ?);", (libro))
                        conn.execute(query)
                        print("[DEBUG SQL] > "+query)
                        conn.execute(query2)
                        print("[DEBUG SQL] > "+query2)  
                        print("Libro aggiunto con successo!")                        
                    elif x == 2:
                        print("Libro non aggiunto.")                     
                    if x==1 or x ==2:
                        break
        conn.close()
        
        
    def modificaLibro(p1,p2,p3,p4): #modifichiamo un libro i parametri sono (Libro.colonna,uguale a, Libro.colonna da aggiornare, valore aggiornato)
        query="SELECT Libro.*,Autore.id FROM Libro INNER JOIN LibroAutore ON Libro.isbn = LibroAutore.isbn INNER JOIN Autore ON LibroAutore.id = Autore.id "
        query += "WHERE Libro."+p1+" like '"+p2+"'"   
        
        db_is_new = not os.path.exists(db_filename)
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)        
            ris = conn.execute(query)
            colDescr = list(map(lambda x: x[0], ris.description))    
            print("\nLIBRO SELEZIONATO")
            for row in ris.fetchall():  
                for x in range(len(row)):    
                    print(colDescr[x]+" > "+str(row[x]))       
                  
            query2 = "UPDATE Libro SET "+p3+" = '"+p4+"' WHERE Libro."+p1+" like '"+p2+"'"
            ris = conn.execute(query2)
            print("[DEBUG SQL] > "+query2)                         
        conn.close()
        
#----------------------------------------------------------------------------------
        
    def inserisciAutore(data):     #inseriamo un utente dalla lista passata     
        db_is_new = not os.path.exists(db_filename)
        
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)        
            conn.execute("INSERT INTO Autore VALUES (?, ?, ?, ?, ?, ?);", (data))
        conn.close()
        
    def rimuoviAutore(nAutore, cAutore): #rimuoviamo un autore in base al nome e al cognome
    #se ci sono più autori con lo stesso nome e cognome consente la scelta tra i casi
        nAutore = nAutore.lower() 
        cAutore = cAutore.lower()
        
        db_is_new = not os.path.exists(db_filename)
        
        query = "SELECT * FROM Autore WHERE nome like '"+nAutore+"' AND cognome like '"+cAutore+"'"     
        
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)        
            ris = conn.execute(query)
            colDescr = list(map(lambda x: x[0], ris.description))     
            ris=ris.fetchall()
            query=""            
            query= "DELETE FROM Autore WHERE "
            
            if len(ris) > 1:
                for row in ris:  
                    print("----------------------------------------")
                    print("Autore:\n")
                    for x in range(len(row)):
                        print(colDescr[x]+" > "+str(row[x]))
                selezione = i.idAutoreValidation("Ho trovato più corrispondenze, quale vuoi eliminare? (Inserisci l'id) ")                   
                query+= "id like '"+selezione+"'"
        
            else:
                query+="nome like '"+nAutore+"' AND cognome like '"+cAutore+"'"
                
            conn.execute(query)
            print("[DEBUG SQL] > "+query)
        conn.close()
    
    def mostraLibroAutore(idAutore): #mostra tutti i libri scritti da un autore (idAutore)
        query="SELECT Autore.*, Libro.isbn, Libro.titolo,Libro.annoPublicazione FROM Libro INNER JOIN LibroAutore ON Libro.isbn = LibroAutore.isbn INNER JOIN Autore ON LibroAutore.id = Autore.id WHERE Autore.id = '"+str(idAutore)+"'"
        
        db_is_new = not os.path.exists(db_filename) 

        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)        
        lista = conn.execute(query)
            
        colDescr = list(map(lambda x: x[0], lista.description))     
        print("Libri scritti dall'autore "+idAutore)
        for row in lista.fetchall():  
            print("----------------------------------------")
            for x in range(len(row)):
                print(colDescr[x]+" > "+str(row[x]))      
    
    
    
    def trovaAutore(nAutore,cAutore): #troviamo un autore in base al nome e al cognome
    #se ci sono più autori con lo stesso nome e cognome consente la scelta tra i casi
        nAutore = nAutore.lower() 
        cAutore = cAutore.lower()
        
        db_is_new = not os.path.exists(db_filename)
        
        query = "SELECT * FROM Autore WHERE nome like '"+nAutore+"' AND cognome like '"+cAutore+"'"     

        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)        
            ris = conn.execute(query)
            colDescr = list(map(lambda x: x[0], ris.description))     
            ris=ris.fetchall()
            query=""            
            query= "SELECT id FROM Autore WHERE "
            query2= "SELECT count(*) FROM Autore WHERE "
            
            if len(ris) > 1:
                for row in ris:  
                    print("----------------------------------------")
                    print("Autore:\n")
                    for x in range(len(row)):
                        print(colDescr[x]+" > "+str(row[x]))
                selezione = i.idAutoreValidation("Ho trovato più corrispondenze, inserisci l'id ")                   
                query += "id like '"+selezione+"'"  
                query2 += "id like '"+selezione+"'" 
            else:
                query += "nome like '"+nAutore+"' AND cognome like '"+cAutore+"'"
                query2 += "nome like '"+nAutore+"' AND cognome like '"+cAutore+"'"
                
            ris2 = conn.execute(query)
            ris2 = ris2.fetchall()
            
            esiste = conn.execute(query2).fetchone()
            esiste = int(''.join(map(str, esiste))) 
            
            if esiste > 0:
                idAutore = ''.join(ris2[0])
            else:
                idAutore = 0
                print("ERRORE! AUTORE NON ESISTENTE")            
           
            print("[DEBUG SQL] > "+query)
        conn.close()
        return idAutore
        
    
#----------------------------------------------------------------------------------
        
    def inserisciUtente(data):   #inseriamo un utente dalla lista passata            
        db_is_new = not os.path.exists(db_filename)        
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)        
            conn.execute("INSERT INTO Utenti VALUES (?, ?, ?, ?, ?, ?, ?);", (data))
            print("INSERT INTO Utenti VALUES "+str(data))
            query = "INSERT INTO PrestitiAttivi (tessera, num) VALUES ('"+data[0]+"',0)"
            conn.execute(query)
        conn.close()    
        
        
    def rimuoviUtente(nUtente, cUtente): #nomeAutore 
    # rimuove un utente dato nome e cognome, se ci sono utenti con lo stesso nome/cognome 
    # stampa i casi e consente la scelta
        nUtente = nUtente.lower() 
        cUtente = cUtente.lower()
        
        db_is_new = not os.path.exists(db_filename)
        
        query = "SELECT * FROM Utenti WHERE nome like '"+nUtente+"' AND cognome like '"+cUtente+"'"     
        
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)        
            ris = conn.execute(query)
            colDescr = list(map(lambda x: x[0], ris.description))     
            ris=ris.fetchall()
            query=""            
            query= "DELETE FROM Utenti WHERE "
            print(ris)
            if len(ris) > 1:
                for row in ris:  
                    print("----------------------------------------")
                    print("Utente:\n")
                    for x in range(len(row)):
                        print(colDescr[x]+" > "+str(row[x]))
                selezione = i.tesseraUtenteValidation("Ho trovato più corrispondenze, quale vuoi eliminare? (Inserisci la tessera) ")                   
                query+= "tessera like '"+selezione+"'"
        
            else:
                query+="nome like '"+nUtente+"' AND cognome like '"+cUtente+"'"
                
            conn.execute(query)
            print("[DEBUG SQL] > "+query)
            query = "DELETE FROM PrestitiAttivi WHERE tessera like '"+selezione+"'"
            conn.execute(query)
            query = "DELETE FROM Prestito WHERE tesseraUtente like '"+selezione+"'"
            conn.execute(query)
            
        conn.close()
    
    def trovaUtente(tessera):   #restituisce un utente in base al numero di tessera
        db_is_new = not os.path.exists(db_filename)
        query = "SELECT * FROM Utenti WHERE tessera like '"+tessera+"'"    
        
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)        
            ris = conn.execute(query)
            ris=ris.fetchall()

        return len(ris)

#----------------------------------------------------------------------------------
        
    def inserisciCategoria(categoria):      #inseriamo una categoria dentro la tabella categoria (se non é già presente)  
        categoria = categoria
        query = "SELECT count(nome) FROM Categoria WHERE nome = '"+categoria+"'"
        query2 = "INSERT INTO Categoria VALUES ('"+categoria+"')" 
        db_is_new = not os.path.exists(db_filename)
        
        
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)  
            n = conn.execute(query)
            n = n.fetchone()
            n = int(''.join(map(str, n)))  
            if n == 0:
                conn.execute(query2)
                print("[DEBUG SQL] > "+query2)
            else:
                print("Categoria già presente")
                        
        conn.close()

        
    def rimuoviCategoria(categoria):   #rimuoviamo una categoria dalla tabella categoria     
        categoria = categoria.lower()        
        query = "DELETE FROM Categoria WHERE nome = lower('"+categoria+"')"
        
        db_is_new = not os.path.exists(db_filename)
        
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema) 
            conn.execute(query)
            print("[DEBUG SQL] > "+query)
        conn.close()
        
    
    def aggiungiCategoria(isbn,categoria):  #inseriamo nella tabella libro-categoria il collegamento tra la categoria e il libro
    #se un libro ha più categorie
        query = "INSERT INTO LibroCategoria VALUES ('"+isbn+"','"+categoria+"')" 
        
        db_is_new = not os.path.exists(db_filename)
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema) 
            conn.execute(query)
            print("[DEBUG SQL] > "+query)
        conn.close()
    
    def restoreCategoria():    #ripristino la tebella cateogire con quelle presenti sul file
        query = "INSERT INTO Categoria (nome) SELECT nome FROM categoria_restore WHERE nome NOT IN Categoria"
        db_is_new = not os.path.exists(db_filename)        
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)
            conn.execute(query)
            print("[DEBUG SQL] > "+query)
        conn.close()
 
#----------------------------------------------------------------------------------

    def newPrestito(tessera,di,isbn,q): #chiediamo un prestito passando l'isbn, la tessera utente, la data di "oggi" e la quantita
    #NB: questa funzione esegue i seguenti controlli:
    #se si prova a restituire un libro non presente nella biblioteca
    #se si chiedono più libri del dovuto (massimo 5)
    #se si chiedono più libri di quelli disponibili
        n = 0
        tessera = tessera        
        db_is_new = not os.path.exists(db_filename)
        
        
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema) 
                
            query = "SELECT num FROM PrestitiAttivi WHERE tessera like '"+tessera+"'"
            n = conn.execute(query).fetchone()
            n = int(''.join(map(str, n))) 
            
            query = "SELECT count(*) FROM Libro WHERE isbn like '"+isbn+"'"
            esiste = conn.execute(query).fetchone()
            esiste = int(''.join(map(str, esiste))) 
            
            if esiste > 0:
                query = "SELECT copieDisponibili FROM Libro WHERE isbn like '"+isbn+"'"
                nLibri = conn.execute(query).fetchone()
                nLibri = int(''.join(map(str, nLibri))) 
    
                if (int(q)+int(n)) <= 5:                    
                    if int(q) <= int(nLibri):                
                        query = "UPDATE Libro SET copieDisponibili = copieDisponibili - "+str(q)+" WHERE isbn ='"+isbn+"'"
                        conn.execute(query)
                        
                        conn.execute("INSERT INTO Prestito (tesseraUtente,dataInizio,isbn,quantita) VALUES (?,?,?,?)",(tessera,di,isbn,q))
                        
                        query = "UPDATE PrestitiAttivi SET num = num + "+str(q)+" WHERE tessera ='"+tessera+"'"
                        conn.execute(query)
                    else:
                        print("Non ci sono abbastanza copie per soddisfare la tua richiesta!")                    
                else:
                    print("Hai troppi prestiti attivi, saldali prima di poterne chiedere altri!")
            else:
                print("Questo libro non é disponibile in questa biblioteca!")
               
        conn.close()
        
    def saldaPrestito(tessera,dr,isbn,q): #salda il prestito di un utente data la tessera, isbn e q (quantita)
    #NB, c'é un funzionamento molto particolare, ovvero se un utente chiede 5 volte in prestito lo stesso libro 
    #(uno per richiesta) e ne restituisce tutti di botto o più di quelli presenti nel singolo prestito
    # salva tutti gli id prestito e fa una sottrazione a scalare inserendo la data di restituzione una volta che la quantita
    # di quel prestito (della riga) raggiunge lo 0

        db_is_new = not os.path.exists(db_filename)        
        
        dataOggi = datetime.datetime.strptime(str(dr), "%Y-%m-%d").date()
        
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema) 
            
            codici = []
            qInCodice = []
            inizioPrestito = []
            
            query = "SELECT id,quantita,dataInizio FROM Prestito WHERE tesseraUtente LIKE '"+tessera+"'"
            ris1 = conn.execute(query)

            for row in ris1.fetchall():
                codici.append(row[0])
                qInCodice.append(row[1])
                inizioPrestito.append(row[2])

            count = q
            for x in range(len(codici)):                
                dataInizio = datetime.datetime.strptime(inizioPrestito[x], "%Y-%m-%d").date()
                differenza = dataOggi - dataInizio
                for y in range(qInCodice[x]):   
                    count = int(count)-1
                    query2 = "UPDATE Prestito SET ritardo = "+str(differenza.days)+" WHERE id = "+str(codici[x])
                    print(query2)
                    conn.execute(query2)
                    if int(count) > -1:
                        query = "UPDATE Prestito SET quantita = quantita - 1 WHERE id ="+str(codici[x])+""
                        conn.execute(query)
                        
            query = "UPDATE Prestito SET dataConsegna = '"+str(dr)+"' WHERE dataConsegna IS NULL and quantita = 0 AND tesseraUtente LIKE '"+tessera+"'"
            conn.execute(query)              
                        
            query = "UPDATE Libro SET copieDisponibili = copieDisponibili + "+str(q)+" WHERE isbn ='"+isbn+"'"
            conn.execute(query)

            query = "UPDATE PrestitiAttivi SET num = num - "+str(q)+" WHERE tessera ='"+tessera+"'"
            conn.execute(query)  
            
            
        conn.close()
    
    def statoPrestiti(tessera): #ritorna il numero di prestiti attivi e i loro dettagli
        db_is_new = not os.path.exists(db_filename)        
        
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema) 
            query = "SELECT num FROM PrestitiAttivi WHERE tessera like '"+tessera+"'"
            ris = conn.execute(query).fetchone()
            n = int(''.join(map(str, ris)))           
            
            query2 = "SELECT * FROM Prestito WHERE tesseraUtente like '"+tessera+"'"
            ris = conn.execute(query2)
            colDescr = list(map(lambda x: x[0], ris.description))     
            k=0
            print("Storico Prestiti")
            for row in ris.fetchall(): 
                if row[4] == 0:
                    k+=1
                print("----------------------------------------")
                print("Prestito:")
                for x in range(len(row)):
                    print(colDescr[x]+" > "+str(row[x]))
                print("[DEBUG SQL] > "+query)
                
            print("\n ATTUALMENTE QUESTO UTENTE HA "+str(n)+" PRESTITI ATTIVI E "+str(k)+" SALDATI")
        conn.close()
                
    def countPrestito(isbn,tessera):    #conta il numero di prestiti e tiene conto del caso in cui un utente con o senza
    #prestiti prova a riconsegnare un presito di un libro non presente o non preso in prestito
        db_is_new = not os.path.exists(db_filename)        
        
        with sqlite3.connect(db_filename) as conn:
            if db_is_new:
                print(msgDb)
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema) 
            query = "SELECT sum(quantita) FROM Prestito WHERE isbn LIKE '"+isbn+"' AND tesseraUtente LIKE '"+tessera+"'"
            ris = conn.execute(query).fetchone()
            
            query2 = "SELECT count(quantita) FROM Prestito WHERE isbn LIKE '"+isbn+"' AND tesseraUtente LIKE '"+tessera+"'"
            esiste = conn.execute(query2).fetchone()
            esiste = int(''.join(map(str, esiste))) 
            
            if esiste > 0:
                n = int(''.join(map(str, ris)))
            else:
                n = 0
                print("ERRORE! NESSUN PRESTITO TROVATO!")
            
            
        conn.close()
        return n
