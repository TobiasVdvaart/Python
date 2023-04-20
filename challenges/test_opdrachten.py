EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. 
Ik kan veel dingen maken met programmeren. Ik kan een website maken. 
Ik kan een spel maken. Ik kan een chatbot maken. 
Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. 
De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. 
Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"



def getNumberOfCharacters(text: str) -> int:
    for words in text:
        words.replace('_-', '')
        words = text.isalpha()
    return words



def getNumberOfSentences(text: str) -> int:
    counter = text.count(".")
    return (len(counter))



def getNumberOfWords(text: str) -> int:
        words = text.split()
        return(len(words))


def getNumberOfCharacters(text: str) -> int:
    aantal = 0
    return len(text) + aantal


# nieuwe zinnen opdracht voor ?, !, .
def getNumberOfCharacters(text: str) -> int:
    Karakters = 0
    for x in text:
        if x == "!":
            Karakters += 1
        if x == "?":
            Karakters += 1
        if x == ".":
            Karakters += 1    
    return Karakters


# oude opdracht
def getNumberOfCharacters(text: str) -> int:
    Karakters = 0
    for x in text:
        if x.isalpha():
            Karakters += 1
    return Karakters