# Gjenbrukbar kode

Når man snakker om gjenbrukbar kode, snakker man hovedsakelig om to ting. Det første er dokumentasjon av kode som gjør det lettere å forstå eller bruke igjen senere. Det andre er mer generelt og tar for seg ting man skriver én gang som man kan bruke om igjen flere ganger. Dette kan være alt fra programmer og faktisk kode (for eksempel funksjoner eller databaser), til snippets og andre "shortcuts".

## Eksempler

### Eksempel 1 - dokumentasjon

```python
class Pokemon:
    """En klasse for pokemons.
    
    Attributes:
        navn: En string med pokemonens navn
        type: En string med pokemonens hoved/første type
        helsepoeng: Et tall (int) med pokemonens totale helse
        angrep: Et tall (int) med pokemonens angrepsskade
        forsvar: Et tall (int) med pokemonens forsvarsmengde

    """
    def __init__(self, navn, type, helsepoeng, angrep, forsvar):
        self._navn = navn
        self._type = type
        self._helsepoeng = helsepoeng
        self._angrep = angrep
        self._forsvar = forsvar
```

### Eksempel 2 - snippet

```json
{
	// Place your global snippets here. Each snippet is defined under a snippet name and has a scope, prefix, body and 
	// description. Add comma separated ids of the languages where the snippet is applicable in the scope field. If scope 
	// is left empty or omitted, the snippet gets applied to all languages. The prefix is what is 
	// used to trigger the snippet and the body will be expanded and inserted. Possible variables are: 
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. 
	// Placeholders with the same ids are connected.
	// Example:
	// "Print to console": {
	// 	"scope": "javascript,typescript",
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
		"Lag python-klasse": {
		"scope": "python",
		"prefix": "class",
		"body": [
			"class $1:",
			"    def __init__(self, $2, $3):",
			"        self._$2 = $2",
			"        self._$3 = $3"
		],
		"description": "Lag en Python-klasse"
	}
}
```

### Eksempel 3 - funksjoner i et program

```python
def finn_gjennomsnittet(liste):
    total = 0
    for i in liste:
        total += i
    gjennomsnittet = total/len(liste)
    return gjennomsnittet

print(finn_gjennomsnittet([1,4,72,6,3]))

print(finn_gjennomsnittet([1,2,3,4]))
```

## [Bruk i større program](/../../Skole/vg2/IT1/Prosjekt%20flask/app.py)
