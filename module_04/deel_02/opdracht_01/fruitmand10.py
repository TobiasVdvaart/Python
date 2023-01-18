from fruitmand1 import fruitmand
from operator import itemgetter
 


gewicht = sorted(fruitmand, key=itemgetter('weight'), reverse=True)

for fruitje in gewicht:
    print(f"fruit: {fruitje['name']}")
    print(f"gewicht: {fruitje['weight']}")
    print("")


