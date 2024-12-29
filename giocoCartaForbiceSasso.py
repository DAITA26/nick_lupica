import random

contatore = 1


while contatore <= 5:
    scelta_computer = random.randint(1, 3)
    # DEBUG
    print(scelta_computer)
    print(f"Sei al {contatore} Round! ")
    print("Scegli tra sasso, carta e forbice")
    mossa = input("Quale mossa scegli: ").strip().lower()
    if not mossa.isalpha():
        print("Puoi inserire solo una tra le mosse carta, sasso e forbice")
        print("")
        contatore += 0
        continue
    contatore += 1

#carta = 1, sasso = 2, forbice = 3
    if mossa == "carta" and scelta_computer == 2 or mossa == "sasso" and scelta_computer == 3 or mossa == "forbice" and scelta_computer == 1:
        print(f"Hai vinto! Il tuo avversario aveva scelto {scelta_computer}")
        print("")

    elif mossa == "carta" and scelta_computer == 3 or mossa == "sasso" and scelta_computer == 1 or mossa == "forbice" and scelta_computer == 2:
        print("Hai perso")
        print("")
    elif  mossa == "carta" and scelta_computer == 1 or mossa == "sasso" and scelta_computer == 2 or mossa == "forbice" and scelta_computer == 3:
        print(f"Hai pareggiato! Entrambi avete scelto {mossa}.")
        print("")
    else:
        print("Non hai inserito una mossa valida! Riprova.")
        print("")