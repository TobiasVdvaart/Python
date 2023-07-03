import time
from termcolor import colored
from data import *
import math

##################### M04.D02.O2 #####################
def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return amount / 50

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    copper = copper2gold(personCash['copper'])
    silver = silver2gold(personCash['silver'])
    gold = personCash['gold']   
    platinum = platinum2gold(personCash['platinum'])
    totaal = copper + silver + gold + platinum
    print(copper)
    print(silver)
    print(gold)
    print(platinum)
    
    
    return totaal
    
##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people, horses):
    totaal_copper_prijs = (people * COST_FOOD_HUMAN_COPPER_PER_DAY + horses * COST_FOOD_HORSE_COPPER_PER_DAY) * JOURNEY_IN_DAYS
    totaal_gold_prijs = totaal_copper_prijs / 50
    return totaal_gold_prijs

##################### M04.D02.O5 #####################

def getFromListByKeyIs(lst:list, key:str, value:any) -> list:
    return [x for x in lst if x.get(key) == value]

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends:list, people:list) -> list:
    adventuring_people = getAdventuringPeople(people)
    share_with_friends = getShareWithFriends(friends)
    return [x for x in adventuring_people if x in share_with_friends]

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people: int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people: int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses: int, tents: int) -> float:
    Horse_totale_berekening = (horses * COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS
    totaal_horse = silver2gold(Horse_totale_berekening)
    Tent_totale_berekening = tents * COST_TENT_GOLD_PER_WEEK * 2
    total_cost = totaal_horse + Tent_totale_berekening
    return total_cost


##################### M04.D02.O7 #####################

def getItemsAsText(items: list) -> str:
    items_as_text = []
    for item in items:
        item_text = f"{item['amount']}x {item['name']}"
        if item.get('unit'):
            item_text += f" ({item['amount']}{item['unit']} {item['name']})"
        items_as_text.append(item_text)
    return ", ".join(items_as_text)

def getItemsValueInGold(items: list) -> float:

    for item in items:
        if 'price' in item and 'amount' in item['price'] and 'type' in item['price']:
            amount = item['price']['amount']
            item_type = item['price']['type']
            total_price += amount
    return total_price, item_type




##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    price = 0
    for y in people:
        price += platinum2gold(y['cash']['platinum'])
        price += y['cash']['gold']
        price += silver2gold(y['cash']['silver'])
        price += copper2gold(y['cash']['copper'])
    return price


##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    intresting_inverstors = []
    
    for x in investors:
        if x['profitReturn'] <= 10:
            intresting_inverstors.append(x)
    return intresting_inverstors


def getAdventuringInvestors(investors:list) -> list:
    real_investors = getInterestingInvestors(investors)
    real_intresting_inverstors = getAdventuringPeople(real_investors)
    return real_intresting_inverstors


def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    resultaat = getAdventuringInvestors(investors)
    total_cost_inverstors = (JOURNEY_IN_DAYS * copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY)) + (JOURNEY_IN_DAYS * copper2gold        (COST_FOOD_HORSE_COPPER_PER_DAY)) + (JOURNEY_IN_DAYS * silver2gold(COST_HORSE_SILVER_PER_DAY)) + (2 * COST_TENT_GOLD_PER_WEEK )   
    Total_cost = total_cost_inverstors * len(resultaat)
    total_cost_gear = 0

    for y in resultaat:
        for x in gear:
            totale_berekening = x['amount'] * x['price']['amount']
            if x['price']['type'] == 'gold':
                total_cost_gear += totale_berekening
            if x['price']['type'] == 'copper':
                total_cost_gear += copper2gold(totale_berekening)
            if x['price']['type'] == 'silver':
                total_cost_gear += silver2gold(totale_berekening)
            if x['price']['type'] == 'platinum':
                total_cost_gear += platinum2gold(totale_berekening)


    Total_cost += total_cost_gear
    print(Total_cost)
    return Total_cost



##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold: float, people: int, horses: int) -> int:
    nights_for_people = leftoverGold // COST_INN_HUMAN_SILVER_PER_NIGHT
    nights_for_horses = (leftoverGold % COST_INN_HUMAN_SILVER_PER_NIGHT) // COST_INN_HORSE_COPPER_PER_NIGHT
    return min(nights_for_people, nights_for_horses)

def getJourneyInnCostsInGold(nightsInInn: int, people: int, horses: int) -> float:
    total_cost = (nightsInInn * COST_INN_HUMAN_SILVER_PER_NIGHT) + (nightsInInn * COST_INN_HORSE_COPPER_PER_NIGHT) / 100
    return round(total_cost, 2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()