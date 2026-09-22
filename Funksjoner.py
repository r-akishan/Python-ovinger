# SKRIV EN FUNKSJON SOM SKRIVER UT EN ADDRESS PÅ ET BESTEMT FORMAT
if __name__ == "__main__":

    def adresse(navn, gateadresse, postnummer, poststed):                                                                # Definerer funksjonen med 4 parametere
        adresse_tekst = f"""Til: {navn}                                                                                   
    {gateadresse}
    {postnummer} {poststed}"""                                                                                           # Skriver inn hele adresse teksten i den formaten jeg vil ved bruk av """-"""
        return adresse_tekst                                                                                             # Returnerer adresse teksten

    adressen = adresse(input("Fornavn Etternavn: "), input("Gateadresse: "), input("Postnummer: "), input("Poststed: ")) # Skriver ut funksjonen samtidig som brukeren får skrevet inn all infoen
    print(adressen)                                                                                                      # Printer ut det brukeren skriver


# LAG EN FUNKSJON SOM TAR INN TO TALL A OG B, OG RETURNERER EN BOOLSK VERDI

def delelig(a, b):                                                                                   # Definerer funksjonen med to parametere
    return a % b == 0                                                                                # Sjekker om a/b gir noen rester, hvis ikke vil den returnere med True fordi == er en boolsk uttrykk

if __name__ == "__main__":

    deling = delelig(int(input("Skriv inn en verdi for a: ")), int(input("Skriv inn en verdi for b: "))) # Setter deling er lik funksjonen og lar brukeren skrive inn to tall, printer ut funksjonen
    print(deling)


# LAG ET SCRIPT SOM BRUKER EN FUNKSJON TIL Å KONVERTERE EN SERIE MED AVSTANDER I KILOMETER TIL NAUTISKE MIL
if __name__ == "__main__":

    def serie(kilometer):                                                 # Definerer funksjonen
        nautiske_mil = 1.852                                              # Definerer nautiske mil
        konvertering = round(kilometer / nautiske_mil, 2)                 # Regner ut antall km i nautiske mil
        return f"{kilometer}km vil være lik {konvertering} nautiske mil." # Returnerer hva funksjonen skal skrive ut

    while True:                                                           # Lager en while-løkke slik at brukeren kan skrive inn antall km
        km = float(input("Kilometer: "))                                  # Brukeren kan skrive inn kilometer
        if km == 0:                                                       # Hvis brukeren skriver inn 0 så vil koden slutte å kjøre
            break
        else:                                                             # Hvis ikke vil koden fortsette å kjøre funksjonen
            print(serie(km))


# LAG EN FUNKSJON SOM TAR INN ET TALL SOM PARAMETER, SJEKKER OM TALLET ER PERFEKT OG RETURNERER SOM EN BOOLSK VERDI
#if __name__ == "__main__":

from Funksjoner import delelig                              # Importerer en funksjon fra en annen fil

def perfekt(A):                                             # Definerer en funksjon med en parameter
    faktor_sum = 1                                          # Definerer sum = 1, fordi det er alltid inkludert
    for loop in range(2, int(A/2) + 1):                     # Lager en for-løkke fra 2 til tallet/2 + 1 for å finne faktorene til parameteren
        sjekk = delelig(A, loop)                            # Sjekker om parameteren er delelig på verdiene i range()
        if sjekk == True:                                   # Hvis det er delelig vil summen øke med faktoren den fant ut
            faktor_sum = faktor_sum + loop
    return faktor_sum == A                                  # Sjekker om summen av faktorene er lik parameteren og returnerer en boolsk verdi

if __name__ == "__main__":

    tall = int(input("Sjekk om tallet er perfekt: "))  # Brukeren kan sjekke om tallet sitt er perfekt
    result = perfekt(tall)
    if result:
        print(f"{tall} er et perfekt tall.")
    else:
        print(f"{tall} er ikke et perfekt tall.")
    

# LAG EN KODE DER BRUKEREN KAN SKRIVE INN ET HELT TALL OG BRUK FUNKSJONEN OVER TIL Å SJEKKE OM TALLET ER PERFEKT
if __name__ == "__main__":

    from Funksjoner import perfekt                       # Importerer en funksjon fra en annen fil

    heltall = int(input("Sjekk om tallet er perfekt: ")) # Brukeren kan sjekke om tallet sitt er perfekt
    resultat = perfekt(heltall)                          # Kjører brukerens tall gjennom den importerte funksjonen

    if resultat:                                         # Printer ut hvis tallet er perfekt og hvis den ikke er perfekt
        print(f"{heltall} er et perfekt tall!")
    else:
        print(f"{heltall} er ikke et perfekt tall.")


# LES OG FORSTÅ FEILEN PÅ KODEN SOM SKAL SPLITTE EN REGNING I TRE KATEGORIER OG REGNER UT TOTAL PRISEN FOR HVER KATEGORI

# FEIL KODE
if __name__ == "__main__":  
     
    sum_mat = 0
    sum_drikke = 0
    sum_annet = 0

    def skriv_inn_pris():
        pris = input("Pris: ")
        if pris == "":
            return None
        try:
            pris = float(pris)                                                 # Pris er ikke returnert, verdien forblir lokal og blir borte
        except ValueError:
            print("Feilformatert pris")
            return None

    def skriv_inn_vartype():                                         
        type_vare = input("Mat (m) eller drikke (d) eller annet (a)")          # Kræsjer hvis den er tom, får IndexError 
        if type_vare[0].lower() == "m":                                        # [0] henter ut første bokstaven
            sum_mat += pris                                                    # Koden prøver å endre på de globale sumverdiene, men de er ikke definert i funksjonen
        elif type_vare[0].lower() == "d":                              
            sum_drikke += pris                                        
        else:                                                                  # Alt annet som blir skrevet regnes som annet, ikke bare a
            sum_annet += pris

    fortsetter = True
    print("Skriv inn priser p√• varer og type vare. Avslutt med negativ pris") # Overskriften for hele koden
    while fortsetter:
        skriv_inn_pris()                                                       # Funksjonen for pris returnerer ikke prisen, får derfor feilmelding
        if pris < 0.0:
            fortsetter = False
            break
        skriv_inn_vartype()                                                    
                                                                               # Sum av varer burde skrevet under med en if-setning ved bruk av definisjonen for funksjonen av varetype
    print("Sum mat: ", sum_mat)
    print("Sum drikke: ", sum_drikke)
    print("Sum annet: ", sum_annet)

# RIKTIG KODE
if __name__ == "__main__":

    sum_mat = 0                                                                             # Definerer sum_mat
    sum_drikke = 0                                                                          # Definerer sum_drikke
    sum_annet = 0                                                                           # Definerer sum_annet

    def skriv_inn_pris():                                                                   # Lager en funksjon for pris
        pris = input("Pris: ")                                                              # Brukeren kan skrive inn prisen
        if pris == "":                                                                      # Hvis brukeren ikke skriver en pris, returnerer den none
            return None
        try:                                                                                # Hvis brukeren skriver bokstaver sender den en ValueError
            pris = float(pris)
            return pris                                                                     # Returnerer prisen, slik at den kan bli hentet ut av funksjonen
        except ValueError:
            print("Feilformatert pris")
            return None
            

    def skriv_inn_varetype():                                                               # Lager en funksjon for varetype
        while True:                                                                         # Lager en while-løkke
            type_vare = input("Mat (m) eller drikke (d) eller annet (a): ").strip().lower() # Brukeren kan skrive inn hvilken type vare, fjerner mellomrom og konverterer alt til små bokstaver
            if type_vare in ["m", "d", "a"]:                                                # Lager en liste, for å sjekke hvilken type vare det er
                return type_vare                                                            # Det brukeren skriver vil bli returnert som type_vare
            else:                                                                           # Hvis brukeren skriver noe som ikke stemmer, printer den ut en feilmelding og lar brukeren skrive igjen
                print("Skriv riktig varetype") 
                continue
        

    print("\nSkriv inn prisen på varene og type vare. Avslutt med negativ pris!\n")
    while True:                                                                             # Lager en while-løkke
        prisen = skriv_inn_pris()                                                           # Henter inn funksjonen for prisen
        if prisen is None:                                                                  # Hvis brukeren skriver feil i prisfeltet, går det ikke videre til hen har skrevet riktig format
            continue
        if prisen < 0.0:                                                                    # Koden avslutter å kjøre når pris < 0
            break
        varevalg = skriv_inn_varetype()                                                     # Henter inn funksjonen for varetype
        if varevalg == "m":                                                                 # Summerer prisen til varene hver for seg etter hva brukeren skriver
            sum_mat += prisen
        elif varevalg == "d":
            sum_drikke += prisen
        else:
            sum_annet += prisen
    print(f"Summen for mat: {sum_mat}kr")                                                   # Printer ut summen for mat
    print(f"Summen for drikke: {sum_drikke}kr")                                             # Printer ut summen for drikke
    print(f"Summen for alt det andre: {sum_annet}kr")                                       # Printer ut summen for annet


# LAG EN FUNKSJON SOM REGNER UT SUMMEN AV E(X) = SUM(N-M), X^N/N!
if __name__ == "__main__":
     
    def fakultet(n):                                      # Lager en funksjon for fakultetet                                                                       # Definerer fakultetet_n som parameteren n
                    fakultet_n = n                        # Definererer fakultet(n) = n
                    resultat = 1                          # Definerer resultat (starter med 1), akkumulator = en variabel som samler opp svaret
                    for tall in range(1, fakultet_n + 1): # Skriver for-løkke, (fra og med, stopper før tallet (til)) 
                            resultat = resultat * tall
                    return resultat                       # Resultatet ganger det tidligere resultatet med det neste tallet
                            

    def rekke(x, M):                                                                                                         # Lager en funksjon med parameter n og M

            while True:                                                                                                      # Lager en while-løkke
                    try:                                                                                                     # Brukeren kan velge x- og M-verdi
                            x = int(input("Skriv inn x: "))
                            if x < 0:                                                                                        # Fakultetet kan ikke være noe av et negativit tall
                                    print("Tallet må være positivt!")
                                    continue
                            M = int(input("Skriv inn M: "))
                            if M < 0:
                                    print("Tallet må være positivt!")
                                    continue
                    except ValueError:                                                                                       # Skriver ut en feilmelding ved bruk av bokstaver
                            print("Du må skrive inn et gyldig tall.")
                            new_round = input("Test koden på nytt, tast 1. Test koden på nytt med default verdi, tast 0: ")

                            if(int(new_round)==1):                                                                           # Brukeren skriver 1 og hele koden vil starte på nytt
                                    continue

                            
                    sum = 0                                                                                                  # Definerer sum = 0
                    for n in range(0, M + 1):                                                                                # Lager en for-løkke
                            f = fakultet(n)                                                                                  # Henter inn funksjonen for fakultet n
                            delsum = (x**n)/f                                                                                # Skriver inn formelen for e(x)
                            sum += delsum                                                                                    # Regner ut summen av verdiene som blir brukt på e(x)
                    return sum                                                                                               # Returnerer summen
            
    print(rekke(2,40)) # Printer funksjonen rekke med x=2 og M=40 som default verdier


# SKRIV ET SCRIPT SOM SJEKKER HVOR STOR FORSKJELLEN MELLOM KVADRATROTA AV E(X) MED DEFAULT VERIER OG TALLET E

if __name__ == "__main__":
    import math
     
    def fakultet(n):                                      # Lager en funksjon for fakultetet
                    fakultet_n = n                        # Definererer fakultet(n) = n
                    resultat = 1                          # Definerer resultat (starter med 1), akkumulator = en variabel som samler opp svaret
                    for tall in range(1, fakultet_n + 1): # Skriver for-løkke, (fra og med, stopper før tallet (til)) 
                            resultat = resultat * tall
                    return resultat                       # Resultatet ganger det tidligere resultatet med det neste tallet
                            
    def rekke(x, M):                                                          # Lager en funksjon med parameter n og M
                    sum = 0                                                   # Definerer sum = 0
                    forskjell = 0
                    for n in range(0, M + 1):                                 # Lager en for-løkke
                            f = fakultet(n)                                   # Henter inn funksjonen for fakultet n
                            delsum = (x**n)/f                                 # Skriver inn formelen for e(x)
                            sum += delsum                                     # Regner ut summen av verdiene som blir brukt på e(x)
                            forskjell = abs(math.e - math.sqrt(sum))
                    return f"Forskjellen er {forskjell:.10f} for M = {verdi}" # Returnerer summen

    for verdi in range(1, 101):                                               # Lager en for-løkke for å sjekke verdi av M mellom 1 og 100
        print(rekke(2, verdi))                                                # Printer funksjonen rekke med x=2 og M=40 som default verdier


# SKRIV OM PROGRAMMET SOM REGNER UT BREDDEN OG HØYDEN AV EN SKJERM I CM
if __name__ == "__main__":
    def tommer(lengde, bredde = 16, hoyde = 9):
        diagonal_tommer_tall = float(lengde)                                   # Tallet skal ha desimaler
        diagonal = bredde**2+hoyde**2                                          # Regner ut tallet for 16:9 format
        x = (diagonal_tommer_tall**2 / diagonal)**0.5                          # Finner lengden på én kloss
        b = bredde*x*2.54                                                      # Regner ut bredden i cm
        h = hoyde*x*2.54                                                       # Regner ut høyden i cm
        return b, h                                                            # Returnerer bredden og høyden i cm

    b, h = tommer(lengde = input("Skriv inn antall tommer på skjermen: "))     # Henter ut bredden og høyden fra funksjonen, og lar brukeren skrive antall tommer
    print (f"Bredden til skjermen er {b}cm og høyden til skjermen er {h}cm." ) # Printer ut bredden og høyden i cm


# SKRIV EN FUNKSJON "STJERNE" SOM TEGNER EI STJERNE MED TURTLE GRAPHICS
if __name__ == "__main__":

    import turtle
    star = turtle.Turtle()
    star.speed(0)

    def stjerne():
        for linjer in range(12):
            star.forward(10)
            star.back(10)
            star.left(30)
        
    def galakse():
        for rotasjon in range(5):
            star.penup()
            star.goto(0, 0)
            star.setheading(72 * rotasjon)
            star.pendown()
            for galaxy in range(9):
                    star.penup()
                    star.forward(40)
                    star.right(15)
                    star.pendown()
                    stjerne()
        turtle.done()


    galakse()