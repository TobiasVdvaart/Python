from random import random


print ('+++++++++++++++++++++++++++++'
'solicitatie Circusdirecteur voor Circus HotelDeBotel'
"""+++++++++++++++++++++++++++++""")

geslachtMv = input("Wat is uw geslacht? (M/V): ")
if geslachtMv == 'm'or geslachtMv == 'M':
    manSnor = input("Heeft u een snor? (J/N): ")
    if manSnor == 'j' or manSnor == 'J':
        snorCm = int(input("Hoelang is uw snor? (in cm): "))

elif geslachtMv == 'v' or geslachtMv == 'V':
    vrouwHaarkleur = input("Wat is uw haarkleur? (rood/zwart/blond): ")
    if vrouwHaarkleur == 'rood':
        raise NameError('we nemen geen vuurtorens aan')
    vrouwHaarlengte = int(input("Wat is uw krulhaarlengte? (in cm): "))
dierDressuur = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?: "))
jongleerErvaring = int(input("Hoeveel jaar ervaring heeft u met jongleren?: "))
acroErvaring = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek?: "))
randomVraag1 = input("Bent u Minecraft-Expert?: (J/N) ")
diploma = input("Bent u in bezit van een Diploma MBO-4 ondernemen? (J/N): ")
if diploma == 'nee':
    raise NameError("je bent te dom")
else:
    rijbewijs = input("Bent u in bezit van een vrachtwagen rijbewijs? (J/N): ")
randomVraag2 = input("Heeft u ooit een vulkaan-uitbarsting gezien? (J/N): ")
hogeHoed = input("Bent u in het bezit van een grote hoed? (J/N): ")
randomVraag3 = input("Spendeert u een hele dag op YouTube? (J/N): ")
persoonLengte = int(input("Hoe lang bent u? (in cm): "))
if persoonLengte == '150':
    raise NameError('helaas we nemen geen goblins aan')
else:
    randomVraag4 = input("Wilt u de loterij winnen? (J/N): ")
persoonGewicht = int(input("Hoeveel weegt u? (in kg): "))
certificaatGevaar = input("Heeft u het certificaat 'Overleven met gevaarlijke mensen'? (J/N) ")


if geslachtMv == 'm' or geslachtMv == 'M':
    if (dierDressuur > 4 or jongleerErvaring > 5 or acroErvaring > 3) and (diploma == 'j' and rijbewijs == 'j' and hogeHoed == 'j' and snorCm >= 10 and persoonLengte >= 150 and persoonGewicht >= 90 and certificaatGevaar == 'j'):
        print("U komt in aanmerking voor deze functie :) ")
    else:
        print("Helaas, u komt niet in aanmerking voor deze functie :( ")
elif geslachtMv == 'v' or geslachtMv == 'V':
    if (dierDressuur >= 4 or jongleerErvaring >= 5 or acroErvaring >= 3) and (diploma == 'j' and rijbewijs == 'j' and hogeHoed == 'j' and vrouwHaarkleur == 'rood' and vrouwHaarlengte >= 20 and persoonLengte >= 150 and persoonGewicht >= 90 and certificaatGevaar == 'j'):
        print("U komt in aanmerking voor deze functie :) ")
    else:
        print("Helaas, u komt niet in aanmerking voor deze functie :( ")
