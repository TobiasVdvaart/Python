leeg_string = 0
antwoord = 0

def get_float_int(vraag: str):
    while True:
        vraag_getal = input(vraag)
        try:
            getal = float(vraag_getal)
            break
        except ValueError:
            print('voer getal 1 in')
    return getal

def addition(number1, number2):
    antwoord_plus = number1 + number2
    return antwoord_plus


def subtraction(number1, number2):
    antwoord_min = number1 - number2
    return antwoord_min

def multiplication(number1, number2):	
    antwoord_keer = number1 * number2
    return antwoord_keer

def division(number1, number2):
    antwoord_delen = number1 / number2
    
    return antwoord_delen

teller = 0

while True:
    choice = input('wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren?, (typ stop in als je wilt stoppen)')


    if choice == 'E' or choice == 'F' and teller < 1:
        nummer2 = 1
        nummer1 = get_float_int('voer getal 1 in')
    if choice == 'E' or choice == 'F' and teller >= 1:
        nummer2 = 1
        nummer1 = antwoord
    elif choice == 'G' or choice == 'H' and teller <1:
        nummer2 = 2
        nummer1 = get_float_int('voer getal 1 in')
    elif choice == 'G' or choice == 'H' and teller >=1:
        nummer2 = 2
        nummer1 = antwoord
    elif choice == 'stop':
        break
    elif choice != '' and teller < 1:
        nummer1 = get_float_int('voer getal 1 in')
        nummer2 = int(input('vul getal 2 in!'))
    elif choice != '' and teller >= 1:
        nummer1 = antwoord
        nummer2 = int(input('vul getal 2 in!'))



    if choice == 'A':
        plus = (addition(nummer1, nummer2))
        print(plus)
        antwoord = plus
    elif choice == 'B':
        min = (subtraction(nummer1, nummer2))
        print(min)
        antwoord = min
    elif choice == 'C':
        keer = (multiplication(nummer1, nummer2))
        print(keer)
        antwoord = keer
    elif choice == 'D':
        delen = (division(nummer1, nummer2))
        print(delen)
        antwoord = delen
    elif choice == 'E':
        print(nummer1 + nummer2)
        antwoord = antwoord + nummer2
    elif choice == 'F':
        print(nummer1 - nummer2)
        antwoord = antwoord - nummer2
    elif choice == 'G':
        print(antwoord * nummer2)
        antwoord = antwoord * 2 
    elif choice == 'H':
        print(antwoord / nummer2)
        antwoord = antwoord / 2
    
    
    


    teller += 1