import random

kleuren = ('oranje', 'blauw', 'groen', 'bruin')
zak = []
aantal = int(input('Hoeveel M&Ms wil je toevoegen aan de zak? '))
for i in range(aantal):
    kleur = kleuren[random.randint(0, (kleuren) - 1)]
    zak.append(kleur)

print('De zak bevat de volgende M&Ms:')
for kleur in zak:
    print(kleur)
