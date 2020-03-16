def hej(imie):
    print(f'dzien dobry {imie}')
    #to ponizej oznacza to samo
    # print(f'dzien dobry' + str(imie))
    # print('dzien dobry {}'.format(imie))
hej("łukasz")


#podaje dwa argumenty
def hej(imie, naziwsko):
    print(f'dzien dobry {imie} {naziwsko}')
#tutaj po nawiasie tez musze podac dwa argumenty
hej("lukasz", "falkowicz")

#jak wpisuje imie=cos tam i nazwisko = cos tam
#to przy wywolaniu funkcji hej() wyswietla mi sie te domyslne przypisane nazwy
#ale moge wpsiac swoje tez hej("ewa" "falkowicz")
def hej(imie = 'ewa', naziwsko="falkowicz"):
    print(f'dzien dobry {imie}{naziwsko}')

hej(imie="joanna", naziwsko="kruk")
#dzieki temu ze mamy zdefiniowane imie i nazwisko mozemy zmeiniac ichkolejnosc
hej(naziwsko="stan", imie="borys")

hej()
imie_czlowieka = input('podaj imie: ')
hej(imie_czlowieka)
