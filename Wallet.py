
wallet = int(input("Quelle est la valeur de votre porte monnaie"))
produit = 50
if wallet >= produit:
    print("Vous pouvez acheter le produit qui est au prix de " + str(produit))
else:
    print("Vous ne pouvez pas acheter le produit")
    exit()



buy = int(input("Voulez vous acheter le produit 0 non, 1 oui "))
if buy == 0:
    print("Vous n'avez pas acheter le produit votre wallet est de " + str(wallet))
    exit()
else:
    wallet = wallet - produit
    print("Vous avez acheter le produit votre wallet est de " + str(wallet))
    exit()

