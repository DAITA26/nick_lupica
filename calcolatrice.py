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
numero_1 = float(input("Inserisci primo numero: "))
numero_2 = float(input("Inserisci secondo numero: "))

# Controllo dell'operazione scelta
if operazione == "somma" or operazione == "+":
    print(f"Risultato della somma: {numero_1 + numero_2}")
elif operazione == "sottrazione" or operazione == "-":
    print(f"Risultato della sottrazione: {numero_1 - numero_2}")
elif operazione == "moltiplicazione" or operazione == "x":
    print(f"Risultato della moltiplicazione: {numero_1 * numero_2}")
elif operazione == "divisione" or operazione == "/":
    if numero_2 == 0:
        print("Errore: divisione per zero non consentita.")
    else:
        print(f"Risultato della divisione: {numero_1 / numero_2}")
else:
    print("Operazione non valida. Scegli tra somma, sottrazione, moltiplicazione, divisione.")
