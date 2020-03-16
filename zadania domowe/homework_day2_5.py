wysokosc = 4
szerokosc = 3

poczatek_koniec = '+' + ('-' * szerokosc) + '+'
srodek = "|" + (' ' * szerokosc) + "|\n"

print(poczatek_koniec)
print(wysokosc * srodek, end='')
print(poczatek_koniec)


# print(poczatek_koniec)
# print(wysokosc * srodek + poczatek_koniec)