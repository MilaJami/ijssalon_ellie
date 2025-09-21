""" 
test9.py
Behoort bij paragraaf 8.7 een variabele binnen een functie.
Het klopt dat er een foutmelding is omdat de regels niet zijn ingesprongen.
Dit is een voorbeeld die je definieert binnen in een functie, daarbuiten kan je deze niet meer gebruiken.
"""
totaal = 0

def mijn_functie():
    a = 2

totaal = totaal + a
print(totaal)