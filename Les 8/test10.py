""" 
test10.py
Behoort bij paragraaf 8.7 een variabele binnen een functie.
Dit is een voorbeeld die je gebruikt in de 'hoofdcode', kan je wel gebruiken in de functie.
"""

B = 2
def mijn_functie():
    """Deze functie wijzigt de waarde van B door gebruik te maken van de 'global' keyword."""
    global B
    B = B + 10
    print("binnen: ", B)

print("buiten: ", B)
mijn_functie()
print("buiten: ", B)
