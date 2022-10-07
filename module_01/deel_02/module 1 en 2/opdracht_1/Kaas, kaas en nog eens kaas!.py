geel = input("Is de kaas geel? ")

if geel == "nee":
    schimmel = input("heeft de kaas blauwe schimmel?")

    if schimmel == "ja":
        korst = input("heeft de kaas een korst? ")

        if korst == "ja":
            print("Blue de Rochbaron")

        else:
            print("Foume d'Ambert")

    else:
        korst1 = input("heeft de kaas een korst? ")

        if korst1 == "ja":
            print("Camembert")

        else:
            print("Mozzarella")

if geel == "ja":
    gaten = input("Zitten er gaten in? ")

    if gaten == "ja":
        duur = input("Is de kaas belachelijk duur? ")
        if duur == "gemiddeld":
            print ("goudse kaas")


        elif duur == "ja":
            print("Emmenthaler")

        else:
            print("Leerdammer")

    else:
        steen = input("Is de kaas hard als steen? ")

        if steen == "ja":
            print("Parmigiano Reggiano")

        else:
            print("Goudse kaas")

