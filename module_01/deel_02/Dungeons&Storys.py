
############### INFO ########################
print(f"""
=========================================
        Storys&Dungeons
=========================================""")
print('welcome travaler to the word of Storys&Dungeons')
naam = input('what is youre name traveler? ')
print (f"welcome, {naam}")
sex = input('are you a boy or a girl? ')
print (f'ahh you are a {sex}')
print (f'okay {naam} here you go!')

###############FORREST######################
print (f'welcome {naam} to youre first dungeon keep in mind everything you choise will effect the story')
place = input(f'okay {naam} where are you going? forrest/cave ')
owns_dagger = False

if place == 'forrest':
    print('you are going to the forrest  ')
    house = input('you find a elfs house are you going in? yes/no ')
    if house == 'yes':
        print ('you entered the elfs house')
        dagger = input('you find a elfs dagger do you take it? yes/no ')
        if dagger =='yes':
            owns_dagger = True
            print ('you pick up the dagger and put it in youre pocket')
        else:
            print('you ignore the dagger and go outside')

    if house == 'no':
        print ('you ignore the house ')
    print ('you are going further in the woods')

    death_pick1 = input('its becoming dark are you doing to sleep? yes/no ')
    if death_pick1 == 'yes':
        print('you where killed in youre sleep')
        exit()
    elif death_pick1 == 'no':
        print('you didint dont go to sleep and go further in the forrest ')
    print ('you find the the end boss of the dungeon The wandering Demon Tree')
    if owns_dagger:
        print('you killed The Demon Tree with the elfs dagger')
    else:
        print('you entered the dungeon but you where killed because you didint have the gear for it')
    print (f"""
    =========================================
        Thank you for playing
          Storys&Dungeons
          Made by: Tobias Van der Vaart
          commissioned by: Davinci College
    =========================================""")
    exit()

###############CAVE############################

if place == 'cave':
    print('you are going to the cave  ')
    owns_hammer = False
house2 = input('you find a dwarfs house are you going in? yes/no ')
if house2 == 'yes':
    print ('you entered the dwarfs house')
    hammer = input('you find a dwarfs hammer do you take it? yes/no ')
    if hammer =='yes':
        owns_hammer = True
        print ('you pick up the dagger and put it in youre pocket')
if house2 == 'no':
    print ('you ignore the house ')
print ('you are going further in the mines')

death_pick2 = input('you are becoming tired are you going to sleep? yes/no ')
if death_pick2 == 'yes':
    print('you where killed in youre sleep')
    exit()
elif death_pick2 == 'no':
    print('you didint dont go to sleep and go further in the mine ')
    
print ('you find the the end boss of the dungeon The Stone demon Golem')
if  owns_hammer :
    print('you killed the demon tree with the elfs dagger')
else:
    print('you entered the dungeon but you where killed because you didint have the gear for it')
print (f"""
=========================================
        Thank you for playing
          Storys&Dungeons
          Made by: Tobias Van der Vaart
          commissioned by: Davinci College
=========================================""")
exit()

