# #pobieranie danych od uzytkownika
# #zmienne:
# imie = input("Jak masz na imie? ")
# nazwisko = "Piechowska"
# print(imie + 2*'\n'+nazwisko)


# # "ala ma kota".capitalize()
# # zdanie="ala ma kota"
# # zdanie.capitalize()
# wynik_dzialania = imie.capitalize()   #funkcja .capitalized zmienia na dużą literę
# print(wynik_dzialania)


# liczba_1 = 123
# # liczba_2 = 4.5
# # liczba_3 = int("1")
# # print(liczba_1 / liczba_3)
# #
# # zmienna_1 = "ala ma"
# # zmienna_2 = "kota"
# # print(zmienna_1 + zmienna_2)

# sciezka_do_pilpitu = "c:\\documents\\nowy folder\\tatry"
#sa dwa \\ bo nie moze byc \n i \t bo wtedy robia sie spacje
# #zeby sie nie przejmować tymi 2 \\ to piszemy
# sciezka_do_pilpitu = r"c:\\documents\nowy folder\tatry"
# print(sciezka_do_pilpitu)

#funkcja type pokazuje nam jakiego typu jest zmienna
# zmienna = 1
# typ = type(zmienna)
# print(typ)

# zmienna = input("wpisz coś: ")
# typ = type(zmienna)
# print(typ)

# program ktory zadaje dwa pytania
# podaj liczbe 1
# podaj liczbe 2
# suma twoich liczb to


#ZADANKO
# print("Podaj liczbę pierwszą:  ")
# print("Podaj liczbę drugą:   ")
# print("suma Twoich liczb to:  ")
#mam zmienne wartosci
# wartosc_1 = input("liczba_1: ")
# wartosc_2 = input("liczba_2: ")
# liczba_1 = float(wartosc_1)   #jak ułamek to float, jak całe to int
# liczba_2 = float(wartosc_2)
# print(liczba_1 * liczba_2)


          #01234567890
# zdanie = "ala ma kota"
# print(zdanie[1:3])   # od pierwszego znaku (łącznie z pierwszym znakiem) do 3 znaku bez 3(nawias otwarty - nie liczy się ta pzycja)
# print(zdanie[1:8:2]) #czyli ide od pierwszego co dwa do 8 znaku: czyli: l ak    3 paramter to skok

# zdanie= "Ala ma kota!"
# print (zdanie [1:8])
# uciete_zdanie = zdanie[1:8:5]
# print(uciete_zdanie)
# print(len(uciete_zdanie)
# print(zdanie[-1])
# dlugosc = len(zdanie)
# print(zdanie[dlugosc-1])


#warunki
zdanie = "Ala ma kota!"
ostatni_znak = zdanie[-1]
if ostatni_znak == '!':
    print('nie krzycz na mnie')
else:
    print('dziękuje')