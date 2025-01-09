# esercizio tabelline
print("printo solo la tabellina richiesta dall'utente")

numero = int(input("Quale tabellina vuoi vedere? ").strip())

for fattore in range(1, 11):
    print(f"{numero} x {fattore} = {numero * fattore}")


# printo tutte le tabelline contemporaneamente con un ciclo for annidato
print("\nprinto tutte le tabelline contemporaneamente con un ciclo for annidato")

for primo in range (2, 10):
    print(f"Stampo la tabellina del {primo}")
    for secondo in range(1, 11):
        print(f"{primo} x {secondo} = {primo * secondo}")
    else:
        print("------")

