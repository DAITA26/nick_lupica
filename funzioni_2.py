# import
# variabili (globali)
# funzioni
# codice

def saluta1():
    print("Ciao")

def saluta2(nome):
    print(f"Ciao {nome}")

def saluta(nome = ""):
    print(f"Ciao {nome}")

saluta2("Alice")
saluta1()
saluta2("Sabrina")
saluta()
saluta("Antonio")

def frase(verbo, aggettivo, nome, articolo):
    print(f"{articolo} {nome} {aggettivo} {verbo}")

frase(aggettivo="rossa", nome="mela", verbo="sta sull'albero", articolo="la")

def differenza(a, b):
    diff = a - b
    print(f"Il valore della differenza è {diff}")

differenza(b=3, a=5)

def stampa_elenco(*args):
    for item in args:
        print(item)

stampa_elenco("rosso", "verde", "blu", "giallo")

def stampa_elenco(**dizionario):
    for chiave, valore in dizionario.items():
        print(f"{chiave}: {valore}")

stampa_elenco(a="rosso", b="verde", c="blu")

def differenzaReturn(a, b):
    diff = a - b
    print(f"Il valore della differenza è {diff}")
    return diff
    print("Istruzione dopo il return")

diff = differenzaReturn(40, 2)
# voglio utilizzare il valore diff qui
print(diff)

def cacolaSommaDifferenza(a = 10, b = 5):
    sum = a + b
    diff = a - b
    return sum, diff

pippo, pluto = cacolaSommaDifferenza(b = 2)
print(pippo)
print(pluto)

def funzioneEsterna():
    print("Sei nella funzione esterna!")

    # questa è la riga 2 di un nuovo file.py
    def funzioneInterna():
        print("Sei nella funzione interna!")

    funzioneInterna()

funzioneEsterna()