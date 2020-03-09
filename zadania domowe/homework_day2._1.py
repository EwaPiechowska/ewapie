#1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)

print("Wzór na przeliczanie stopni F na C wygląda tak: F = (32+9) / 5* (C)")
print("wpisz stopnie w C: ")
C = float(input())
#deklaruje zmienną C,input pozwala wprowadzić liczbe, a float konwertuje to co wpisze
#użytkownik do liczby
F = (32+9) / 5* (C)
print ("F = " + str(F))




