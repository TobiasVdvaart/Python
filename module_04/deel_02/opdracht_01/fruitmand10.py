from fruitmand1 import fruitmand

gewichten = []
gesoteerde_fruit = []

for gewicht in fruitmand:
    gewichten.append(gewicht["weight"])

print(sorted(gewichten))

for fruit in fruitmand:
    gesoteerde_fruit.append(fruit["name"])
print(sorted(gesoteerde_fruit))    


