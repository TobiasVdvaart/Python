import random

kleuren = ['rood', 'blauw', 'groen', 'geel', 'bruin']
zak = {}

aantal_MM = int(input("hoeveel M&M's wilt u toevoegen,  "))

for i in range(aantal_MM):
    kleur = random.choice(kleuren)
    if kleur in zak:
        zak[kleur] += 1
    else:
        zak[kleur] = 1

print(zak)


