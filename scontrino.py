# esercizio 16 dicembre

print("Programma che visualizza uno scontrino relativo all'acquisto di un prodotto dati nome del prodotto, quantità desiderata e prezzo")

item = input("Che cosa vuoi comprare? ")
price = input("Quanto costa? ")
qty = input("Quante ne compri? ")

# metodo_1 - calcolare il risultato e metterlo in una variabile
tot = round(int(qty) * float(price))
print(F"Per comprare {qty} di {item} devi pagare {tot}€. Grazie e arrivederci")

# metodo_2 - calcolare il risultato e mettere la formula nella f strings
print(F"Per comprare {qty} di {item} devi pagare {round(int(qty) * float(price), 2)}€. Grazie e arrivederci")



