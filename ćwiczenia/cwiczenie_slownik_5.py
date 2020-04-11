# wiersze = {}

wiersze = [
    {'imie': 'ewa', 'naziwsko': 'Falkowicz'},
    {'imie': 'Adam', 'naziwsko': 'Falkowicz'},
    {'imie': 'Jan', 'naziwsko': 'Falkowicz'},
]

#mam na imie: ewa
#mam na imie:..

print(type(wiersze))
#iterujemy, nawiasy klamrowe to slownik
for element in wiersze:
    #imie to jest klucz u nas
    print(element['imie'])

slownik = {'imie': 'Lukasz', 0 : 'wartosc zero', "0": 'warosc zero jest stringiem'}
print(slownik['imie'])
print(slownik[0])
print(slownik["0"])
