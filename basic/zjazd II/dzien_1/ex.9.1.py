#dostepne_produkty = {"mleko" : 1.50, "cukier": 2.00, "chleb": 2.79}

#print(dostepne_produkty)

#produkt = input("Podaj nazwę produktu, który chcesz kupić: ")
#ilosc = int(input("Jaką ilość produktu chcesz zakupić? :"))

#dostepne_produkty.get("mleko", )
#kwota= dostepne_produkty * ilosc
#print(kwota)


produkty = {
    "ziemniaki": 2.20,
    "kukurydza": 3.40,
    "pomidory": 7.00,
    "kapusta": 3.00,
    "złoto": 10000.00,
}

print ("Dostępne produkty:")
for produkt in produkty:
    print(f" - {produkt}")

produkt = input ("Co kupujesz: ")
ilosc = float(input(" Ile kg:"))

if produkt in produkty:
    print("Należy się", produkty[produkt] * ilosc)
else:
    print(f"Niestety, {produkt} - brak na stanie")