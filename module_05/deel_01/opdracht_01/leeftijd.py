Names = []
Ages =  []


def get_name_and_age():
    while True:
        name = input("Wat is je naam? ")
        Names.append(name)
        if name == "stop":
            Names.pop(-1)
            break
        age = int(input("Wat is je leeftijd? "))
        Ages.append(age)

    print(Names)
    print(Ages)

(get_name_and_age())