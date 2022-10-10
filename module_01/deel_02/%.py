bedrag = int(input('voer bedrag centen in')) 

euro_2 = bedrag // 200
print(f'aantal 2 euro: {euro_2}')
restant = bedrag - euro_2 * 200
euro_1 = restant // 100
print (f'aantal 1 euro: {euro_1}')
restant = restant - euro_1 * 100
euro_050 = restant // 50
print (f'aantal 50 cent: {euro_050}')


print (restant)