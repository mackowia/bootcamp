liczby = []

while len(liczby) < 10:
    dana = input("Podaj liczbe lub 'koniec': ").strip()
    #dana = dana.strip()
    if not dana:
        print("Nic nie podałeś!")
        continue
    if dana.lower() == 'koniec' :
        break
    if not dana.replace('-', '').isdigit():
        print("Obsługuję tylko liczby całkowite i 'koniec' ")
    dana = int(dana)
    liczby.append(dana)

#if len(liczby) != 0:
if liczby:
    print("Średnia to", sum(liczby)/len(liczby))
else:
    print("Nie podałeś żadnej liczby!")