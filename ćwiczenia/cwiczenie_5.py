lista = [1, 2, 3]
nowa_lista = lista
print(lista)
lista[0] = 'jeden'
print(nowa_lista)
print(lista)

lista_1 = ['A', 'B', 'C']
prawdziwa_kopia = lista_1.copy()
print(lista_1)
lista_1[0] = '6'
print(lista_1)

#można też slajsować liste czyli np. prawdziwa kopie = lista_1[1:2]

#lista zagnieżdzona --> to sie moze pojawic na tescie -->copy deepcopy

lista_3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
import copy
nowka_lista = copy.deepcopy(lista_3)
print(lista_3[1][1])
lista_3[1][1] = 'X'
print(nowka_lista[1][1])
print(lista_3[1][1])