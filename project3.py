import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# Parte 4 – Pandas
# Crea un DataFrame Pandas con colonne:Cliente, Destinazione, Prezzo, Giorno_Partenza, Durata, Incasso.Calcola con Pandas:incasso totale dell’agenzia,incasso medio per destinazione,top 3 destinazioni più vendute.

data = {
    "Cliente":["Pippo","Pluto","Paperino","Gastone","Cip","Ciop","Paperone","Paperone","Pippo"],
    "Destinazione":["Livorno","Livorno","Milano","Milano","Milano","Pisa","Lucca","Mumbai","Casablanca"],
    "Prezzo":[21,21,105,105,105,5,200,100,50],
    "Giorno_Partenza":["12/12/2026","19/04/2026","12/11/2026","14/08/2026","14/07/2026","1/1/2026","12/12/2026","21/12/2026","20/05/2026"],
    "Durata":[7,14,24,32,45,1,5,30,20],
    "Incasso":[147,294,2520,3360,4725,5,2500,3000,1000]
}

df = pd.DataFrame(data)
df["Giorno_Partenza"] = pd.to_datetime(df["Giorno_Partenza"],format="%d/%m/%Y")
print(df)
print("\nL'incasso totale dell'agenzia è: ",df["Incasso"].sum())
print("\nIncasso medio per destinazione:\n",df.groupby("Destinazione")["Incasso"].mean())
print("\nTop 3 destinazioni:\n",df.groupby("Destinazione")["Incasso"].count().sort_values(ascending=False).head(3))

# Parte 5 – Matplotlib

# Crea un grafico a barre che mostri l’incasso per ogni destinazione.Crea un grafico a linee che mostri l’andamento giornaliero degli incassi.Crea un grafico a torta che mostri la percentuale di vendite per ciascuna destinazione.

valori = df.groupby("Destinazione")["Incasso"].sum().reset_index()["Incasso"].tolist()
categorie = df.groupby("Destinazione")["Incasso"].sum().reset_index()["Destinazione"].tolist()
print (df.groupby("Destinazione")["Incasso"].sum().reset_index())
plt.bar(categorie,valori,color="skyblue")
plt.title("Incasso per destinazione")
plt.show()

print (df.groupby("Giorno_Partenza")["Incasso"].sum().reset_index().sort_values("Giorno_Partenza"))
x = df.groupby("Giorno_Partenza")["Incasso"].sum().reset_index()["Giorno_Partenza"].tolist()
y = df.groupby("Giorno_Partenza")["Incasso"].sum().reset_index()["Incasso"].tolist()

plt.fill_between(x,y,color="lightblue",alpha=0.6)
plt.title("Andamento giornaliero incassi")
plt.show()

plt.pie(valori,labels=categorie, autopct="%1.1f%%")
plt.title("Percentuale di vendite per destinazione")
plt.show()

# Parte 6 – Analisi Avanzata
# Raggruppa i viaggi in categorie:
# "Europa", "Asia", "America", "Africa".(Puoi usare un dizionario che associa ogni destinazione a una categoria).
# Calcola con Pandas:incasso totale per categoria,durata media dei viaggi per categoria.Salva il DataFrame aggiornato in un CSV chiamato prenotazioni_analizzate.csv.

continenti = {
    "Livorno":"Europa",
    "Milano": "Europa", 
    "Pisa": "Europa", 
    "Lucca" : "Europa",
    "Mumbai": "Asia",
    "Casablanca":"Africa"
    }

df["Continenti"] = df["Destinazione"].map(continenti)

print (
    "\nIncasso totale per categoria / continente: \n", 
    df.groupby("Continenti")["Incasso"].sum().reset_index()
    )
print (
    "\nDurata media del viaggio per categoria / continente: \n",
    df.groupby("Continenti")["Durata"].mean().reset_index()
    )

df.to_csv("prenotazioni_analizzate.csv")

# Parte 7 – Estensioni
# Crea una funzione che restituisce i N clienti con più prenotazioni.Realizza un grafico combinato (barre + linea) che mostri:barre = incasso medio per categoria,linea = durata media per categoria.

def top_prenotazioni(df, n=3):
    return df["Cliente"].value_counts().head(n)

print("\nTop clienti per numero di prenotazioni:\n", top_prenotazioni(df))

fig, (ax1,ax2) = plt.subplots(1,2)
x = df.groupby("Continenti")["Incasso"].mean().reset_index()["Incasso"].tolist()
y = df.groupby("Continenti")["Incasso"].mean().reset_index()["Continenti"].tolist()
x2 = df.groupby("Continenti")["Durata"].mean().reset_index()["Durata"].tolist()
ax1.bar(y,x,color="skyblue",edgecolor="red")
ax2.plot(y,x2,color="black")

plt.show()