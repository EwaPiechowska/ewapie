def czworokat():
    print('podaj wysokość: ')
    wysokosc = int(input())
    print('podaj szerokosc: ')
    szerokosc = int(input())
    poczatek_koniec = '+' + ('-' * szerokosc) + '+'
    srodek = "|" + (' ' * szerokosc) + "|\n"
    print(poczatek_koniec)
    print(wysokosc * srodek, end='')
    print(poczatek_koniec)
czworokat()

# print(poczatek_koniec)
# print(wysokosc * srodek + poczatek_koniec)