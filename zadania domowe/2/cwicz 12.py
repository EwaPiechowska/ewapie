# 12) Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
#    Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
#    A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)

def funkcja(lista):
    szerokosc = 30

    poczatek_koniec = '+'
    for slowo in lista:
        poczatek_koniec += ('-' * szerokosc) + '+'
    srodek='|'
    for slowo in lista:
        srodek += slowo + (' ' * (30 - len(slowo))) + "|"

    print(poczatek_koniec)
    print(srodek)
    print(poczatek_koniec)

name = "'col1','col2','col3'"
lista = name.split(",")
funkcja(lista)








