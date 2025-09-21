""" 
test7.py
Dit is een voorbeeld van een functie die informatie over een persoon geeft.
"""


def info(naam: str, leeftijd: int, in_dienst: bool) -> str:
    """Deze functie geeft informatie over een persoon."""
    if in_dienst:
        text_1 = "en nog altijd in dienst van onze firmma."
    else:
        text_1 = "en niet meer bij ons in dienst."

    uitvoer = f"Beste {naam}, u bent {leeftijd} jaar {text_1}"
    return uitvoer
print(info("Harry", 54, True))
print(info("Magda", 73, False))

# Dit is een voorbeeld van het gebruik van de 'global' keyword in Python. zie les 8.8 NHA boek.
