bedrag = int(input('voer bedrag centen in')) 

euro_2 = bedrag // 200
print(f'aantal 2 euro: {euro_2}')
restant = bedrag - euro_2 * 200
euro_1 = restant // 100
print (f'aantal 1 euro: {euro_1}')
print (restant)