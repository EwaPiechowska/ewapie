class Ksiazka(object):
    def __init__(self, tytul, autor, ilosc_stron=100, cena=19.99):
        self.tytul = tytul
        self.ilosc_stron = ilosc_stron
        self.autor = autor
        self.cena = cena
        self.vat = 7
    def __str__(self):
        return f"{self.tytul}, autor: {self.autor}"
    def __len__(self):
        return self.ilosc_stron
    def __add__(self, other):
        if isinstance(other, Ksiazka):
            return self.ilosc_stron + other.ilosc_stron
        else:
            print('Tak naprawdę nie dodałem nic')
            return self.ilosc_stron
class Ebook(Ksiazka):
    def __init__(self, autor, tytul):
        super().__init__(autor, tytul)
        self.format = 'pdf'
        self.vat = 23

class koszyk():
    def __init__(self):
        self.elementy  = []
        self.ilosc_elementow = 0
        self.netto = 0
        self.brutto = 0

    def dodaj(self, element):
        self.elementy.append(element)
        self.ilosc_elementow +=1
        self.netto += element.cena
        self.brutto += element.cena


    def __len__(self):
        return len(self.elementy)

    def wartosc_netto(self):
        self.




koszyk = koszyk()
ksiazka_1= Ksiazka('potop', 'sienkiewicz',300 )
ksiazka_2= Ksiazka('TRYLOGIA', 'sienkiewicz',1200 )
ebook_1 = Ebook('Potop', 'Sienkiewicz')

koszyk.dodaj(ksiazka_1)
koszyk.dodaj(ksiazka_2)
koszyk.dodaj(ebook_1)

print(koszyk.elementy)
print(f"ilosc w koszyku: {len(koszyk)}")
print(f"wartosc netto: ")



# koszyk = Koszyk()
# ksiazka_1 = Ksiazka('Potop'....)
# koszyk.dodaj(ksiazka_1)
# koszyk.dodaj(ksiazka_2)
# koszyk.dodaj(ebook_1)
# print("Ilosc w koszyku: " + len(koszyk))
# print("Wartość netto: " + len(koszyk.wartosc_netto()))
# print("Wartość brutto: " + loszyk.wartosc_brutto()))en(k