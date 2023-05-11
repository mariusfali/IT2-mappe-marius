fil = open("./sykkelturer.csv", encoding="utf-8")
data = fil.read()
linjer = data.split("\n")

#print(linjer[1])
alle_starter = []
ulike_starter = []
alle_slutter = []
ulike_slutter = []

for i in linjer[1:-1]:
    splittet = i.split(",")
    if splittet[4] not in alle_starter:
        ulike_starter.append(splittet[4])
    alle_starter.append(splittet[4])
    if splittet[10] not in alle_slutter:
        ulike_slutter.append(splittet[10])
    alle_slutter.append(splittet[10])

ordbok_starter = {}
ordbok_slutter = {}

for i in ulike_starter:
    antall = alle_starter.count(i)
    ordbok_starter[str(i)] = antall

for i in ulike_slutter:
    antall = alle_slutter.count(i)
    ordbok_slutter[str(i)] = antall


top_tre_starter = []
top_tre_slutter = []

for i in range(3):
    key = max(ordbok_starter, key=ordbok_starter.get)
    top_tre_starter.append(key)
    print(f"{key}: {ordbok_starter[key]}")
    ordbok_starter.pop(str(key))

for i in range(3):
    key = min(ordbok_slutter, key=ordbok_slutter.get)
    top_tre_slutter.append(key)
    print(f"{key}: {ordbok_slutter[key]}")
    ordbok_slutter.pop(str(key))

#print(top_tre_starter)
#print(top_tre_slutter)
print("-------")


# 4 er start, 9 slutt
#print(alle_starter)
#print(ulike_starter)
#print(alle_slutter)
#print(ulike_slutter)



## Bedre løsning av Thor
fil = open("sykkelturer.csv", encoding="utf-8") # åpner fila
data = fil.read() # leser innholdet i fila som en string
linjer = data.split("\n")# splitter innholdet i fila på "newline" til en liste

holdeplasser = {} # en tom ordbok som skal fylles med info

for linje in linjer[1:-1]:
    splittet_linje = linje.split(",") # splitter hver linje på komma
    start = splittet_linje[4] # henter ut startholdeplass
    if start not in holdeplasser:
        holdeplasser[start] = 1
    else:
        holdeplasser[start] += 1

sortert = sorted(holdeplasser, key=holdeplasser.get, reverse=True)
hoyeste = sortert[:3]
laveste = sortert[-3:]

print("__Høyeste__")
for plass in hoyeste:
    print(f"{plass}: {holdeplasser[plass]}")

print("__Laveste__")
for plass in laveste:
    print(f"{plass}: {holdeplasser[plass]}")