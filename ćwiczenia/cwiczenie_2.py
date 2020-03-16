# cudzysłow w vudzyslowiu byc nie może
# dlatego trzeba wyeskejpowac np. prz \\
# tytul = "Ksiązka pt.: \"kot w butach\"."
# tytul = 'ksiązka pt.: "kot w butach".'
# print(tytul)



#tu jest string i int, dlatego trzeba rzutować (w linijce 11)
liczba = 1
liczba_2 = 863
#print('wprowadziles liczbe: ' + liczba)
#dlatego możemy zrobić tak:
print(f'wprowadziles liczbe: {liczba}'
      f'dzieki jeszcze raz za liczbe {liczba}' )
print('wprowadziles liczbę: {} {}'.format(liczba, liczba_2))
print('wprowadziles liczbę: {} {a} {a}'.format(liczba, a = liczba_2))