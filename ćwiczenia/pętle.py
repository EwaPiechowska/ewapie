#zobaczyl warunek zobaczył true, pass, potem znowu warunek i się kręci
# while True:
#     #nieskonczona pętla
#     pass

# #nieskonczona petla
# while True:
#     print(' . ')
#
# czy_kontynuowac = 'T'
# while czy_kontynuowac == 'T':
#     print(' . ')
#     czy_kontynuowac = input('czy kontynuowac [T/N]? ')
#
# # licznik = 0
# # while licznik < 10:
# #    if licznik == 5:
# #        continue
# #    else:
#        print(licznik)
# #Mmodyfikacja zmiennej
#    licznik += 1

# licznik = 0
# while licznik < 10:
#    licznik += 1
# #mozna tez zapisac if licznik in [5,8]:
#    if licznik == 5 or licznik == 8:
# #to continue omija jedną kolejkę
#        continue
# #bez elsa tez zadziała
#    else:
#        print(licznik)


# licznik = 0
# while licznik < 10:
#    licznik += 1
#    if licznik == 5 or licznik == 8:
#        break


zdanie = "ala ma kota"
# for litera in zdanie:
#     print(litera)

for litera in zdanie:
    if litera in ['E']:
        continue
    print(zdanie)


