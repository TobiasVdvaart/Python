dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")


for x in dagen:
    print(x)

print()

print("werkdagen, ")
for y in range(1, 5):
    print(dagen[y])

print()
print("weekend, ")
for t in range(5, 7):
    print(dagen[t])

print()
print("werkdagen omgekeerd,")
for s in range(4, -1, -1):
    print(dagen[s])

print()
print("weekend omgekeerd,")
for s in range(5, -6, -6):
    print(dagen[s])
