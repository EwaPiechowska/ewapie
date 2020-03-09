#6. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.


# 000110
# 1*2*2+1*2*1=6
#
# 111111
# 1+2+4+8+16+32=63

print("podaj liczbę w formacie binarnym: ")
liczba = input()
wynik = int(liczba[0:1]) * pow(2,5) + int(liczba[1:2]) * pow(2,4) + int(liczba[2:3]) * pow(2,3) + \
        int(liczba[3:4]) * pow(2,2)+ int(liczba[4:5]) * pow(2,1) + int(liczba[-1]) * pow(2,0)



print(wynik)

# jak piszemy od nowej linii?!
