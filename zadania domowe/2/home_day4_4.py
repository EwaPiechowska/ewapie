# 4) Program rysujący piramidę o określonej wysokości, np dla 3

wysokosc = int(input())
#i numer wiersza wpisany przez uzytkownika
#wiersze indeksują się od 0
n=1

for i in range (wysokosc):
    print(ilosc_spacji)
    ilosc_spacji = wysokosc - i - 1
    print(' ' * ilosc_spacji + '#' * n + ' ')
    n= n+2
