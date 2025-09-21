""" 
test8b.py
Dit is een voorbeeld dat je niet altijd argumenten hoeft door te geven.
behoort bij paragraaf 8.6 een functie met parameters.
Let op: ( tussen haakjes zijn PARAMETERS, Functie aanroepen van waarden noewmen we de waarden: ARGUMENTEN)
"""

def tel_op(a=1,b=2):
    return a + b
totaal = tel_op(20)
print(totaal)