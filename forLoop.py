"""
parola = "python"

for lettera in parola:
    print(lettera)

parola = input("python")

for lettera in parola:
    print(lettera)


parola = input("python")

for x in parola:
    maiuscola = x.upper()
    print(x + "aggiungo una sringa a caso")
"""

for numero in range(5):
    print(numero)

for numero in range(1, 11):
    print(numero)

for numero in range(1, 20, 2):
    print(numero)

for numero in range (1, 32, 1):
    print(f"{numero} dicembre")

for numero in range (31, 0, -1):
    print(f"{numero} dicembre")

for numero in reversed(range(31, 0, -7)):
    print(f"{numero} dicembre")



for n in range(11):
    if n == 5:
        print("break in corrispondenza del numero 5")
        break

    print(n)
else:
    print("il ciclo for è finito")





for n in range(11):
    if n == 5:
        print("salto in corrispondenza del numero 5")
        continue

    print(n)
else:
    print("il ciclo for è finito")
