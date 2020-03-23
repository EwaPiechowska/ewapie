#4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
# zdanie = "ala ma kota"
# print(zdanie[1:3])

def pierwsza_ostatnia_cyfra():
    print("Podaj liczbę: ")
    liczba = input()
    print('pierwsza liczba to: %s ' % liczba[0:1])
    print('ostatnia liczba to: %s ' % liczba[-1])    #od konca leci
pierwsza_ostatnia_cyfra()

