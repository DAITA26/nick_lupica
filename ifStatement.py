# 18/12/24
# Esercizio costrutto if (mutualmente esclusivo)

pippo = 8

if pippo >= 7:
    print("pippo vale almeno 7")
    print("ciao! non mi hanno indentato bene!!")
elif pippo == 8:
    print("pippo vale 8")
elif pippo == 6:
    print("pippo vale 6")
else:
    print("pippo NON vale 6 e non è maggiore o uguale a 7")

print("ciao! sono la riga 12!!!")

# Logica booleana
if True:
    print("questo if vale sempre!")

if False:
    print("questo if non vale mai!")

flag = True

if flag:
    print("questo if funziona solo quando flag vale True!")

if not flag:
    print("questo if funziona solo quando flag vale False!")

# verificare se il numero è un multiplo di 2 oppure un multiplo di 3 o di 5
numero = int(input("inserisci un numero"))

if numero % 2 == 0:
    print(f"{numero} è un multiplo di 2")
if numero % 3 == 0:
    print(f"{numero} è un multiplo di 3")
if numero % 5 == 0:
    print(f"{numero} è un multiplo di 5")
if numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0:
    print(f"{numero} non è multiplo di 3 nè di 2 nè di 5")

# operatore modulo %: resto della divisione per INTERI
# DRY -> don't repeat yourself

# Approccio 2: utilizzo dei booleani
print("""
Approccio 2 - utilizzo una variabile booleana
""")
flag = False

if numero % 2 == 0:
    print(f"{numero} è un multiplo di 2")
    flag = True
if numero % 3 == 0:
    print(f"{numero} è un multiplo di 3")
    flag = True
if numero % 4 == 0:
    print(f"{numero} è un multiplo di 4")
    #flag = True
if numero % 5 == 0:
    print(f"{numero} è un multiplo di 5")
    flag = True
if numero % 7 == 0:
    print(f"{numero} è un multiplo di 7")
    flag = True
# si legge " se la variabile flag è falsa, allora esegui il blocco di codice
if not flag:
    print(f"{numero} NON è un multiplo di 2,3,4 o 5 o 7")




num = 5

if not num:
    print("la condizione è falsa")
else:
    print("la condizione è vera")