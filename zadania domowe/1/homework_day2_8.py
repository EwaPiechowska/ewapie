#8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
print("Podaj liczbę: ")

#definiuje liczbę jako integer i mogę ją sobie wpisać z klawiatury
liczba = int(input())
#print(liczba % 3 )

# if liczba % 3 == 0 or liczba % 5 == 0 or liczba % 7 == 0 :
#     print("liczba jest podzielna przez 3 lub 5 lub 7!")
# else:
#     print("liczba jest niepodzielna przez 3 lub 5 lub 7")


#wstawiam zmienną logiczną
#zakłądamy z góry ze czegokolwiek nie napiszemy jest niepodzielne
#dopóki któryś warunek z poniższych nie zostanie spełniony
niepodzielne = True
#jeśli reszta z dzielenia bedzie równa 0 to warunek niepodzielene=true nie ma znaczenia
#bo zmieniam warunek na false
if liczba % 3 == 0:
    print("liczba jest podzielna przez 3")
    niepodzielne = False
if liczba % 5 == 0:
    print("liczba jest podzielna przez 5")
    niepodzielne = False
if liczba % 7 == 0:
    print("liczba jest podzielna przez 7")
    niepodzielne = False
if niepodzielne:
    print("liczba jest niepodzielna przez 3 lub 5 lub 7")