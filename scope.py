# variabile globale
x = 10

def funzione1():
    print(x)

funzione1()
print(x)

def funzione2():
    # variabile locale
    y = 20
    print(y)

funzione2()
# print(y)

# variabile globale
z = 30
def funzione3():
    # variabile locale
    z = 40
    print(z)

print(z) # output 30
funzione3() # output 40
print(z) # output 30

a = 50
def funzione4():
    global a
    a += 10

print(a) # output 50
funzione4() # viene modificato il valore di a globale
print(a) # output 60
funzione4()
funzione4()
print(a) # output 80
a = 30
print(a) # output 30
funzione4()
print(a) # output 40

def funzioneEsterna():
    b = "originale"

    def funzioneInterna():
        c = "local"
        nonlocal b
        b = "modificata"

    print(b)
    funzioneInterna()
    print(b)

funzioneEsterna()
# print(b)
# print(c)
