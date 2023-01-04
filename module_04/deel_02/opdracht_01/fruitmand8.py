from fruitmand1 import fruitmand
 
fruitmand.append({
    'name' : 'watermelon',
    'weight' : 2500,
    'color' : 'green',
    'round' : True
})

for fruit in fruitmand:
    print(fruit['weight'])

