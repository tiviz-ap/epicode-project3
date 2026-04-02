import numpy as np

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

# Parte 2 – Programmazione ad Oggetti (OOP)

# Crea una classe Cliente con attributi: nome, età, vip.Aggiungi un metodo per stampare le informazioni.Crea una classe Viaggio con attributi: destinazione, prezzo, durata in giorni.Crea una classe Prenotazione che colleghi un cliente a un viaggio.Deve calcolare l’importo finale, con sconto del 10% se il cliente è VIP.Aggiungi un metodo dettagli() che stampa le informazioni complete.

class Cliente:
    def __init__(self,nome,eta,vip):
        self.nome = nome
        self.eta = eta
        self.vip = vip

    def anagrafica (self):
        print (f"Nome: {self.nome}, Età: {self.eta}, VIP: {self.vip}")
    
class Viaggio:
    def __init__(self,dest,prezzo,durata):
        self.dest=dest
        self.prezzo=prezzo
        self.durata=durata
    
class Prenotazione():
    def __init__(self,Cliente,Viaggio):
        self.durata = Viaggio.durata
        self.prezzo = Viaggio.prezzo
        self.vip = Cliente.vip

    def calcolaimporto(self):
        if (self.vip == True):
            self.importofinale = (self.prezzo * self.durata) * 0.90
        else:
            self.importofinale = self.prezzo * self.durata
        
        return self.importofinale

    def stampaimporto(self):
        print ("L'importo finale per il viaggio è di: ", self.importofinale)

cli_1 = Cliente("Andrea",39,False)
cli_2 = Cliente("Chobi",40,True)

via_1 = Viaggio("Pisa",100,10)

pre_1 = Prenotazione(cli_1,via_1)
pre_2 = Prenotazione(cli_2,via_1)

pre_1.calcolaimporto()
pre_2.calcolaimporto()

print("\nStampa Importo finale per cliente 1: ")
pre_1.stampaimporto()
print("\nStampa Importo finale per cliente 2: ")
pre_2.stampaimporto()


# Parte 3 – NumPy

# Genera un array NumPy di 100 prenotazioni simulate, con prezzi casuali fra 200 e 2000 €.Calcola e stampa:prezzo medio,prezzo minimo e massimo,deviazione standard,percentuale di prenotazioni sopra la media.

coda_prenotazioni = []

for i in range(100):
    coda_prenotazioni.append(Prenotazione(cli_1,Viaggio("Pisa",np.random.randint(200,2000),10)))

listaimporti = np.array ([x.calcolaimporto() for x in coda_prenotazioni])

print("\nL'importo medio è: ", listaimporti.mean())
print("\nL'importo più basso è", listaimporti.min())
print("\nL'importo massimo è:", listaimporti.max())
print("\nLa deviazione standard è: ", listaimporti.std())
print("\nPercentuale importi sopra la media: ",(len(np.where(listaimporti > listaimporti.mean())[0])*100) / np.size(listaimporti))
