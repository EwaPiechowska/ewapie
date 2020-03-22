#3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)

print("Wzór na pole powierzchni koła to: P = πr^2")
print("wpisz długość promienia r: ")
try:
    r = float(input())
    pi = 3.14
    P = pi * (r * r)
    print(P)
except ValueError:
    print('błędna wartość podana przez użytkownika')