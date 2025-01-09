# Le Liste
print("Le liste")
frutti = ["mela", "banana", "pera", "mela"]
# aggiungere un elemento
frutti.append("ciliegia")

# modificare un elemento
frutti[1] = "kiwi"

# eliminare un elemento stringa
frutti.remove("pera")

#eliminare un elemento in base all'indice
frutti.pop(2)
print(frutti)

numeri = [12, 45, 67, 43, 23, 45, 5, 78]
print(numeri)
print("")

# Le tuple
print("LE TUPLE")
frutti = ("mela", "banana", "pera", "mela")
print(frutti)
print("")

# Gli insiemi o set
print("Gli insiemi o set")
frutti = {"mela", "banana", "pera", "mela"}
print(frutti)
numeri = {12, 45, 67, 43, 23, 45, 5, 78}
print(numeri)
# Unione, intersezione(elemento che hanno in comune) e differenze
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print("")
#I Dizionari
print("I Dizionari")
persona = {"nome" : "Alice",
           "età" : 25,
           "città" : "Roma",
           1 : "Alice"}
print(persona)
# Accesso ai valori tramite la chiave
print(persona["nome"])
# Aggiungere una nuova coppia di valori
persona["professione"] = "data engineer"
print(persona)
# Modificare il valore corrispondente ad una chiave
persona["età"] = 26
print(persona)
# Rimuovere una coppia di valori
persona.pop("città")
print(persona)

