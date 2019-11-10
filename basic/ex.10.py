a=int(input("Podaj pierwszą liczbę: "))
b=int(input("Podaj drugą liczbę: "))

dzialanie = input("Podaj rodzaj operacji: ")


if dzialanie == "+":
    print("Wynik", a + b)
elif dzialanie == "-":
    print("Wynik", a - b)
elif dzialanie == "*":
    print("Wynik:", a * b)
elif dzialanie == "/":
    if b != 0:
        print ("Wynik", a / b)
    else:
        print ("nie można dzielic przez zero")
else:
    print ("niepoprawne dzialanie. Obslugiwane: + - * / ")

