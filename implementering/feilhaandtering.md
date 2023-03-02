# Vern mot kjøretidsfeil og logiske feil i programmer

## Kjøretidsfeil

Håndtering av kjøretidsfeil i Python gjøres med nøkkelordene try og except.
Python forsøker å kjøre kodeblokken som ligger under `try:`, hvis Python får en feilmelding, vil den kjøre kodeblokken som ligger under `except:`.

```python
try:
    alder = int(input("Alder: "))
    fodselsaar = 2022 - alder
    print(f"Fødselsår: {fodselsaar}")
except:
    print(f"Feil: Alder må være et heltall")

print("koden fortsetter")
```

### Eksperttips: While-løkke med try-except

```python
while True:
    try:
        alder = int(input("Alder: "))
        break
    except:
        print("Alder må være et heltall, prøv igjen")
fodselsaar = 2022 - alder
print(f"fødselsår: {fodselsaar}")
```

## Logiske feil i programmer

For å oppdage logiske feil i python-programmer kan vi bruke nøkkelordet `assert` for å forsikre oss om at koden gir korrekte resultat.

Eksempel:

```python
assert 10 > 5 # 10 er større enn 5, derfor gjør denne ingenting
assert 10 > 20 # 10 er ikke større enn 20, derfor gir denne en 
```

Eksempel: Test av funksjoner med assert

```python
def areal(hoyde, bredde):
    return hoyde*bredde

def omkrets(hoyde, bredde):
    return hoyde + hoyde + bredde + bredde

assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12
assert omkrets(3,2) == 10
assert omkrets(3,3) == 12
assert omkrets(3,4) == 14
```

### Eksperttips: Håndtering av kjøretidsfeil og logisk feil

```python
while True:
    try:
        alder = int(input("Alder: "))
        assert alder >= 0
        break
    except:
        print("Alder må være et positivt heltall, prøv igjen")
fodselsaar = 2022 - alder
print(f"fødselsår: {fodselsaar}")
```
