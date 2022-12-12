# getal = 3-6
# print(getal)

# getal_2 = 6-3
# print(getal_2)

# print(abs(getal))
# print(abs(getal_2))



# while True:
#     naam = input("wat is je naam? ")
#     if naam == "noa":
#         continue 
#     print(f"je bent geweldig {naam} ")
#     if naam == "stop":
#         break
# print("noa je bent geweldig")

mijn_namen_lijst = {}

while True:
    naam = input("wat is je naam (stop)")

    if naam == "stop":
        break

    if naam in mijn_namen_lijst:
        if input("wilt u bijwerken?") != "ja":
            continue
    leeftijd = int(input("wat is uw leeftijd"))
    if leeftijd in mijn_namen_lijst:
        print("er zit al iemand in met die leeftijd")
    mijn_namen_lijst.update({naam : leeftijd})
print(mijn_namen_lijst) 


