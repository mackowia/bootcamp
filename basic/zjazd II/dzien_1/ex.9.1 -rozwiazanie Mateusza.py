productsPrices = {
    "marchew": 10,
    "ziemniaki": 3.15,
    "papryka": 6.99,
    "łosoś": 55
}

productsBought = {}
productsBoughtAmount = {}
sumTotal = 0
amountTotal = 0

for i in productsPrices:
    print(f"Towar: {i}. Cena za kilogram: {productsPrices[i]}")

while True:
    product = input("Co chcesz kupić? ").lower().strip()

    if product in productsPrices:
        amount = float(input("Ile kg? "))
    elif not product in productsPrices:
        askToAdd = input("Nie ma takiego towaru. Czy chcesz dodać [tak/nie]? ")
        if askToAdd == "tak":
            productToAdd = input("Podaj towar: ").lower().strip()
            priceToAdd = float(input("Podaj cenę: "))
            productsPrices[productToAdd] = productsPrices.get(productToAdd, priceToAdd)
            continue
        else:
            continue

    if product in productsBought:
        duplikatProduktu = input("Produt znajduje się już w koszyku. Czy chcesz dodać większą ilość tego produktu [tak/nie]? ").lower().strip()

        if duplikatProduktu != "tak":
            check = input("Czy kończysz zakupy [tak/nie]? ").lower().strip()

            if check == "nie":
                continue
            elif check != "nie":
                print(f"Za Twoje zakupy należy się: {sumTotal} złotych")
                break

        if duplikatProduktu == "tak":
            productsBought[product] = productsBought.get(product, 0) + round(amount * productsPrices[product], 2)
            sumTotal += round(amount * productsPrices[product], 2)
            productsBoughtAmount[product] = productsBoughtAmount.get(product, 0) + amount
            amountTotal += amount

            check = input("Czy kończysz zakupy [tak/nie]? ").lower().strip()
            if check == "nie":
                continue
            elif check != "nie":
                print(f"Za Twoje zakupy należy się: {sumTotal} złotych")
                break

    productsBought[product] = productsBought.get(product, 0) + round(amount * productsPrices[product], 2)
    sumTotal += round(amount * productsPrices[product], 2)
    productsBoughtAmount[product] = productsBoughtAmount.get(product, 0) + amount
    amountTotal += amount

    check = input("Czy kończysz zakupy [tak/nie]? ").lower().strip()
    if check == "nie":
        continue
    elif check != "nie":
        print(f"\n\nZa Twoje zakupy należy się: {sumTotal} złotych")
        break

print(f"\nTwój koszyk: {productsBought} złotych."
      f"\nTwój koszyk: {productsBoughtAmount} kg."
      f"\n\nCennik sklepu: {productsPrices}")