#7. Napisz program do rozpoznawania czy podane liczba jest parzysta czy nie.

nazwa = 'program do rozpoznawania czy podane liczba jest parzysta czy nie'
def parzyste_nieparzyste():
    print("Podaj liczbę: ")

#definiuje liczbę jako integer i mogę ją sobie wpisać z klawiatury
    liczba = int(input())
# pokazuje mi reszte z dzielenia przez 2
    print('reszta z dzielenia: %d ' % (liczba % 2))
    if liczba % 2 == 0:
        print("liczba jest parzysta!")
    else:
        print("liczba jest nieparzysta!")
