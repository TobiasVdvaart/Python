geheim_woord = "buvesa"
gok = ""
gok_teller = 0
gok_limiet = 3
einde_van_gokken = False

while gok != geheim_woord and not einde_van_gokken:
    if gok_teller < gok_limiet:
        gok = input("Raad het geheim woord: ")
        gok_teller += 1
    else:
        einde_van_gokken = True

if einde_van_gokken:
    print("Game over! Je verliest het spel.")
else:
    print("Proficiat! Je hebt het geheime woord geraden.")
