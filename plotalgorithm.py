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
    return roots[0]


x = 0
y = [0]
z = [0]

while x <= 100:
    var = phi(x)
    y.append(var)
    z.append(x)
    x = x + 0.1

plt.plot(z, y)
plt.title('Reelle Lösung für 0 < x < 10000')
plt.grid()
plt.show()
