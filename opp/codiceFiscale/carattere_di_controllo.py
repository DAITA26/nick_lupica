# Terminata la prima parte dell'esercizio, sarà possibile usare la stringa
# fin qui generata per calcolare il carattere di controllo, la cui logica
# dovrebbe essere inserita in una ulteriore classe CarattereDiControllo

from stringa_di_testo import StringaDiTesto
from data_di_nascita import DataDiNascita

def unisci_codice_fiscale(nome, cognome, anno, mese, giorno, sesso):
    stringa_testo = StringaDiTesto(nome, cognome)

    data_nascita = DataDiNascita(anno, mese, giorno)

    codice_fiscale = stringa_testo.genera_codice() + data_nascita.stampa_codice(sesso)

    return codice_fiscale

nome = input("Digita il tuo nome ").strip()
cognome = input("Digita il tuo cognome ").strip()
anno_nascita = int(input("Digita il tuo anno di nascita ").strip())
mese_nascita = input("Digita il tuo mese di nascita ").strip()
giorno_nascita = int(input("Digita il giorno della tua nascita ").strip())
sesso = input("Digita il tuo sesso (M o F) ").strip()

# Stampa CF
print(unisci_codice_fiscale(nome, cognome, anno_nascita, mese_nascita, giorno_nascita, sesso))