grootste = 0
kleinste = 1000
for x in range(10):
    getal = int(input("vul uw getallen in "))
    if getal < kleinste:
        kleinste = getal
    if getal > grootste:
        grootste = getal
    if getal % 3 == 0:
        aantaldeel = aantaldeel + 1
print(f"het grootste getal is(0-1000): {grootste} ")
print(f"het kleinste getal is(0-1000): {kleinste} ")
print(f"getallen die je kan delen door 3 (zonder rest): {aantaldeel} ") 
