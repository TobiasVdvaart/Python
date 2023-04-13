import time
from termcolor import colored
from data import *

##################### M04.D02.O2 #####################

def copper2silver(amount: int) -> float:
   return amount/10
    

def silver2gold(amount:int) -> float:
    return amount/5

def copper2gold(amount:int) -> float:
    return amount/50

def platinum2gold(amount:int) -> float:
    return amount*25

def getPersonCashInGold(cash: dict) -> float:
    goldValue = 0
    goldValue += cash.get("copper", 0) / 100.0
    goldValue += cash.get("silver", 0) / 10.0
    goldValue += cash.get("gold", 0)
    goldValue += cash.get("platinum", 0) * 10.0
    return goldValue
##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(aantal_mensen, aantal_paarden):
    totaal_copper = (aantal_mensen * kosten_copper_per_day + aantal_paarden * kosten_eten_paard_kopper) * journey_in_dagen
    totaal_gold = totaal_copper / 50
    return totaal_gold

##################### M04.D02.O5 #####################

def getFromListByKeyIs(lst:list, key:str, value:any) -> list:
    return [dct for dct in lst if dct.get(key) == value]

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends:list) -> list:
    adventuring_people = getAdventuringPeople(friends)
    share_with_friends = getShareWithFriends(friends)
    return [person for person in adventuring_people if person in share_with_friends]

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    pass

def getNumberOfTentsNeeded(people:int) -> int:
    pass

def getTotalRentalCost(horses:int, tents:int) -> float:
    pass

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    pass

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