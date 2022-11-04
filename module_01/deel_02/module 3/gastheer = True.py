gastheer = True
gasten = True
drank = True
chips = True


if (gastheer and drank) or (gasten and drank and chips) or (gasten and drank and chips and gastheer):

    print('start the party')

else:

    print('No party')

