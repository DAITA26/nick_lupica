# 17/12/24
# Esercizi su metodi e funzioni delle stringhe
nome = input("Come ti chiami? ")
cognome = input("Il tuo cognome? ")

# carattere di escape - \


# stampa numero di carartteri
print(len(nome))

# prima occorrenza di una substring
print(nome.find("ab"))

# quando non è presente stampa -1
print(nome.find("ar"))

# prima occorrenza di un singolo carattere
print(nome.find("b"))

# ultima occorrenza di un singolo carattere
print(nome.rfind("a"))

# ultima occorrenza di una substring
print(nome.rfind("na"))

# converte tutti i caratteri in Maiuscolo
print(nome.upper())

# converte tutti i caratteri in minuscolo
print(nome.lower())

# converte l'iniziale in maiuscolo
print(nome.capitalize())
print(nome.capitalize() + " " + cognome.capitalize())

# controlla se sono tutte lettere
print(nome.isalpha())

# controlla se sono tutti numeri
print(nome.isdigit())

# controlla substring iniziale
print(nome.startswith("S"))

# controlla substring finale
print(nome.endswith("na"))

# controlla il numero di occorrenze di una subtring
print(nome.count("a"))

# controlla il numero di spazi
print(nome.count(" "))

# sostituisce una substring con un'altra
print(nome.replace("a", "o"))

# rimuove gli spazi iniziali e finali di una stringa
print(nome.strip())

# rimuove un certo carattere all'inizio e alla fine di una stringa
print(nome.strip("a"))

print(help(str))
