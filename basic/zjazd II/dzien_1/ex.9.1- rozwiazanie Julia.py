import random
produkty = {'jablka': 3.50, 'pomarancze': 4.40, 'winogrona': 5.50, 'nektarynki': 3.20, 'kokos': 8.90}
suma = 0
print("Witamy w sklepie!")
for klucz,wartosc in produkty.items():
    print(klucz, "->",wartosc)
portfel = random.randint(30, 100)
print(f"Mam {portfel} zl")
koszyk = dict()
while True:
    owoc = input("Co chce kupic? ").lower().strip()
    if owoc == "nic":
        if suma > portfel:
            roznica = suma-portfel
            print(f"W koszyku mam:{koszyk}.Nie stać cię")
            y = input("Czy chcesz cos z tym zrobic? ")
            if y == "tak":
                x = input("Co chcesz usunac z koszyka? ")
                cena_do_us = koszyk[x]
                suma -= cena_do_us
                del koszyk[x]
                continue
            else:
                print(f"Brakuje ci: {int(roznica)} zł. Zapraszamy ponownie póżniej!")
            break
        else:
            print(f"W koszyku mam:{koszyk}")
            print(f"Za zakupy zapłace: {suma} zł")
            break
    if owoc not in produkty:
        print("Nie ma takiego produktu")
        continue
    ilosc = int(input("Ile kg? "))
    cena_za_kg = produkty[owoc]
    cena = ilosc*cena_za_kg
    if owoc not in koszyk:
        koszyk[owoc] = cena
    else:
        koszyk[owoc] += cena
    suma += cena