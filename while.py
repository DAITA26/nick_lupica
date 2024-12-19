# esempio break

contatore = 1

while contatore <= 10:
    print("contatore vale", contatore)
    contatore = contatore + 1
    # contatore += 1
    if contatore == 6:
        print("trovato", contatore)
        break
print("Istruzioni dopo il while")


# esempio continue
contatore = 0

while contatore <=9:
    contatore +=1
    if contatore == 4:
        print("Questa volta passo ")
        continue

    print("contatore vale", contatore)


# esempio else
contatore = 1
x = 4

while contatore <= 10:
    if contatore == x:
        print("trovato", contatore)
        break
    contatore += 1
else:
    print("non ho trovato il numero")

# esempio validazione input: l'utente inserisce la password finche non l'azzecca
password = ""

while password != "laMiaPassword":
    password = input("Inserisci la tua password ").strip()
print("Accesso consentito")
















