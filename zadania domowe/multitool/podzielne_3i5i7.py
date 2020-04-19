#9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
nazwa = 'Program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7'
#definiuje liczbę jako integer i mogę ją sobie wpisać z klawiatury
def funkcja():
    try:
        print('podaj liczbe: ')
        liczba = int(input())
        if liczba % 3 == 0 and liczba % 5 == 0 and liczba % 7 == 0:
             print("liczba jest podzielna przez 3 i 5 i 7!")
        else:
             print("liczba jest niepodzielna przez 3 i 5 i 7")
    except ValueError:
        print('podaj liczbę!')



