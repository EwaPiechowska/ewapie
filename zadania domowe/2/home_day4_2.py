# 2) Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
#    Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.


wysokosc = 4
szerokosc = 3

poczatek_koniec = '+' + ('-' * szerokosc) + '+'
srodek = "|" + (' ' * szerokosc) + "|\n"

print(poczatek_koniec)
print(wysokosc * srodek, end='')
print(poczatek_koniec)