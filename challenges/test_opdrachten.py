EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. 
Ik kan veel dingen maken met programmeren. Ik kan een website maken. 
Ik kan een spel maken. Ik kan een chatbot maken. 
Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. 
De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. 
Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"


def getNumberOfCharacters(text: str) -> int:
    for letters in text:
        ALLOWED_IN_WORD_NEW = ALLOWED_IN_WORD.replace('_-', '')
        return len(ALLOWED_IN_WORD_NEW)
print  (getNumberOfCharacters(text=ALLOWED_IN_WORD))



def getNumberOfSentences(text: str) -> int:
    counter = text.count(".")
    return (len(counter))



def getNumberOfWords(text: str) -> int:
        words = text.split()
        return(len(words))
