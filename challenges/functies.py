EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. 
Ik kan veel dingen maken met programmeren. Ik kan een website maken. 
Ik kan een spel maken. Ik kan een chatbot maken. 
Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. 
De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. 
Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

DIFFICULT_TEXT = """Programmeren is een geweldige activiteit, die je in staat stelt om je creativiteit, 
logica en probleemoplossend vermogen te gebruiken, om allerlei soorten applicaties te maken, 
die nuttig, vermakelijk of zelfs levensveranderend kunnen zijn, afhankelijk van je doel en publiek. 
Het is ook een uitdagende bezigheid, die je voortdurend leert om nieuwe talen, technieken en concepten te leren, 
die je helpen om je code efficiënter, eleganter en robuuster te maken, zonder dat je je ooit hoeft te vervelen of te herhalen. 
Bovendien is het een leuke hobby, die je veel voldoening en plezier kan geven, als je ziet hoe je ideeën tot leven komen op het scherm, als je de interactie met je gebruikers ziet of 
als je de reacties van je vrienden en familie ziet, als je ze verrast met je eigen creaties.
"""

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

# depending on the type of text you wish you get an easy, difficult or text from file.
def getText(choice: str) -> str:
    if choice == 'easy':
        return EASY_TEXT
    elif choice == 'difficult':
        return DIFFICULT_TEXT
    else:
        return getFileContentAsString(choice)

def getFileContentAsString(textFile: str) -> str:
    with open(textFile, 'r') as file:
        content = file.read()
    return content



# opdracht 1
def getNumberOfCharacters(text: str) -> int:
    Karakters = 0
    for x in text:
        if x in ALLOWED_IN_WORD:
            Karakters += 1
    return Karakters

# opdracht 2
def getNumberOfSentences(text: str) -> int:
    aantal_karakters = 0
    for x in text:
        if x == "!":
            aantal_karakters += 1
        elif x == "?":
            aantal_karakters += 1
        elif x == ".":
            aantal_karakters += 1    
    return aantal_karakters

# opdracht 3
def getNumberOfWords(text: str) -> int:
        words = text.split()
        return(len(words))

# opdracht 5
def getAVIresults(text: str) -> int:
    punten = 0
    gemiddeld = getNumberOfWords(text) / getNumberOfSentences(text)
    if gemiddeld <= 7.4:
        punten = 5
    elif gemiddeld > 7.4 and gemiddeld <= 8.4:
        punten = 6
    elif gemiddeld > 8.4 and gemiddeld <= 9.4:
        punten = 7
    elif gemiddeld > 9.4 and gemiddeld <= 10.4:
        punten = 8
    elif gemiddeld > 10.4 and gemiddeld <= 11.4:
        punten = 11
    elif gemiddeld > 11:
        punten = 12

    return punten