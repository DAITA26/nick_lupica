class ComuneDiNascita:

    def __init__(self, luogo_nascita):
        self.luogo_nascita = str(luogo_nascita).upper()


    def codice_catastale(self):

        codici_catastali = {
            "ROMA": "H501",
            "MILANO": "F205",
            "NAPOLI": "F839",
            "TORINO": "L219",
            "FIRENZE": "D612",
            "BOLOGNA": "A944",
            "VENEZIA": "L736",
            "GENOVA": "D969",
            "PALERMO": "G273",
            "CATANIA": "C351",
            "VERONA": "L781",
            "TRIESTE": "L424",
            "BARI": "A662",
            "CAGLIARI": "B354",
            "PERUGIA": "G478",
            "ANCONA": "A271",
            "TRENTO": "L378",
            "BOLZANO": "A952",
            "PARMA": "G337",
            "REGGIO EMILIA": "H223",
            "PESCARA": "G482",
            "RIMINI": "H294",
            "SALERNO": "H703",
            "MESSINA": "F158",
            "LIVORNO": "E625",
            "PADOVA": "G224",
            "TARANTO": "L049",
            "LECCE": "E506",
            "MODENA": "F257",
            "UDINE": "L483",
            "SIRACUSA": "I754",
            "AOSTA": "A326",
            "SASSARI": "I452",
            "FERRARA": "D548",
            "BERGAMO": "A794",
            "MONZA": "F704",
            "COMO": "C933",
            "LUCCA": "E715",
            "PISA": "G702",
            "RAVENNA": "H199",
            "TREVISO": "L407",
            "VICENZA": "L840",
            "CREMONA": "D150",
            "MANTOVA": "E897",
            "AREZZO": "A390",
            "SIENA": "I726",
            "GROSSETO": "E202",
            "PISTOIA": "G713"
        }
        codici_catastali_esteri = {
            "ALBANIA": "Z100",
            "ALGERIA": "Z101",
            "ANDORRA": "Z102",
            "ANGOLA": "Z103",
            "ARGENTINA": "Z104",
            "ARMENIA": "Z105",
            "AUSTRALIA": "Z106",
            "AUSTRIA": "Z107",
            "AZERBAIGIAN": "Z108",
            "BANGLADESH": "Z109",
            "BELGIO": "Z110",
            "BIELORUSSIA": "Z111",
            "BOLIVIA": "Z112",
            "BOSNIA-ERZEGOVINA": "Z113",
            "BRASILE": "Z114",
            "BULGARIA": "Z115",
            "CANADA": "Z116",
            "CINA": "Z210",
            "COLOMBIA": "Z118",
            "COREA DEL NORD": "Z119",
            "COREA DEL SUD": "Z120",
            "COSTA D'AVORIO": "Z121",
            "CROAZIA": "Z122",
            "CUBA": "Z123",
            "DANIMARCA": "Z124",
            "EGITTO": "Z125",
            "EMIRATI ARABI UNITI": "Z126",
            "ECUADOR": "Z127",
            "ESTONIA": "Z128",
            "ETIOPIA": "Z129",
            "FILIPPINE": "Z130",
            "FINLANDIA": "Z131",
            "FRANCIA": "Z132",
            "GERMANIA": "Z133",
            "GIAPPONE": "Z250",
            "GIORDANIA": "Z135",
            "GRECIA": "Z136",
            "INDIA": "Z260",
            "INDONESIA": "Z138",
            "IRAN": "Z139",
            "IRAQ": "Z140",
            "IRLANDA": "Z141",
            "ISLANDA": "Z142",
            "ISRAELE": "Z143",
            "KAZAKISTAN": "Z144",
            "KENYA": "Z145",
            "KIRGHIZISTAN": "Z146",
            "LIBANO": "Z147",
            "LIBIA": "Z148",
            "LIECHTENSTEIN": "Z149",
            "LITUANIA": "Z150",
            "LUSSEMBURGO": "Z151",
            "MACEDONIA": "Z152",
            "MALAYSIA": "Z153",
            "MALTA": "Z154",
            "MAROCCO": "Z330",
            "MESSICO": "Z156",
            "MONACO": "Z157",
            "MONGOLIA": "Z158",
            "MONTENEGRO": "Z159",
            "NORVEGIA": "Z160",
            "NUOVA ZELANDA": "Z161",
            "OLANDA (PAESI BASSI)": "Z162",
            "PAKISTAN": "Z163",
            "POLONIA": "Z164",
            "PORTOGALLO": "Z165",
            "REGNO UNITO": "Z166",
            "REPUBBLICA CECA": "Z167",
            "REPUBBLICA DOMINICANA": "Z168",
            "ROMANIA": "Z169",
            "RUSSIA": "Z170",
            "SERBIA": "Z171",
            "SINGAPORE": "Z172",
            "SLOVACCHIA": "Z173",
            "SLOVENIA": "Z174",
            "SPAGNA": "Z175",
            "STATI UNITI": "Z404",
            "SVEZIA": "Z177",
            "SVIZZERA": "Z178",
            "THAILANDIA": "Z179",
            "TUNISIA": "Z180",
            "TURCHIA": "Z181",
            "UCRAINA": "Z182",
            "UNGHERIA": "Z183",
            "URUGUAY": "Z184",
            "UZBEKISTAN": "Z185",
            "VENEZUELA": "Z186",
            "VIETNAM": "Z187",
            "ZIMBABWE": "Z188"
        }

        try:
            if self.luogo_nascita in codici_catastali:
                return codici_catastali[self.luogo_nascita]
            elif self.luogo_nascita in codici_catastali_esteri:
                return codici_catastali_esteri[self.luogo_nascita]
            else:
                raise KeyError(f"Errore: il comune {self.luogo_nascita} non è registrato.")
        except KeyError as e:
            return str(e)


if __name__ == '__main__':
    obj = ComuneDiNascita("Messina")
    print(obj.codice_catastale())

    obj1 = ComuneDiNascita("messina")
    print(obj1.codice_catastale())

    obj2 = ComuneDiNascita("MAROCCO")
    print(obj2.codice_catastale())

    obj3 = ComuneDiNascita("Marocco")
    print(obj3.codice_catastale())

    obj4 = ComuneDiNascita("brolo")
    print(obj4.codice_catastale())

    obj5 = ComuneDiNascita(22)
    print(obj5.codice_catastale())
