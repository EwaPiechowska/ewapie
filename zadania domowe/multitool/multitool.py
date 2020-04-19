from imports import bin2dec,c_na_f, czworokat, f_na_c, nominaly, parzyste_nieparzyste, pierwsza_ostatnia_cyfra, \
    piramida, podzielne_3i5i7, podzielne_przez_3lub5lub7, powierzchnia_kola, psi_rok, rok_przestepny, losowa_funkcja
import random

def menu():
    def losowa_funkcja():
        return switcher.get(random.randint(1, 13))

    #nazwa modulu. funkcja - ale bez jej wywołania
    switcher = {
        1: bin2dec,
        2: c_na_f,
        3: czworokat,
        4: f_na_c,
        5: nominaly,
        6: parzyste_nieparzyste,
        7: pierwsza_ostatnia_cyfra,
        8: piramida,
        9: podzielne_3i5i7,
        10: podzielne_przez_3lub5lub7,
        11: powierzchnia_kola,
        12: psi_rok,
        13: rok_przestepny,
    }
    print('WITAJ W MULTITOOL PYTHON PROGRAM BY EWA! ')

    for i in switcher:
        print( '%d. %s ' % (i, switcher[i].nazwa))

    print('14. Losowa funkcja')

    print('A teraz podaj numer programu i baw się dobrze: ')
    argument = int(input())
    if argument == 14:
        modul = losowa_funkcja()
        print(modul.nazwa)
    else:
        modul = switcher.get(argument)
    # print(func)
    # Execute the function
    if modul is None:
        print('oj sorry, nie ma takiego programu :(')
    else:
         modul.funkcja()


menu()