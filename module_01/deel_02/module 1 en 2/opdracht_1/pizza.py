




from logging import exception


try:
    pizza_klein_prijs = 9.95
    pizza_medium_prijs = 15.34
    pizza_groot_prijs = 22.87
    pizza_klein_amount = int(input("[-] Hoeveel small pizza's wilt u hebben? : "))
    pizza_medium_amount = int(input("[-] Hoeveel medium pizza's wilt u hebben? : "))
    pizza_groot_amount = int(input("[-] Hoeveel Large pizza's wilt u hebben? : "))
    pizza_klein_total_price = pizza_klein_prijs * pizza_klein_amount
    pizza_medium_total_price = pizza_medium_prijs * pizza_medium_amount
    pizza_groot_total_price = pizza_groot_prijs * pizza_groot_amount
    pizza_total_price = pizza_klein_total_price + pizza_medium_total_price + pizza_groot_total_price
except ZeroDivisionError:
    print('u kunt geen 0 pizza bestellen')

except exception:
    print('er is iets fout gegaan')


print (f"""
U heeft :
=========================================
{pizza_klein_amount} Small pizza {pizza_klein_total_price}€)
{pizza_medium_amount} Medium pizza ({pizza_medium_total_price}€)
{pizza_groot_amount} Large pizza ({pizza_groot_total_price}€)
==========================================
In Totaal kost het : ({pizza_total_price}€)
""")

round (pizza_groot_prijs, 2)
round (pizza_klein_total_price, 2)
round (pizza_medium_total_price, 2)
round (pizza_total_price, 2)

print ("dankuwel en een fijne dag!")