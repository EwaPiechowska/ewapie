# Kalkulator do wyliczania wieku psa.
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
#  Np: 15 ludzkich lat to 73 psie lata
nazwa = 'Kalkulator do wyliczania wieku psa'
def funkcja():
    psi_rok_1 = 10.5
    psi_rok_2 = 21
    kolejny_rok = 4
    print("podaj wiek ludzia: ")
    wiek = int(input())
    if wiek ==1:
        print('wiek psa to %s.' % psi_rok_1)
    elif wiek == 2:
        print('wiek psa to %s. ' % psi_rok_2)
    else:
        print('wiek psa to %s. ' % (psi_rok_2 + (wiek-2)*4))
