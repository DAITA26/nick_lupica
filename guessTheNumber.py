import random

numero_segreto = random.randint(1, 100)
tentativiRimasti = 5

# DEBUG
print(numero_segreto)

while tentativiRimasti > 0:
    print(f"Hai ancora {tentativiRimasti} tentativi")
    scommessa = input("Quale numero scegli? ").strip()
    if not scommessa.isdigit():
        print("Puoi inserire solo numeri")
        tentativiRimasti -= 1
        continue
    scommessa = int(scommessa)
    tentativiRimasti -= 1

    if scommessa == numero_segreto:
        print("Hai vinto!")
        break
    else:
        print("Che peccato! Hai sbagliato")
        if scommessa > numero_segreto:
            print("Prova con un numero più BASSO...")
        else:
            print("Prova con un numero più ALTO...")

else:
    print(f"Il numero da indovinare era {numero_segreto}")

