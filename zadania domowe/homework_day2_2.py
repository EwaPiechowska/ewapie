#2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
print("Wzór na przeliczanie stopni F na C wygląda tak: F = (32+9) / 5* (C)")
print("wpisz stopnie w F: ")
F = float(input())
C = (F - 32) /1.8
print ("C = " + str(C))
