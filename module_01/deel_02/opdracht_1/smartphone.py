##########variable########################
iphone = int(input('hoe duur is de iphone?'))
samsung = int (input('hoe duur is de samsung'))
zenfone = int(input('hoe duur is de zenphone'))
verschil_iphone = iphone-samsung
verschil_samsung = samsung-iphone
verschil_zenphone1 = zenfone-iphone 
verschil_zenphone2 = zenfone-samsung


#################IF########################


if samsung > 900:
    print(f'het advies is geen telefoon te kopen omdat het buiten het budget valt')

if iphone >900:
    print(f'het advies is geen telefoon te kopen omdat het buiten het budget valt')

if samsung < iphone:
    print(f'de samsung is het goedkoopst, hij kost {samsung} euro ')

if samsung >= iphone:
    print (f"de samsung is het duurst , hij kost {samsung} euro")

if iphone < samsung:
    print (f'de ihone is het goedkoopst hij kost {iphone} euro ')
    
if iphone >= samsung:
    print (f"de iphone is het duurst , hij kost {iphone} euro")


if iphone < samsung:
    print(f'het advies is dus de iphone te kopen omdat het {verschil_iphone} euro goedkoper is')

if samsung < iphone:
    print(f'het advies is de samsung te kopen omdat het verschil {verschil_samsung} euro goedkoper is ')

if samsung == iphone:
    print('de telefoons zijn even duur als u van zakelijk houd zou ik voor de iphone gaan maar als u meer van fotos maken bent zou ik de samsung halen')



