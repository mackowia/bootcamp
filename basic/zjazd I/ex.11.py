x=int(input("podaj pozycje x:"))
y=int(input("Podaj pozycje y:"))

if x > 100 or x < 0 or y > 100 or y < 0:
    print ("Gracz znajduje się poza planszą.")
elif x <= 10:
    if y >= 90:
        print("Gracz znajduje się na lewym górnym rogu.")
    elif y <= 10:
        print("Gracz znajduje się na lewym dolnym rogu.")
    else:
        print("Gracz znajduje się w lewej krawedzi")
elif x >= 90:
    if y >= 90:
        print("Gracz znajduje się w prawym gornym rogu")
    elif y <= 10:
        print("Gracz znajduje się w prawym dolnym rogu")
    else:
        print ("Gracz znajduje się na prawej krawedzi")
else:
    if y >= 90:
        print("Gracza znajduje sie na gornej krawedzi")
    elif y <= 10:
        print("Gracza znajduje sie na dolnej krawedzi")
    else:
        print("Gracz znajduje sie na srodku planszy")



