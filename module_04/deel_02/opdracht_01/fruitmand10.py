from fruitmand1 import fruitmand
from operator import itemgetter
 

gewichten = []
gesoteerde_fruit = []

# for gewicht in fruitmand:
#     gewichten.append(gewicht["weight"])

# print(sorted(gewichten))

print (sorted(fruitmand, key=itemgetter('name', 'weight')))



