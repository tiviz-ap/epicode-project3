# Progetto d’Esame – Analisi di un Sistema di Prenotazione Viaggi
# Scenario Reale
# Un’agenzia di viaggi online vuole realizzare un sistema informatico per gestire le prenotazioni dei clienti.Il sistema deve permettere di:
# memorizzare le informazioni dei clienti e dei viaggi prenotati,calcolare statistiche sulle vendite,analizzare i dati con strumenti avanzati,visualizzare i risultati in forma grafica.

# ConsegnA (da svolgere in Python)

# Parte 1 – Variabili e Tipi di Dati

# Definisci variabili per rappresentare le seguenti informazioni di un cliente:nome (stringa),età (intero),saldo conto (float),stato VIP (booleano).✅ Esempio: nome = "Mario Rossi", eta = 34, saldo = 2500.75, vip = TrueCrea una lista di destinazioni disponibili (almeno 5 città).Definisci un dizionario che associa ogni destinazione a un prezzo medio del viaggio.

nome = "Andrea Paradisi"
eta = 39
saldo = 99.99
vip = False

città = ["Livorno","Lucca","Milano","Roma","Venezia"]
costo_medio = [5.5,99.9,200,100,999.99]
costo_medio_viaggio = zip(città, costo_medio)
#print (tuple(costo_medio_viaggio))


