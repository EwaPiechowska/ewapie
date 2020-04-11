import bs4
import requests

olx_html = requests.get('https://www.olx.pl/motoryzacja/samochody/')
parser = bs4.BeautifulSoup(olx_html.text, 'html.parser')
obrazki = parser.find_all('img')
for obrazek in obrazki:
    print(obrazek.get('alt'))
    print(obrazek.get('src'))
    #tworze katalog obrazki
    #sciagam obrezek z internetu
    #zapisuje jego zawrtosci do pliku NAZWA.JPG
    #gdzie NAZWA to wartość a <img 'alt'='...'>