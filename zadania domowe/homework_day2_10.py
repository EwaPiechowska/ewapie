#10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym
print("podaj rok: ")
rok = int(input())
#((rok mod 4 = 0) and (rok mod 100 <> 0)) or (rok mod 400 = 0)
if ( rok % 4 ==0 and rok % 100 != 0) or ( rok % 400 ==0 ):
    print("rok jest przestępny!")
else:
    print("rok nie jest przestępny!")
