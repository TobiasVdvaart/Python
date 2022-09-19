a = int(input('vul het getal hier voor A: '))
b = int(input('vul het getal hier voor B: '))

if a > b:
    max = a
    min = b 
    print ('a is het grootste getal ' + str(max))
elif a < b:
    min = a
    print('a is het kleinste getal ' , min)
    max = b
else: 
    print('a en b zijn even groot')  
    max = a
    min = b  

print("Het minimum is:" ,min)  
print("Het maximum is:" ,max) 