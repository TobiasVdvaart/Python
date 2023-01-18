from fruitmand1 import fruitmand

longest_fruit = ''

for fruit in fruitmand:
    if  len(fruit["name"]) > len(longest_fruit):
        print(fruit['name'])
        longest_fruit = fruit['name']
        


print(longest_fruit)

