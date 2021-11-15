import numpy as np


def phi(eingabe):
    eingabe = str(eingabe)
    check = len(eingabe.partition('.')[0])
    res = ''.join(filter(lambda i: i.isdigit(), eingabe))
    liste = list(map(int, str(res)))
    liste[check - 2] = liste[check - 2] - 1

    if check == 1:
        liste.insert(0, -1)
        liste[len(liste) - 1] = liste[len(liste) - 1] + 1  # warum wird letztes Element -1???

    p = np.poly1d(liste)
    roots = p.roots

    print(roots)


phi(333)  # Wert hier eingeben
