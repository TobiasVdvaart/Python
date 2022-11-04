string = 'dsjf4?!Taf?!Ejslf?!S5is91?!Tsagjka94hj'
l1 = ''
l2 = ''
target = ''
for letter in string:
    if l1 == '?' and l2 == '!':
        target += letter
    l1 = l2
    l2 = letter

print(target)