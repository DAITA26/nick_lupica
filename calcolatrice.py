# input -> quale operazione vuoi fare?
# input -> primo numero
# input -> secondo numero
# controllo l'operazione scelta, controllo se operazione o meno
# svolgo il calcolo
# stampo il risultato

print("Programma che crea una calcolatrice")

# Richiesta all'utente del tipo di operazione che vuole fare
operazione = input("Che tipo di operazione vuoi fare? ")

# Richiesta di inserimento dei numeri
x = float(input("Inserisci primo numero: "))
y = float(input("Inserisci secondo numero: "))

# Controllo dell'operazione scelta
if operazione == "somma" or operazione == "+":
    print(f"Risultato della somma: {x + y}")
elif operazione == "sottrazione" or operazione == "-":
    print(f"Risultato della sottrazione: {x - y}")
elif operazione == "moltiplicazione" or operazione == "x":
    print(f"Risultato della moltiplicazione: {x * y}")
elif operazione == "divisione" or operazione == "/":
    if y == 0:
        print("Errore: divisione per zero non consentita.")
    else:
        print(f"Risultato della divisione: {x / y}")
else:
    print("Operazione non valida. Scegli tra somma, sottrazione, moltiplicazione, divisione.")
