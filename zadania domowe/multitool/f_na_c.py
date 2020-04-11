
# Od dziś też będę zwaracał uwagę na to czy nie tylko kod działa ale:
# a) czy składanie jest ładna i zgodna ze standardami
# b) czy kod jest zabezpieczony przed wprowadzaniem niepoprawnych danych
#    (np jeśli prosimy o liczbę a dostaniemy znaki poprośmy użytkownika o podanie danej jeszcze raz)
# c) czy metody są udokumentowane a co ciekawsze fragmentu kodu opatrzone komentarzem.
# d) parametryzacja, im większy wpływ na program i jakieś parametry tym fajniej :)
# e) wydzielanie uniwersalnych fragmentów kodów do osobnych funckji
nazwa = 'Przeliczanie stopni Celsjusza na Fahrenheita'
def funkcja():
    print("Wzór na przeliczanie stopni F na C wygląda tak: F = (32+9) / 5* (C)")
    print("wpisz stopnie w C: ")
    #w przypadku błednego typu danych, program pokazuje komunikat: podaj liczbę!
    try:
        stopnie_c = float(input())
        stopnie_f = (32 + 9) / 5 * float(stopnie_c)
        print("F = " + str(stopnie_f))
    except ValueError:
        print("Podaj liczbę!")









