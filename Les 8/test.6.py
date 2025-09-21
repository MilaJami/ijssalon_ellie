b = 2
def mijn_functie():
    global b
    b = b + 10
    print("binnen: ", b)

print("buiten: ", b)
mijn_functie()
print("buiten: ", b)
# Dit is een voorbeeld van het gebruik van de 'global' keyword in Python. zie les 8.8 NHA boek.