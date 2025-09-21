def info(naam, leeftijd, in_dienst):
    if in_dienst:
        text_1 = "en nog altijd in dienst van onze firma."
    else:
        text_1 = "en niet meer bij ons in dienst."

    uitvoer = f"{naam} is {leeftijd} jaar oud {text_1}"
    return uitvoer

print(info("Harry", 54, True))
print(info("Magda", 73, False))