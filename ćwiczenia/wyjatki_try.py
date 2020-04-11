# try:
#     # print('dzielenie')
#     # wynik = zmienn_ktorej_nie_ma
#     wynik = 15/0
#     print(wynik)
#     #on juz nie doszedł do linijki 4 bo sie nie dzieli przez 0
#     print(wynik)
# except:
#     print('wystapił błąd')
#
#
# #czy uzytkownik wprowadzil nam liczne
# #do nakładni moze si eprzydać
#
# liczba = None
# while liczba is None:
#     wartosc = input('podaj liczbe: ')
#     try:
#     #zamieniamy np przecinek na kropke, jakby uzytkownik sie walnął
#     #uzywając replace
#         wartosc = wartosc.replace(',', '.')
#         liczba = float(wartosc)
#     except:
#         print('to nie jest liczba! podaj jeszcze raz')
# #importuje moduly
import moduly.witacz
moduly.witacz.dzien_dobry()

import send2trash
send2trash.send2trash('smietnik.txt')