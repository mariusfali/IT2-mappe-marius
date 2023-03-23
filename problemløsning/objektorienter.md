# Objektorienterte programmer med klasser, arv og objekter

Objektorientere programmer består hovedsakelig av klasser og objekter. I tillegg kan man bruke arv slik at man ikke behøver å skrive samme kode flere ganger. Det er en måte å programmere på som er veldig effektiv for spill og/eller programmer med "ting" som har faste egenskaper (for eksempel brukere, objekter eller noe som trenger struktur). Det handler om funksjonalitet i programmet og at man fokuserer på hvordan "tingene" i programmet funker i forhold til hverandre.


## Klasser

Klasser er det første og mest essensielle i objektorientert programmering. Det er "hovedstrukturen" i programmet. I klassene definerer man både en `__init__` som er konstruktøren, men også en `self` og eventuelt andre variabler man ønsker å ha med i klassen. Man kan også ha andre metoder som for eksempel `__str__` eller `def hva_enn_du_vil(self)` som spiller hver sin rolle i programmets helhet.

### Eksempel 1:

```python
class Bruker:
    """Superklasse for Brukere i skolesystemet. Skal ikke brukes direkte.
    
    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn

    """
    # Alt i rødt her er dokumentasjon som er informasjon om klassen som vises når man skriver den i python.

    def __init__(self, epost, fornavn, etternavn):
        self._epost = epost
        self._fornavn = fornavn
        self._etternavn = etternavn
        
    def logg_inn(self):
        print(f"{self._epost} logget inn")

    def logg_ut(self):
        print(f"{self._epost} logget ut")
```

### Eksempel 2:

```python
class Planet():
    def __init__(self, navn, radius, avstand):
        self.navn = navn
        self.radius = radius
        self.avstand = avstand

    def __str__(self):
        return f"Navn: {self.navn}, Radius: {self.radius} km, Avstand fra sola: {self.avstand} millioner km"
```


## Arv

Arv er noe som kan brukes i objektorientert programmering for å gjenbruke tidligere kode og unngå å skrive samme kode flere ganger. Det er effektivt for å spare tid, og det får koden til å se mer ryddig ut. Det er ikke nødvendig, men sterkt anbefalt dersom man har store programmer med mye repetisjon

### Eksempel 1

```python
class Barnebillett(Billett): # Inne i parantesen her skriver man den klassen man ønsker å arve fra
    def __init__(self):
        super().__init__() # Dette er "arv-konstruktøren"
        self.pris = self.pris * 0.5
```

### Eksempel 2

```python
class Faglaerer(Laerer):
    """En subklasse til Laerer for faglærere.
    Attributes:
        epost: En string med lærerens epost
        fornavn: En string med lærerens fornavn
        etternavn: En string med lærerens etternavn
        lonnskonto: Et serienummer (int) med lærerens lønnskonto

    """
    def __init__(self, epost, fornavn, etternavn, lonnskonto):
        super().__init__(epost, fornavn, etternavn, lonnskonto) # Her skriver man også de variablene man ønsker å sende med fra klassen man arver fra
        self._kompetanse = []
        self._klasser = []

    def sett_karakter(self):
        pass
```


## Objekter

Objekter er det man lager med klassene, det "fysiske" objektet. Disse brukes da som faktiske ting i programmet som har direkte funksjoner eller hensikter, ofte for å representere noe eller noen. Objekter kan også endres og krysses på tvers, og man kan bruke informasjonen i ett objekt til å endre eller lage et annet objekt. Objekter lagres i minnet og tar plass.

### Eksempel 1

```python
fredrik = Faglaerer("fredrikg@viken.no", "Fredrik", "Gade", 5432344920)
```

### Eksempel 2

```python
jorda = Planet("Jorda", 6371, 149.87)
merkur = Planet("Merkur", 2439.7, 48.532)
venus = Planet("Venus", 6051.8, 107.64)
```