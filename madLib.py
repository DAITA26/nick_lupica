# Titolo del Mad Libs
print("""Questo è un esempio del gioco Mad Libs!
Riempi gli spazi vuoti per creare una storia divertente.""")
# Chiedi input all'utente
nome = input("Inserisci un nome: ")
luogo = input("Inserisci un luogo: ")
animale = input("Inserisci un animale: ")
cibo = input("Inserisci un cibo: ")
azione = input("Inserisci un'azione (verbo all'infinto): ")
# Costruisci la storia
storia = f"""Un giorno, {nome} decise di andare a {luogo}.
Lungo il cammino, incontrò un {animale} che sembrava molto
affamato.
Così, {nome} decise di condividere un po' di {cibo} con il
{animale}.
Inaspettatamente, il {animale} iniziò a {azione} senza sosta!
"""
# Stampa la storia completa
print("\nEcco la tua storia:")
print(storia)