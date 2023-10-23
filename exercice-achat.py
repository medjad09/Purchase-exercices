

names = []
sommes = []

for i in range(1,4):
    total = 0
    name = input(f'Give the first and last name of customer N°{i} : ')
    names.append(name)
    nombre_article = int(input(f'Give the number of items for customer N°{i} : '))
    for j in range(1,nombre_article+1):
        prix = float(input(f'Give the price of the item {j} : '))
        total = total + prix
    sommes.append(total)
for o in range(3):
    montant_ttc = sommes[o] * (1 + 15/100)
    montant_final = montant_ttc - (montant_ttc * 2/100)
    print(f'The Total to be paid for customer {names[o]} is : {montant_final:.2f} DH')
