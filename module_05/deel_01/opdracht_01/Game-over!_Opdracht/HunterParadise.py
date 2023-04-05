# clobal en lokal verschil uitzoeken
# import, functies, variablen/constane, flow
# leren functies scrijfen zonder globale variablen


from game_verhaal import *
import random
import time

def gevecht(player_hp,goblin_hp):
        while goblin_hp > 0:
            print(f"Goblin: HP:{goblin_hp} Attack:{goblin_attack}")
            speler_keuze_1 = input(f"{naam_speler}: HP:{player_hp} Attack:{player_attack} Defense:{player_defense}. Wat gaat u doen: attack/defense ")

            if speler_keuze_1 == 'attack':
                goblin_hp = goblin_hp - random.randint(15, 25)
                time.sleep(1)
                print(f'de Goblins hp is nu: {goblin_hp}')
                time.sleep(1)
                print('de goblin heeft ook aangevallen!')
                player_hp = player_hp - random.randint(10, 20)
                time.sleep(0)
                print(f'je HP is nu:{player_hp}')

            if player_defense == 0:
                if speler_keuze_1 == 'defense':
                    print('Je hebt geen schild!')
                    time.sleep(1)
                    print(f'de Goblins hp is nu: {goblin_hp}')
                    time.sleep(1)
                    print('de goblin heeft ook aangevallen!')
                    player_hp = player_hp - random.randint(10, 20)
                    time.sleep(0)
                    print(f'je HP is nu:{player_hp}')
                    gevecht(100,80)
        return goblin_hp, player_hp
def level_up():
    player_hp += random.randint
    player_attack = random.randint(10, 20)
    print("Je bent level Up!")
    time.sleep(2)
    print(f'je HP is nu {player_hp}')
     

player_attack = 25
player_defense = 0
goblin_attack = 20

start_vraag = input("wilt u starten? yes/no ")

if start_vraag == "no":
    quit()

else:
    naam_speler = input('wat is uw naam ')
    time.sleep(2)
    print(Teksten[0])
    time.sleep(2)
    gevecht(100,80)

    player_hp = 100
    level_up()
    print("FLOOR REWARD")
    time.sleep(2)
    print('Fire sword')
    time.sleep(2)
    print(f'Je attack is nu {player_attack}')
    time.sleep(2)
    print("je hebt de 1ste monster verslagen...")
    time.sleep(3)
    print("maar wees niet te blij want dit is niet de laatste!")
    time.sleep(1)
    goblin_hp = 80
    goblin_hp = goblin_hp + random.randint(30, 50)
    goblin_attack = goblin_attack + random.randint(5, 10)
    gevecht(player_hp,goblin_hp)
    level_up(player_hp = 130)
    print("FLOOR REWARD")
    time.sleep(2)
    print('Ice shield')
    time.sleep(2)
    print(f'Je Defense is nu {player_defense}')
    time.sleep(2)
    print("hmm....")
    time.sleep(1)
    goblin_hp = goblin_hp + random.randint(20, 40)
    goblin_attack = goblin_attack + random.randint(10,20)
    gevecht()
    


























    # while goblin_hp > 0:
    #     print(f"Goblin: HP:{goblin_hp} Attack:{goblin_attack}")
    #     speler_keuze_1 = input(f"{naam_speler}: HP:{player_hp} Attack:{player_attack} Defense:{player_defense}. Wat gaat u doen: attack/defense ")
        
    #     if speler_keuze_1 == 'attack':
    #         goblin_hp = goblin_hp - random.randint(15, 25)
    #         time.sleep(1)
    #         print(f'de Goblins hp is nu: {goblin_hp}')
    #         time.sleep(1)
    #         print('de goblin heeft ook aangevallen!')
    #         player_hp = player_hp - random.randint(10, 20)
    #         time.sleep(0)
    #         print(f'je HP is nu:{player_hp}')

    #     if player_defense == 0:
    #         if speler_keuze_1 == 'defense':
    #             print('Je heb geen schild!')
    #             time.sleep(1)
    #             print(f'de Goblins hp is nu: {goblin_hp}')
    #             time.sleep(1)
    #             print('de goblin heeft ook aangevallen!')
    #             player_hp = player_hp - random.randint(10, 20)
    #             time.sleep(0)
    #             print(f'je HP is nu:{player_hp}')

    #     if goblin_hp <= 0:
    #         player_hp = 100
    #         player_hp = player_hp + 30
    #         player_attack = player_attack + random.randint(10,20)
    #         print("Je bent level Up!")
    #         time.sleep(2)
    #         print(f'je HP is nu {player_hp}')
    #         time.sleep(2)
    #         print("FLOOR REWARD")
    #         time.sleep(2)
    #         print('Fire sword')
    #         time.sleep(2)
    #         print(f'Je attack is nu {player_attack}')
    #         time.sleep(2)
    #         print("je heb de 1ste monster verslagen...")
    #         time.sleep(3)
    #         print("maar wees niet te blij want dit is niet de laaste!")
    #         time.sleep(1)
    #         goblin_hp = 80
    #         goblin_hp = goblin_hp + random.randint(30, 50)
    #         goblin_attack = goblin_attack + random.randint(5, 10)	
    #         while goblin_hp > 0:
    #             print(f"Goblin: HP:{goblin_hp} Attack:{goblin_attack}")
    #             speler_keuze_1 = input(f"{naam_speler}: HP:{player_hp} Attack:{player_attack} Defense:{player_defense}. Wat gaat u doen: attack/defense ")