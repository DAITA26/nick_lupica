import random

# Dobbiamo fare 5 domande
# Per ogni domanda la macchina seleziona una risposta giusta a caso
# salva la risposta corretta in una lista
# Per ogni domanda viene richiestp all'utente di scegliere una risposta e quella viene salvata in una lista
# Per ogni domanda facciamo il confronto tra le due risposte
# Alla fine delle domande voglio vedere il punteggio

# Le domande le salviamo in una tupla
domande = ("A quale colore sto pensando?", "A quale città sto pensando?",
           "A quale frutto sto pensando?", "A quale animale sto pensando?",
           "A quale professione sto pensando?")


# le opzioni le salviamo in dizionari
# Ciascuna ha 4 opzioni di risposta
colori = {"A": "Magenta", "B": "Vinaccia", "C": "Bordeaux", "D": "Cremisi"}
citta = {"A": "Milano", "B": "Roma", "C": "Bari", "D": "Catania"}
frutti = {"A": "Mango", "B": "Cocco", "C": "Mela", "D": "Pera"}
animali = {"A": "Elefante", "B": "Volpe", "C": "Leone", "D": "Tigre"}
professioni = {"A": "Idraulico", "B": "Cameriere", "C": "Manager", "D": "Avvocato"}

risposte_utente = []
risposte_pc = []
punteggio = 0

# Funzione per fare una domanda
def fai_domanda(indice_domanda):
    global punteggio
    # Stampa la domanda
    print(domande[indice_domanda])

    # Seleziona le risposte per questa domanda
    if indice_domanda == 0:
        risposte = colori
    elif indice_domanda == 1:
        risposte = citta
    elif indice_domanda == 2:
        risposte = frutti
    elif indice_domanda == 3:
        risposte = animali
    elif indice_domanda == 4:
        risposte = professioni

    for opzione in risposte:
        print(f"{opzione}: {risposte[opzione]}")

    risposta_pc = random.randint(0, 3)
    y = ("A", "B", "C", "D")
    # DEBUG risposta corretta pc
    print("La risposta corretta è:", y[risposta_pc])
    risposte_pc.append(y[risposta_pc])

    # L'utente inserisce la sua risposta
    risposta_utente = input("Scegli la tua risposta (A, B, C, D): ").strip().upper()

    if risposta_utente == y[risposta_pc]:
        print("Bravo! Hai indovinato!")
        risposte_utente.append(risposta_utente)
        punteggio += 1

    else:
        risposte_utente.append(risposta_utente)
        print(f"Sbagliato! La risposta corretta era: {y[risposta_pc]}")

def gioca():

    for i in range(len(domande)):
        fai_domanda(i)
    print(f"Le risposte corrette erano {risposte_pc}")
    print(f"Le tue risposte erano {risposte_utente}")
    print(f"Il tuo punteggio finale è: {punteggio} su {len(domande)}")
    print(f"La percentuale di vittorie è stata del {punteggio / (len(domande)) * 100}%")
# Avvia il quiz
gioca()

