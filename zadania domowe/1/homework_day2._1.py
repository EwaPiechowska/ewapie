#1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)

print("Wzór na przeliczanie stopni F na C wygląda tak: F = (32+9) / 5* (C)")
print("wpisz stopnie w C: ")
C = float(input())
#deklaruje zmienną C,input pozwala wprowadzić liczbe, a float konwertuje to co wpisze
#użytkownik do liczby
F = (32+9) / 5* (C)
print ("F = " + str(F))



# Od dziś też będę zwaracał uwagę na to czy nie tylko kod działa ale:
# a) czy składanie jest ładna i zgodna ze standardami
# b) czy kod jest zabezpieczony przed wprowadzaniem niepoprawnych danych
#    (np jeśli prosimy o liczbę a dostaniemy znaki poprośmy użytkownika o podanie danej jeszcze raz)
# c) czy metody są udokumentowane a co ciekawsze fragmentu kodu opatrzone komentarzem.
# d) parametryzacja, im większy wpływ na program i jakieś parametry tym fajniej :)
# e) wydzielanie uniwersalnych fragmentów kodów do osobnych funckji


print("Wzór na przeliczanie stopni F na C wygląda tak: F = (32+9) / 5* (C)")
print("wpisz stopnie w C: ")
stopnie_c = input()



zmienna = 1
typ = type(zmienna)
print(typ)
