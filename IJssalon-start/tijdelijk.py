from helper import decodeer

def print_aanbieding():
        prijzen = {
            "aardbei": 3,
            "vanille": 4,
            "chocola": 5
        }

        aanbieding = prijzen["aardbei"] * 0.8

        reclame_tekst = f"vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding}!"

        reclame_tekst2 = reclame_tekst[:63]

        reclame_tekst3 = reclame_tekst2.upper()

        reclame_tekst = reclame_tekst3.split()

        for el in reclame_tekst:
            if len(el) > 5:
                print (el.upper())
            else:
                print(el.lower())

decodeer("Aanbieding")
print_aanbieding()