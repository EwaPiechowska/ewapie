#2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
nazwa = 'Przeliczanie stopni Fahrenheita na Celsjusza'
def funkcja():
    print("Wzór na przeliczanie stopni F na C wygląda tak: c = (F-32)/1.8")
    print("wpisz stopnie w F: ")
    #w przypadku błednego typu danych, program pokazuje komunikat: podaj liczbę!
    try:
        stopnie_f = float(input())
        stopnie_c = (stopnie_f - 32) / 1.8
        print("C = " + str(stopnie_c))
    except ValueError:
        print("Podaj liczbę!")
