def saluta(name, age, city):
    print(f"ciao {name} di {city} ")
    print(f"Hai {age} anni")

def funzione():
    print("Sono la funzione funzione()")


print("Ora eseguo la funzione saluta()")
saluta("Alice", 25, "Roma")
saluta("Mario", 30, "Rimini")
saluta("Claudio", 42, "Milano")
print("Ho finito di eseguire la funzione saluta()")


def somma(a,b):
    sum = a + b
    print(f"la somma di {a} e {b} è {sum}")

somma(5, 3)
# somma("Alice", 42)
# somma(42, "alice")
print("")

# parametri di default
print("Parametri di default")
def somma(a = 5,b = 8):
    sum = a + b
    print(f"la somma di {a} e {b} è {sum}")

somma()
somma(3)
somma(15, 23)
print("")

#parametri arbitrari
print("parametri arbitrari")

def stampa_elenco(*elenco):
    for item in elenco:
        print(item)

stampa_elenco(1, 3, 1, 5, 67, 3, 45, 334)
stampa_elenco("rosso", "verde", "giallo", "blu")

print("")
def prestito(ammontare, giorni):
    # calcola l'ammontare degli interessi al 20%
    interesse = (ammontare * 0.2) * giorni
    totale = ammontare + interesse
    print(f"Il totale da restituire è {totale}")
    return totale

dovuto = prestito(10, 2)
print(f"Dovrai restituire {dovuto}")