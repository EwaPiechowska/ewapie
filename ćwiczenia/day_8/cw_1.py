import requests
# strona = requests.get('https://wp.pl')
dane = requests.get('https://api.exchangeratesapi.io/2000-01-03')
print(dane.text)
dane_str = dane.text

dane.json= dane.json()
print(dane.json['rates']['PLN'])
