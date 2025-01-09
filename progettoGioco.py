#Lavoro per le vacanze a dicembre.
#Creare un gioco stile carta-forbice-sasso in cui metto in competizione giocatore e pc

import random
scelta_computer = random.randint(1, 3)

carta = 1
sasso = 2
forbice = 3

# DEBUG
# print(scelta_computer)

#Input scelta per l'utente
print("1 = carta, 2 = sasso, 3 = forbice")
scelta_giocatore = int(input("Scegli il numero corrispondente alla tua mossa "))


if scelta_giocatore == scelta_computer:
    print(f"Pareggio! Entrambi i giocatori hanno scelto {scelta_giocatore}")
elif scelta_giocatore == 1 and scelta_computer == 3 or scelta_giocatore == 2 and scelta_computer == 1 or scelta_giocatore == 3 and scelta_computer == 2:
    print("Hai perso")
else:
    print("Hai vinto")
