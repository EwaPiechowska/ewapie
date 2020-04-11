napis1 = 'witaj'
napis2 = "witaj"
if (napis1 == napis2):
    print('TRUE')
else:
    print('to nieprawda!')

napis = "Nie martw sie o 'pojedyncze' cudzyslowy."
print(napis)

jeden = 1
dwa = 2
trzy = jeden + dwa
print (trzy)

witaj = "witaj"
swiecie = "swiecie"
witajswiecie = witaj + " " + swiecie
print (witajswiecie)

# zmien ponizszy kod
napis = 'witaj'
rzeczywista = float(10)
calkowita = 20

# sprawdzenie kodu
if napis == 'witaj':
    print (napis)
if isinstance(rzeczywista, float) and rzeczywista == 10.0:
    print ('to jest liczba rzeczywista!')
if isinstance(calkowita, int) and calkowita == 20:
    print ('to jest liczba całkowita!')

liczby = [1,2,3]
napisy = ['witaj' , 'swiecie']
imiona = ['jan', 'edward', 'joanna']
print(liczby)
print(napisy)
drugie_imie = imiona[1]
print(drugie_imie)
print("drugim imieniem w tablicy jest:" + drugie_imie)

parzyste_dodatnie = [2,4,6,8]
nieparzyste_dodatnie = [1,3,5,7]
naturalne = parzyste_dodatnie + nieparzyste_dodatnie
print(naturalne)

print ([1,2,3] * 3)

x = object()
y = object()

# zmien ten kod
x_tab = [x,2,x,x,x,x,x,x,x,x]
y_tab = [y,y,y,y,y,y,y,y,y,y]
duza_tab = x_tab + y_tab

print ("x_tab zawiera %d obiektow" % len(x_tab))
print ("y_tab zawiera %d obiektow" % len(y_tab))
print ("duza_tab zawiera %d obiektow" % len(duza_tab))

# sprawdzenie poprawnosci
if x_tab.count(2) == 1 and y_tab.count(y) == 10:
    print ("Prawie zrobione...")
else:
    print('źle')
if duza_tab.count(x) == 10 and duza_tab.count(y) == 10:
    print ("Doskonale!")

dane = ("Dorota", 5, 32,45,32)

print ("%s mieszka w bloku nr %d w mieszkaniu %d" % dane[0:3])

rzeczywista_1 = 4.34
rzeczywista_2 = 54.432
calkowita = 16

print ("rzeczywista_1 = %f" % rzeczywista_1)
print ("rzeczywista_2 = %f" % rzeczywista_2)
print ("rzeczywista_2 = %.2f" % rzeczywista_2)

dane_1 = ('jacek', 'darek', 44.4)
print("czesc %s i %s. temperatura na zewnątrz wynosi %.1f stopnie celsjusza" % dane_1)

napis = "abcdeabcde"
print (napis.count("a"))

napis3 = 'jaki powinien byc ten napis?'
print(len(napis3))
len(napis3)
print("dlugosc napisu to %d" % len(napis3[0:17]))
print(napis3[1])
print(napis3.count('a'))
print("'a' wystepuje %d razy" % napis3.count('a'))
print ("Pierwszych piec znakow to '%s'" % napis3[:5])

napis3 = napis3.replace('n', 'N')
# print(napis3)
napis3 = napis3[-6:-5].upper() + napis3[-5:]
print(napis3)
print(napis3[-6:-3])
if napis3[-6:-3].startswith("Nap"):
    print ("Napis zaczyna sie od 'Nap'. Dobrze!")
else:
    print("zle")

napis3 = napis3.replace('ten', 'tne')
print(napis3)
if napis3[-10:-7].endswith('tne'):
    print("Napis konczy sie 'tne'. Dobrze!")

napis3 = napis3[0:17]
print(napis3)
tablica = napis3.split()
print(tablica)


