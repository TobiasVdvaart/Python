

#stap 1/2/3/4
vraag1 = float(input("hoelang is de zembad? "))
vraag2 = float(input("hoe breed is de zwembad? "))
vraag3 = float(input("hoe diep is de zwembad? "))
voorrijs_afstand = float(input('hoever woont u?'))




berekening1 = (vraag1*vraag2*vraag3)
kostenuitgraven = 25*berekening1
kostenafvoer = 32.50*berekening1
totaalkost = kostenuitgraven + kostenafvoer + voorrijs_kosten


print(f' de inhoud van uw zwembad is:      ${berekening1} ')
print(f'uw uitgraaf kosten zijn:           ${kostenuitgraven} ')
print(f'uw afvoer kosten zijn:             ${kostenafvoer} ')
print(f'uw voorrijs kosten zijn:           ${voorrijs_kosten} ')
print(f'uw totaal kosten zijn:             ${totaalkost} ')

