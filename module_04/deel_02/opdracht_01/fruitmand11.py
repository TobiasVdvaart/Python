from fruitmand1 import fruitmand

niet_rond = 0
rond = 0

zit_erin = False
while zit_erin == False:
    fruit_kleur = input("vul uw gewenste kleur in, ")
    for fruit in fruitmand:
        if fruit['color'] == fruit_kleur:
            zit_erin = True
            break
    if zit_erin == False:
        print("deze kleur zit niet in de fruitmand ")

#rond en niet rond tellen van de juiste kleur
for fruit2 in fruitmand:
    if fruit2['round'] == False:
        niet_rond+=1
    else:
        rond+=1

meer_rond = rond - niet_rond
minder_rond = niet_rond - rond

if niet_rond > rond:
    print(f'Er zijn {minder_rond} meer ronde vruchten dan niet ronde vruchten in de kleur {fruit_kleur}')
else:
    print(f'Er zijn {meer_rond} minder ronde vruchten dan niet ronde vruchten in de kleur {fruit_kleur}')

if niet_rond == rond:
    print(f'Er zijn {meer_rond} ronde vruchten en {niet_rond} niet ronde vruchten in de kleur {fruit_kleur}')



    