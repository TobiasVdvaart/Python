from fruitmand1 import fruitmand
import random



aantal = int(input("Geef een aantal op: "))



for i in range(aantal):
    random_pick = random.choice(fruitmand)
    print(random_pick)