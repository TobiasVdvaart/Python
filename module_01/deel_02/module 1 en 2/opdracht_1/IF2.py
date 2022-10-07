from ctypes.wintypes import PCHAR
from subprocess import CREATE_NEW_CONSOLE


vraag = input('concole of pc')
vraag2 = input('bent u member')

if vraag == 'pc':
    print ('45')
    if vraag2 == 'ja':
        print ('30')

if vraag == 'concole':
    print ('dat word dan 60 euro')
    if vraag2 == 'nee':
        print ('geen korting')