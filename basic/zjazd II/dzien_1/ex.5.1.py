print("   ", end='')
for y in range(10):
    print(f"{y:3}", end='')
print()
print()

for x in range(10):
    print(x, end='  ') # pomiedzy '' 2x spacja
    #print() tutaj też zadziała print, tworząć tabele
    for y in range(10):
        print(f"{x*y:3}", end='')
    print()
