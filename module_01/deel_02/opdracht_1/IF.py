from operator import le


naam = input('goedendag wat is uw naam?')
leeftijd = int(input('hoe oud bent u?'))

if leeftijd < 18: 
    print (f'helaas {naam} u mag niet naar binnen')
    if naam == 'tobias':
        print (f'je krijgt een vrijkaart.')
    else:
        print(f'je krijgt een sticker')
elif leeftijd >= 18 and leeftijd < 21:
    print (f'goedendag {naam} kom binnen, u mag nog geen sterke drank kopen.')
else:
    print (f"goedendag {naam} u mag naar binnen hoe kan ik u helpen?")






