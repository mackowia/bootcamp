liczba_min = "None"
liczba_max = "None"



while True:
    dane = input('Wpisz liczbę lub "koniec": ')
    if dane.lower() == "koniec":
        break
    if dane == "" or not dane.replace('-', '') .isdigit():
        print("Nic nie wpisałeś!")
        continue
    liczba= int(dane)
    if liczba_min == "None" or liczba < liczba_min:
        liczba_min = liczba
    if liczba_max == "None" or liczba > liczba_max:
        liczba_max = liczba
