# Presentere data

Med data mener vi all mulig informasjon, det kan f.eks. være temperaturer, tekst, bilder, filmer.

I IT2 lærer vi om to forskjellige måter å presentere data på, nemlig ved tegning av grafer og med nettsider.

## Tegne grafer

For å tegne grafer i Python kan vi bruke biblioteket `matplotlib`.

> Installere matplotlib: `pip install matplotlib`

## Lage nettsider (HTML/Flask)

## Eksempler

```python
import matplotlib.pyplot as plt

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
```

### Eksperttips: Man kan bruke linspace fra numpy

```python
import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return x**2

xverdier = np.linspace(0, 10, 101)
yverdier = f(xverdier)

plt.plot(xverdier, yverdier)
plt.show()
```

### Eksperttips 2: Man kan "designe" grafen

```python
import matplotlib.pyplot as plt
import numpy as np

x= []
y = []

def f(x):
    return 2*x - 3

for i in range(11):
    x.append(i)
    y.append(f(i))

plt.plot(x, y, color="coral", linestyle="dotted") # Gi grafen farge og linjestil
plt.grid() # Gjøre det til en grid
plt.title("$f(x)=2x-3$") # Gi hele grafen en tittel
plt.style.use("bmh") # Bruke en stil
plt.plot(x, y)
plt.xlabel("$x$") # Gi x et navn
plt.ylabel("$y$") # Gi y et navn

plt.show()
```

## [Bruk i større program](yr-temperatur-plotting.py)

