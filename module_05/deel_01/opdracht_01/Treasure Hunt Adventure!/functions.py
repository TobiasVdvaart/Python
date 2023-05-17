import time
from termcolor import colored
from data import *
import math

##################### M04.D02.O2 #####################
def copper2silver(amount: int) -> float:
    copper = amount/10
    return float(copper)
    

def silver2gold(amount:int) -> float:
    silver = amount/5
    return float(silver)
    

def copper2gold(amount:int) -> float:
    gold = amount/50
    return float(gold)
    

def platinum2gold(amount:int) -> float:
    platinum = amount*25
    return float(platinum)
    

def getPersonCashInGold(personCash:dict) -> float:
    platinum = personCash['platinum'] * 25
    gold = personCash['gold']
    copper = personCash['copper']/50
    silver = personCash['silver']/5
    personCash = platinum + gold + copper +silver
    return personCash
    
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
    Horse_Berekening = (horses * COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS
    totaal_horse = silver2gold(Horse_Berekening)
    Tent_Berekening = tents * COST_TENT_GOLD_PER_WEEK * 2
    total_cost = totaal_horse + Tent_Berekening
    return total_cost


##################### M04.D02.O7 #####################

def getItemsAsText(items: list) -> str:
    Items_naar_text = []
    for item in items:
        item_text = f"{item['amount']}x {item['name']}"
        if item.get('unit'):
            item_text += f" ({item['amount']}{item['unit']} {item['name']})"
        Items_naar_text.append(item_text)
    return ", ".join(Items_naar_text)

def getItemsValueInGold(items:list) -> float:
    pass

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

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