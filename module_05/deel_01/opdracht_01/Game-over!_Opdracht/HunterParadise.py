from game_verhaal import *

HEALTH_PLAYER = 100
DEFENSE_PLAYER = 0
DAMAGE_PLAYER = 5

HEALTH_ENEMY_01 = 50
DAMAGE_ENEMY_01 = 10

HEALTH_ENEMY_02 = 70
DAMAGE_ENEMY_02 = 15

HEALTH_ENEMY_03 = 60
DAMAGE_ENEMY_03 = 20

HEALTH_ENEMY_04 = 80
DAMAGE_ENEMY_04 = 22

HEALTH_BOSS = 200
DAMAGE_ENEMY_05 = 50
def damage_functie_player():
    print("test")

#STARTING POINT
print(afbeeldingen[0])
print(Teksten[0])
vraag_1 = input(" yes/no, ")
if vraag_1 == "no":
    quit
naam_speler = input("wat is uw naam, ")


#STORY
print(afbeeldingen[1])
print(Teksten[1])
print(afbeeldingen[2])
print(Teksten[2])

#STORY_02
print(f"mom: {naam_speler} Wake up!" )
print(f"{naam_speler}: zZZzZZZ")
print(f"mom: {naam_speler} you need wake up!, its you're big day! you can take you're hunter Exam today! ")
print(f"{naam_speler}: Yes! im gonna be the greatest of them All!")
print(f"mom: If you want to be the greatest {naam_speler} you need to be on time! ")
print(afbeeldingen[3])
print(Teksten[3])
print(afbeeldingen[4])

vraag_2 = input("you see some people sitting in a cabin, are you joining them?, yes/no, ")

if vraag_2 == "no":
    print(Teksten[4])
else:
    print
