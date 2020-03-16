zestaw_liczb = range(0,10)
print(zestaw_liczb)

lista = [1,2,3,4,5,7,9,10]
print(lista)

#list kazda po koeli wywołuje
lista_2 = list('dwa')
print(lista_2)

lista_3 = ['d', 'w', 'a']
print(lista_3)

lista_4 = list(range(0,10))
print(lista_4)

lista_5 = ['zero', 1, 'trzeci', 'dom']
print(lista_5)
print(lista_5[-1])
print(lista_5[::-1])
#modyfikujemy coś z listy - podajemuy indeks i = do czegos co chcemy
lista_5[1] = 'jedenascie'
print(lista_5)
#dodawanie elementow do listy
lista_5.append('nowy element')
print(lista_5)
#usuwanie elementów z listy
del(lista_5[1])
print(lista_5)
#usuwanie po wartości
lista_5.remove('dom')
print(lista_5)



if 'trzeci' in lista_5:
    lista_5.remove('trzeci')
    print('usunięto')
else:
    print("taki wyraz nie istnieje")

do_skasowania = input('co skasowac')
if do_skasowania in lista_5:
    lista_5.remove(do_skasowania)





