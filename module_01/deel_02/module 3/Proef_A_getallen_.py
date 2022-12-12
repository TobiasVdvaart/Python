import random
abs



getal_1 = abs(random.randint(1,1000))
print(getal_1)
punten = 0

Vraag_1 = input("Wilt u beginnen, ")
while Vraag_1 == "ja":
    for x in range(20):
        for x in range(10):
            Vraag_2 = int(input("raad het getal, "))
            if Vraag_2 == getal_1:
                    getal_1 = random.randint(1, 1000)
                    punten = punten + 1
                    print(getal_1)
                    print("u heeft het goed! ")
                    Vraag_4 = input("wil je nog een ronde? ")
                    if Vraag_4 == "nee":
                        print(f"u heeft punten, {punten}! ")
                        quit()
                            
                    else:
                        print(f"u heeft punten, {punten}! ")
                        continue

            verschil_geraden = abs(Vraag_2 - getal_1)
            if Vraag_2 > getal_1:
                print('lager')
            elif Vraag_2 < getal_1:
                print('hoger')
            if verschil_geraden <= 20:
                print('je bent heel warm')
            elif verschil_geraden <= 50:
                print('je bent warm')
        Vraag_4 = input("wil je nog een ronde? ")
        if Vraag_4 == "nee":
            print(f"u heeft punten, {punten}! ")
            quit()
                
        else:
            print(f"u heeft punten, {punten}! ")
            continue









else:
    quit