a = 0
while a < 10:
    print ( 2 ** a )
    a += 1


a = 0
b = 0
while b < 10000:
    print ( b )
    a += 1
    b = 2 ** a

a = 1
while a < 10:
    print ( 2 ** a)
    a += 1

a = 0
while a < 100:
    print(f"{a}^2 = {a ** 2}")
    a+=1

suma_temperatur = 0
dzien = 1
while dzien < 8 :
    suma_temperatur += float (input(f"Podaj temperaturę dla dnia {dzien}: "))
    dzien += 1

print (f"Średnia temperatur to { suma_temperatur / 7 :.2f}")





