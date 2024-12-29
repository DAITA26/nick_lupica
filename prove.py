'''# Esempio valutazione input
print("""
Esempio validazione input: l'utente inserisce la password finché non la azzecca
""")
password = ""

while password != "laMiaPassword":
    password = input("inserisci la tua password ").strip()

print("accesso consentito")'''

# Esempio valutazione input
print("""
Esempio validazione input: l'utente inserisce la password sbagliata al massimo 3 volte
""")
password = ""
tentativi = 0


while password != "passwordCorretta" and tentativi < 3:
    #qui parte il tentativo di inserire la pw corretta
    #passo 1 - incrementare i tentativi
    tentativi += 1

    mexTry = f"Ti sono rimasti {4 - tentativi} tentativi "
    mexLast = "Ultimo tentativo rimasto!"

    mex = mexTry if tentativi < 3 else mexLast
    print(mex)
    password = input("inserisci la password: ").strip()
    risultato = print("Accesso consentito") if password == "passwordCorretta" else print("Accesso non consentito")
else:
    print("il ciclo è finito")

print("il ciclo è finito anche qui")