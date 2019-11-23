rok= int(input("Podaj rok urodzenia postaci: "))
aktualny_rok = 2019
wiek =  aktualny_rok-rok

print(" Ta osoba urodziła się przed", wiek, "laty.")

if wiek >= 18:
    print("Jesteś pełnoletni")
else:
    print("Jesteś niepełnoletni")