
def fibo_lijst(fibo_lijst1: [], vraag: int) -> int:
    teller = 0
    teller2 = 1
    
    for x in range(vraag - 2):
        getal_1 = fibo_lijst1[teller]
        getal_2 = fibo_lijst1[teller2]
        antwoord = getal_1 + getal_2
        fibo_lijst1.append(antwoord)
        teller += 1
        teller2 += 1
    print(fibo_lijst1)
    gulden_snede = antwoord / getal_2
    return gulden_snede


start = [0, 1]
vraag_getal = int(input('geef een getal!'))
 


gulden_snede = fibo_lijst(start, vraag_getal)
print(gulden_snede)
