def finn_gjennomsnittet(liste):
    total = 0
    for i in liste:
        total += i
    gjennomsnittet = total/len(liste)
    return gjennomsnittet

print(finn_gjennomsnittet([1,4,72,6,3]))

print(finn_gjennomsnittet([1,2,3,4]))




# logisk feil i kalkulator ting
# brukervennlighet i programmer
# pygame lagg på try again