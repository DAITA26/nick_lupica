# La classe DataDiNascita dovrà gestire:
# la separazione della stringa inserita in input in giorno, mese e anno
class DataDiNascita:

    def __init__(self, anno, mese, giorno):
        self.anno = str(anno)
        self.mese = str(mese)
        self.giorno = int(giorno)

# La generazione del numero a 2 cifre che identifica l'anno di nascita
    def gestisci_anno(self):
        return self.anno[-2:] if len(self.anno) == 4 else "Immetti un anno valido"

# La conversione del mese di nascita in lettera dell'alfabeto
    def gestisci_mese(self):
        mesi = {
            1: 'A', 2: 'B', 3: 'C',
            4: 'D', 5: 'E', 6: 'H',
            7: 'L', 8: 'M', 9: 'P',
            10: 'R', 11: 'S', 12: 'T',
            "01": 'A', "02": 'B', "03": 'C',
            "04": 'D', "05": 'E', "06": 'H',
            "07": 'L', "08": 'M', "09": 'P',
            "10": 'R', "11": 'S', "12": 'T',
            'gennaio': 'A', 'febbraio': 'B', 'marzo': 'C', 'aprile': 'D', 'maggio': 'E', 'giugno': 'H',
            'luglio': 'L', 'agosto': 'M', 'settembre': 'P', 'ottobre': 'R', 'novembre': 'S', 'dicembre': 'T'
        }
        for chiave, valore in mesi.items():
            if self.mese == chiave or str(self.mese).upper() == str(chiave).upper():
                return valore
        return "Mese non valido"

# Il calcolo del giorno di nascita in base al sesso
    def gestisci_giorno_sesso(self, sesso):

        if sesso == "M" or sesso == "m":
            if 9 < self.giorno <= 31:
                return str(self.giorno)
            elif self.giorno <= 9:
                return "0" + str(self.giorno)
        elif sesso == "F" or sesso == "f":
            if self.giorno <= 31:
                return str(self.giorno + 40)
        else:
            print("Digita un giorno valido")

# Stampa la concatenazione di anno, mese e giorno
    def stampa_codice(self, sesso):
        return self.gestisci_anno() + self.gestisci_mese() + self.gestisci_giorno_sesso(sesso)


if __name__ == '__main__':
    """
    anno_nascita = int(input("Digita il tuo anno di nascita ").strip().isdigit())
    mese_nascita = input("Digita il tuo mese di nascita ").strip()
    giorno_nascita = int(input("Digita il giorno della tua nascita ").strip().isdigit())
    
    obj = DataDiNascita(anno_nascita, mese_nascita, giorno_nascita)
    print(obj.stampa_codice("F"))  # Output: 63T44
    print(obj.stampa_codice("M"))  # Output: 63T04
    """

    obj1 = DataDiNascita(1999, "marzo", "04")
    obj2 = DataDiNascita(9, "03", 4)
    obj3 = DataDiNascita(199, 3, "09")
    obj4 = DataDiNascita("1999", 3, 9)

    print(obj1.stampa_codice("M"))
    print(obj2.stampa_codice("m"))
    print(obj3.stampa_codice("F"))
    print(obj4.stampa_codice("f"))
    print("")

    print(obj1.gestisci_giorno_sesso("M"))
    print(obj2.gestisci_giorno_sesso("m"))
    print(obj3.gestisci_giorno_sesso("F"))
    print(obj4.gestisci_giorno_sesso("f"))
    print("")

    print(obj1.gestisci_mese())
    print(obj2.gestisci_mese())
    print(obj3.gestisci_mese())
    print(obj4.gestisci_mese())
