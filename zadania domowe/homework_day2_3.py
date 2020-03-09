#3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
print("Wzór na pole powierzchni koła to: P = πr^2")   # wyświetl wzór.....
print("wpisz długość promienia r: ")                  # wyświetl wpisz dlugość....
r = float(input())                                    # definiuje zmienną r która moge wpisać w konsoli i jest zameiniana na liczbę
pi = 3.14                                             # definiuje pi
#P = πr^2
P = pi * (r*r)                                        # definiuje wzór
print(P)                                              # wyświetlam wzór


