rok= int(input("Podaj rok urodzenia postaci ( przed 1960 r.): "))
aktualny_rok = 2019
wiek =  aktualny_rok-rok

print(" Ta osoba urodziła się przed", wiek, "laty.")
print( "To mogła być Twoja", " pra " * (wiek // 30 - 2 ) + "babka." )
