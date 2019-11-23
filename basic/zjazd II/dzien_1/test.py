print("Ala")
print("kot")


print("ala", end= '')
print("kot")



print(f"{12:5}") #5 spacji przed "12"

print(f"{1:3}", end='') #przed "1" 2x spacja (liczba+ 2 spacje =łącznie 3 miejsca)
print(f"{9:3}", end='') #przed "9" 2x spacja
print(f"{10:3}", end='') #przed "10" 1x spacja (10 to liczba dwu-dyfrowa)
print(f"{50:3}", end='') #przed "50" 1x spacja (10 to liczba dwu-dyfrowa)
print(f"{90:3}", end='') #przed "90" 1x spacja (10 to liczba dwu-dyfrowa)



lista=["A", "B", "C", "D", "E"]
lista[2]



liczby=[1,5,8,9,7]
for liczba in liczby:
    if liczba > 10:
        print("Znalaziono liczbe wieksza od 10")
        break
    else:
        print("nie znaleziono liczby wiekszej od 10")


