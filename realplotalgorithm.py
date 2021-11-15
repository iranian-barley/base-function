import numpy as np
import matplotlib.pyplot as plt


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

    # print(roots)

    if roots[0].imag < 0.01: # Großzügig, eigentlich gleich Null setzen
        return roots[0]


a = 0
y = [0]
z = [0]

while a <= 100:
    var = phi(a)
    y.append(var)
    z.append(a)
    a = a + 0.1


plt.plot(z, y)
plt.title('Reelle Lösung für 10 < x < 100')
plt.grid()
plt.show()
