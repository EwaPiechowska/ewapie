#Zadanko na prywatne pokoje. Robimy funkcję która zlicza do pliku ilość jej wywołań. Pamiętajmy że plik ze statystykami przy pierwszym uruchomieniu nie istnieje a przy kolejnym po prostu podbijamy w nim licznik.
def licznik():
    try:

        with open ('licznik.txt', 'r+') as plik:
            #musimy zrzutowac bo tutaj jest string, a wykonujemy zadania matematyczne
            ilosc_uruchomien = (plik.read())
            if ilosc_uruchomien == '':
                ilosc_uruchomien = 1
            else:
                ilosc_uruchomien = int(ilosc_uruchomien+1)
            #zapisuje wartośc do pliku
            #i jeszcze zapisujemy zeby kursos szedł n apoczatek
            plik.seek(0)
            plik.write(str(ilosc_uruchomien))
            print(ilosc_uruchomien)

    except FileNotFoundError:
        with open ('licznik.txt', 'w') as plik:
            plik.write('1')
            print("1")
licznik()
