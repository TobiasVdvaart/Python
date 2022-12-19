import random 

kleuren = ["harten", "klaveren", "schoppen", "ruiten"]
kaart_soorten = [ "boer", "vrouw", "heer", "aas"]
deck = []
hand = []


for kleur in kleuren:
    for soort in kaart_soorten:
        kaart = kleur + "" + soort
        deck.append(kaart)
    for x in range(2, 11):
        kaart = kleur + soort + "" + str(x)
        deck.append(kaart)
deck.append("joker_1")
deck.append("joker_2")
random.shuffle(deck)


for x in range(7):
    kaarten_hand = deck.pop()
    hand.append(kaarten_hand)


print(f"Uw deck is, {deck} ")   
print(f"Uw kaarten zijn, {hand} ")   







    