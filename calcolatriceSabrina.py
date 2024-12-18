#CALCOLATRICE FATTA DA SABRINA

#gestire operazione non consentita
#gestire numeri non validi
#gestire spazi e lower
#imput -> quale operazione fare

operatore = input("""
Scegli un'operazione da svolgere
1 + somma
2 - differenza
3 * moltiplicazione
4 / divisione
""").strip().lower()

#controllo la validità dell'operatore
if (operatore == "1" or operatore == "+" or operatore == "somma" or operatore == "addizione"):
    print("Hai scelto la somma")
    a = input("Inserisci il primo addendo").strip()
    #controllo se il valore inserito è alfabetico
    if a.isalpha():
        print("devi inserire un numero!")
    else:
        print(f"hai inserito il numero {a}")
        a = float(a)
        b =input("Inserisci secondo addendo").strip()
        if b.isalpha():
            print("devi inserire un numero!")
        else:
            b = float(b)
        #eseguo la somma
            risultato = a + b
            print(f"il tuo risultato è {risultato}")

elif (operatore == "2"
      or operatore == "-"
      or operatore == "differenza"
      or operatore == "sottrazione"):
    print("Hai scelto la sottrazione")
    a = float(input("Inserisci il minuendo ").strip())
    b = float(input("Inserisci il sottraendo ").strip())
    # eseguo la meno
    risultato = a - b

elif (operatore == "3"
      or operatore == "*"
      or operatore == "x"
      or operatore == "prodotto"
      or operatore == "moltiplicazione"):
    print("Hai scelto la moltiplicazione")
    a = float(input("Inserisci il primo fattore ").strip())
    b = float(input("Inserisci il secondo fattore ").strip())
    # eseguo la somma
    risultato = a * b

elif (operatore == "4"
      or operatore == "/"
      or operatore == ":"
      or operatore == "rapporto"
      or operatore == "divisione"):
    print("Hai scelto la divisione")
    a = float(input("Inserisci dividendo ").strip())
    b = float(input("Inserisci divisore ").strip())
    # eseguo la diviso
    risultato = a / b

else:
    print("---operazione non valida---")

#input -> primo numero
#input -> secondo numero

#controllo l'operazione scelta