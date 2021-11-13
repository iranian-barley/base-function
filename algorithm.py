import numpy as np

integer = False

abfrage = input('Natuerliche Zahl [j/n]?: ')

if abfrage == 'j' or 'J':
    integer = True


if integer:
    eingabe = int(input('Bitte natuerliche Zahl hier eingeben: '))
    liste = list(map(int, str(eingabe)))  # Polynomkonstruktion abgeschlossen
else:
    vorkomma = int(input('Vorkommastelle eingeben: '))
    nachkomma = int(input('Nachkommastellen eingeben: '))
    vorliste = list(map(int, str(nachkomma)))
    vorliste.insert(0, vorkomma)
    negliste = [-x for x in vorliste]
    negliste.insert(0, 1)
    liste = negliste  # Polynomkonstruktion abgeschlossen

p = np.poly1d(liste)
roots = p.roots

print(roots)
