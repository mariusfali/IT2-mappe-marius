class Bruker:
    """Superklasse for Brukere i skolesystemet. Skal ikke brukes direkte.
    
    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn

    """
    def __init__(self, epost, fornavn, etternavn):
        self._epost = epost
        self._fornavn = fornavn
        self._etternavn = etternavn
        
    def logg_inn(self):
        print(f"{self._epost} logget inn")

    def logg_ut(self):
        print(f"{self._epost} logget ut")

class Laerer(Bruker):
    """En subklasse til Brukere, men også en superklasse for Lærere i skolesystemet. Skal ikke brukes direkte.
    
    Attributes:
        epost: En string med lærerens epost
        fornavn: En string med lærerens fornavn
        etternavn: En string med lærerens etternavn
        lonnskonto: Et serienummer (int) med lærerens lønnskonto

    """
    def __init__(self, epost, fornavn, etternavn, lonnskonto):
        super().__init__(epost, fornavn, etternavn)
        self._lonnskonto = lonnskonto

class Elev(Bruker):
    """En subklasse til Bruker for Elever.
    
    Attributes:
        epost: En string med elevens epost
        fornavn: En string med elevens fornavn
        etternavn: En string med elevens etternavn
        trinn: Et tall (int) med elevens skoletrinn.
        klasse: En string med elevens klasse
    
    """
    def __init__(self, epost, fornavn, etternavn, trinn, klasse):
        super().__init__(epost, fornavn, etternavn)
        self._trinn = trinn
        self._klasse = klasse
        self._fag = []

    def lever_egenmleding():
        pass

class Faglaerer(Laerer):
    """En subklasse til Laerer for faglærere.
    Attributes:
        epost: En string med lærerens epost
        fornavn: En string med lærerens fornavn
        etternavn: En string med lærerens etternavn
        lonnskonto: Et serienummer (int) med lærerens lønnskonto

    """
    def __init__(self, epost, fornavn, etternavn, lonnskonto):
        super().__init__(epost, fornavn, etternavn, lonnskonto)
        self._kompetanse = []
        self._klasser = []

    def sett_karakter(self):
        pass

class Kontaktlaerer(Laerer):
    """En subklasse til Laerer for kontaktlærere.
    
    Attributes:
        epost: En string med lærerens epost
        fornavn: En string med lærerens fornavn
        etternavn: En string med lærerens etternavn
        lonnskonto: Et serienummer (int) med lærerens lønnskonto
        klasse: En string med lærerens klasse 
        trinn: Et tall (int) med lærerens undervisningstrinn

    """
    def __init__(self, epost, fornavn, etternavn, lonnskonto, klasse, trinn):
        super().__init__(epost, fornavn, etternavn, lonnskonto)
        self._klasse = klasse
        self._trinn = trinn
        
    def fiks_fravaer(self):
        pass

# Denne brukes for testing, betyr at koden inne i if-setningen kun kjøres hvis 
# vi "trykker" play på denne filen eller kjører denne fila i terminalen
if __name__ == "__main__":
    ravi = Laerer("ravim@viken.no", "David Ravi", "Manikarnika", 9700340022936)
    ravi.logg_inn()
    ravi.logg_ut()

    camilla = Elev("camillac@kkg.no", "Camilla", "Coward", 2, "STG")
    camilla.logg_inn()
    camilla.logg_ut()

