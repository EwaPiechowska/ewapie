#8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub
nazwa = 'Program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub'
def podzielne_przez_3lub5lub7():
    print("Podaj liczbę: ")

#definiuje liczbę jako integer i mogę ją sobie wpisać z klawiatury
    liczba = int(input())
#wstawiam zmienną logiczną
#zakłądamy z góry ze czegokolwiek nie napiszemy jest niepodzielne
#dopóki któryś warunek z poniższych nie zostanie spełniony
    podzielna = True
#jeśli reszta z dzielenia bedzie równa 0 to warunek niepodzielene=true nie ma znaczenia
#bo zmieniam warunek na false
    def czy_podzielna(x):
        if liczba % x == 0:
            print("liczba jest podzielna przez %s" % x)
            return True
        else:
            print("liczba jest niepodzielna %s" % x)
            return False


    y=3
    for x in range(3):
        czy_podzielna(y)
        y += 2

    if not podzielna:
        print("liczba jest niepodzielna przez 3 lub 5 lub 7")

