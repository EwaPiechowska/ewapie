#10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym
nazwa = 'Program do sprawdzania czy podany rok jest rokiem przestępnym'
def funkcja():
    print("podaj rok: ")

    try:
        rok = int(input())
        #((rok mod 4 = 0) and (rok mod 100 <> 0)) or (rok mod 400 = 0)
        if ( rok % 4 ==0 and rok % 100 != 0) or ( rok % 400 ==0 ):
            print("rok jest przestępny!")
        else:
            print("rok nie jest przestępny!")
    except ValueError:
        print('podaj liczbę!')


