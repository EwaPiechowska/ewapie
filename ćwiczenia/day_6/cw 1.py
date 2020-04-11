# plik = open('test.txt', 'a+')
# print(plik.tell())
# print(plik.read())
# print(plik.tell())

# plik = open('test.txt', 'r+')
# print(plik.tell())
# print(plik.readline())
# print(plik.tell())
# #offset i whence - domysla wartsc to 0
# #4,0  --> 4 liczby od miejsca gdzie jest kursor i przesuwa o 4
# # a jak jest np 10,5 --> to 10 znakow od konca
# print(plik.seek(2))
# wszystkie_linie = plik.readlines()
# print(wszystkie_linie)
# plik.close()
import io


with open ('test.txt', 'r+') as plik:
    print(plik.tell())
    wszystkie_linie = plik.readlines()
    print(wszystkie_linie)
    print(plik.tell())
    try:
        plik.writelines(['\nlinia 5', '\nlinia 8'])
    except io.UnsupportedOperation:
        print('nie masz uprawien do teo zapisu. ')

    print(plik.tell())
