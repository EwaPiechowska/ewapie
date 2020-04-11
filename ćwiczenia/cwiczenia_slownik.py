slownik = {}
print(type(slownik))
slownik['imiona'] = ['ALA', 'JAN']
print(slownik)
slownik.update({'nazwiska': ['kowalski', 'cezar']})

wiersze = [
    {'imie': 'lukasz', 'nazwisko': 'falkowicz'},
    {'imie': 'ewa', 'nazwisko': 'falkowicz'},
    {'imie': 'jan', 'nazwisko': 'falkowicz'},
]
print(slownik)
print(len(slownik))
print(slownik.values())

for klucz, wartosc in slownik.items():
    print(klucz)
    print(wartosc)
    print('===')

# slownik = {}
# slownik['imiona'] = ['ALA', 'JAN', 'EWA']
# print(slownik)
# print('mam na imię: ' slownik(0))

