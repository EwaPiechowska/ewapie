#6. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.#6. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.


print("podaj liczbę w formacie binarnym: ")
liczba = input()

def bin2dec(od, do, potega):
    return int(liczba[od:do]) * pow (2, potega)

wynik = bin2dec(0,1,5) + bin2dec(1,2,4) + bin2dec(2,3,3) + bin2dec(3,4,2) + bin2dec(4,5,1) + bin2dec(5,6,0)
print(wynik)







