import matplotlib.pyplot as plt
fil = open("kolsaas.csv")
data = fil.read()
#print(data)

linjer = data.split("\n")
#print(linjer)
tur = []
for linje in linjer:
    splittet_linje = linje.split(",")
    tur.append(splittet_linje)
#print(tur)
print(tur[0][1])

x = []
y = []
lengde = []
bredde = []

for i in tur[1:]:
    x.append(float(i[0]))
    y.append(float(i[3]))
    lengde.append(float(i[2]))
    bredde.append(float(i[1]))

plt.plot(x, y)
plt.xlabel("Tid")
plt.ylabel("Høyde")
plt.show()