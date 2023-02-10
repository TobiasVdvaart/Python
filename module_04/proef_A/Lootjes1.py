import random

name_list = []
name_list_02 = []

while  True :
    name = input("Voer een naam in,  ")
    if name not in name_list:
        name_list.append(name)
        name_list_02.append(name)
    elif name in name_list:
        print("deze naam zit er al in, ") 
    if len(name_list) >= 3:
        eindvraag = input("wilt u lootjes gaan trekken?, ")
        if eindvraag == "ja":
            print("de lootjes zijn, ")
            break

counter_02 = 0

while True:
    if name_list[counter_02] == name_list_02[counter_02]:
        random.shuffle(name_list_02)

    else:
        counter_02 += 1

    if counter_02 == len(name_list):
        break

counter_03 = 0
for name in name_list:
    print(f'{name_list[counter_03]} heeft {name_list_02[counter_03]}')
    counter_03 += 1

            
            








 