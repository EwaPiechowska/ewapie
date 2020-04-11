# 3) Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
# wydając ich jak najmniej.
nazwa = 'przeliczanie nominałów '
def funkcja():
    lista_nominalow = [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    print("podaj kwotę: ")
    kwota = float(input())
    i = 0
    while kwota > 0.001:
        if kwota >= lista_nominalow[i]:
            print (lista_nominalow[i])
            kwota = kwota - lista_nominalow[i]
        else:
            i=i+1
