def dodaj (x, y) :
    #suma jest zmienna do ktorej przypisujemy wynik działania, float bo nie wiemy co wpisze uztkowik czy np. 1 czy 1.2
    suma = float(x) + float(y)
    return suma
wynik = dodaj (2, 7)
print(wynik)

#scope --> to jest to co widzimy jakby w jednej lini z góry na doł, a to co jest wciete np w funkcji juz nie jest
#dalej widocczny


suma = 15
def dodaj (x, y):
    suma = float(x) + float(y)
    return suma
print(suma)
#ponizej zwracamy cos z czym nic nie robimy
dodaj(2,7)
print(suma)

#ale jeśłi zrobimy tak:
suma = 15
def dodaj (x, y):
    suma = float(x) + float(y)
    return suma
print(suma)
#ze do dodaj przypisujemy sume  i wtedy wystwetli nam sie 15
suma = dodaj(2,7)
print(suma)
