import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8, 10]

plt.plot(x, y) # Oppretter et plott
#plt.show() # Viser plottet

# Plott funksjonen f(x) = 3*x + 2, med x fra 0 til 5

x = []
y = []

def f(x):
    return 3*x + 2

for i in range(6):
    x.append(i)
    y.append(f(i))

plt.plot(x, y)
plt.scatter(x, y) # Prikker for hvert punkt i stedet for én strek
plt.show()