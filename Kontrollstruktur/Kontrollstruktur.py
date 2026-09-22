# SKRIV ET PYTHON-SCRIPT SOM REGNER UT DRIVSTOFFSPRISEN FOR EN KJØRETUR

pris = float(input("Hvor mye koster drivstoffen pr. liter? "))                   # Definerer drivstoffprisen pr. liter
forbruk = float(input("Hvor langt kan bilen kjøre på én liter? "))               # Definerer hvor mye km/liter
avstand = float(input("Hvor langt ønsker du å kjøre? "))                         # Definerer avstanden for kjøreturen

antall_liter = avstand/forbruk                                                   # Regner ut hvor mye liter bilen trenger for kjøreturen
pris_for_avstand = round(antall_liter*pris , 2)                                  # Regner ut drivstoffprisen for hele turen

print(f"Drivstoffprisen for kjøreturen på {avstand}km er {pris_for_avstand}kr.") # Printer ut drivstoffsprisen, bruker formatert streng


# MODIFISER EN KODE SLIK AT DEN SKRIVER UT AT DEN IKKE TRENGER LADING HVIS DISTANSE < 80% AV MAKS DISTANSEN

rekkevidde_km_str = int(input("Rekkevidden til din el-bil i km: "))     # Brukeren skriver inn rekkevidden 
tur_lengde_km_str = int(input("Lengden til kjøreturen din i km: "))     # Brukeren skriver inn lengden på kjøreturen
rekkevidde_lading = rekkevidde_km_str-int(rekkevidde_km_str*0.2)        # Regner ut 20% av den totale rekkevidden
antall_ladninger = tur_lengde_km_str // rekkevidde_lading               # Regner ut hvor mange ladninger bilen trenger for hele kjøreturen
distanse = int(rekkevidde_km_str*0.8)                                   # Definerer 80% av den totale rekkevidden som distanse

if distanse > tur_lengde_km_str:                                        # Hvis kjøreturen er mindre enn distanse, null lading
    antall_ladninger = 0
    print(f"Need {antall_ladninger} charging. You are good to go!!!")   # Printer ut ved bruk av formatert-streng
if distanse < tur_lengde_km_str:                                        # Hvis kjøreturen er større enn distanse
    if antall_ladninger == 1:                                           # Hvis bilen må lade én gang
        print(f"You need to charge your car once!")                     # Printer ut ved bruk av formatert-streng
    else:                                                               # Bilen må lade flere ganger
        print(f"You need to charge your car {antall_ladninger} times!") # Printer ut ved bruk av formatert-streng


# MODIFISER KODEN SLIK AT DU LADER FRA 20% TIL 80%

rekkevidde_km_str = int(input("Rekkevidden til din el-bil i km: "))      # Brukeren skriver inn rekkevidden 
tur_lengde_km_str = int(input("Lengden til kjøreturen din i km: "))      # Brukeren skriver inn lengden på kjøreturen
rekkevidde_lading = rekkevidde_km_str-int(rekkevidde_km_str*0.6)         # Regner ut 60% av den totale rekkevidden
antall_ladninger = tur_lengde_km_str // rekkevidde_lading                # Regner ut hvor mange ladninger bilen trenger for hele kjøreturen
distanse = int(rekkevidde_km_str*0.8)                                    # Definerer 80% av den totale rekkevidden som distanse

if distanse > tur_lengde_km_str:                                         # Hvis kjøreturen er mindre enn distanse, null lading
    antall_ladninger = 0
    print(f"Need {antall_ladninger} charging. You are good to go!!!")    # Printer ut ved bruk av formatert-streng
if distanse < tur_lengde_km_str:                                         # Hvis kjøreturen er større enn distanse
    if antall_ladninger <= 1:                                            # Hvis bilen må lade mindre eller lik en gang
        print(f"You need to charge your car once!")                      # Printer ut ved bruk av formatert-streng
    else:                                                                # Bilen må lade flere ganger
        print(f"You need to charge your car {antall_ladninger} times!")  # Printer ut ved bruk av formatert-streng


# MODIFISER KODEN TIL Å TELLE RIKTIG

import random                                                                                # Importerer funksjonen random

mitt_tall = random.randint(1, 1000)                                                          # Definerer et random tall mellom 1 og 999
ditt_tall = 0                                                                                # Definerer ditt_tall
antall_forsok = 0                                                                            # Definerer antall_forsøk
print("Jeg har et tall mellom 1 og 1000. Du skal gjette mitt tall på færrest mulig forsøk.") # Printer ut spillteksten
while True:                                                                                  # Lager en while-løkke som kjører evig
    ditt_tall = int(input("Hva gjetter du? "))                                               # Brukeren kan gjette et tall, koverteres til heltall
    antall_forsok = antall_forsok + 1                                                        # Teller antall forsøk, gjelder for if-, elif- og else-setningene
    if ditt_tall < mitt_tall:                                                                # Hvis brukerens gjett er mindre eller større, gir den beskjed om det
        print("Ditt tall er mindre enn mitt tall.")
    elif ditt_tall > mitt_tall:
        print("Ditt tall er større enn mitt tall.")
    else:                                                                                    # Hvis brukeren gjetter riktig, får de beskjed om det
        print(f"Gratulerer! Du gjettet riktig. Du brukte {antall_forsok} forsøk.")


# MODIFISER KODEN TIL Å AVSLUTTE NÅR TALLET ER GJETTET

import random                                                                                # Importerer funksjonen random

mitt_tall = random.randint(1, 1000)                                                          # Definerer et random tall mellom 1 og 999
ditt_tall = 0                                                                                # Definerer ditt_tall
antall_forsok = 0                                                                            # Definerer antall_forsøk
print("Jeg har et tall mellom 1 og 1000. Du skal gjette mitt tall på færrest mulig forsøk.") # Printer ut spillteksten
                                                    
while True:                                                                                  # Lager en while-løkke som kjører evig
    ditt_tall = int(input("Hva gjetter du? "))                                               # Brukeren kan gjette et tall, koverteres til heltall               
    antall_forsok = antall_forsok + 1                                                        # Teller antall forsøk, gjelder for if-, elif- og else-setningene
    if ditt_tall < mitt_tall:                                                                # Hvis brukerens gjett er mindre eller større, gir den beskjed om det
        print("Ditt tall er mindre enn mitt tall.")
    elif ditt_tall > mitt_tall:
        print("Ditt tall er større enn mitt tall.")
    else:                                                                                    # Hvis brukeren gjetter riktig, får de beskjed om det
        print(f"Gratulerer! Du gjettet riktig. Du brukte {antall_forsok} forsøk.")

    if ditt_tall == mitt_tall:                                                               # Hvis brukeren gjetter riktig så skal koden stoppe å kjøre
        break


# MODIFISER KODEN TIL AT BRUKEREN KAN LEGGE INN ET HØYT TALL

import random                                                                                          # Importerer funksjonen random  

bruker_tall = int(input("Skriv inn et høyt tall: "))                                                   # Brukeren kan velge det høyeste tallet
mitt_tall = random.randint(1, bruker_tall)                                                             # Definerer et random tall mellom 1 og det brukeren har valgt
ditt_tall = 0                                                                                          # Definerer ditt_tall
antall_forsok = 0                                                                                      # Definerer antall_forsøk
print(f"Jeg har et tall mellom 1 og {bruker_tall}. Du skal gjette mitt tall på færrest mulig forsøk.") # Printer ut spillteksten

while True:                                                                                            # Lager en while-løkke som kjører evig
    ditt_tall = int(input("Hva gjetter du? "))                                                         # Brukeren kan gjette et tall, koverteres til heltall
    antall_forsok = antall_forsok + 1                                                                  # Teller antall forsøk, gjelder for if-, elif- og else-setningene
    if ditt_tall < mitt_tall:                                                                          # Hvis brukerens gjett er mindre eller større, gir den beskjed om det
        print("Ditt tall er mindre enn mitt tall.")
    elif ditt_tall > mitt_tall:                                                                        # Hvis brukeren gjetter riktig, får de beskjed om det
        print("Ditt tall er større enn mitt tall.")
    else:
        print(f"Gratulerer! Du gjettet riktig. Du brukte {antall_forsok} forsøk.")
        break                                                                         # Hvis brukeren gjetter riktig så skal koden stoppe å kjøre


# MODIFISER KODEN TIL Å SKRIVE UT OM BRUKERENS GJETT VAR NÆRMERE ELLER LENGER UNNA DET NEST SISTE GJETTET

import random                                                                                          # Importerer funksjonen random

bruker_tall = int(input("Skriv inn et høyt tall: "))                                                   # Brukeren kan velge det høyeste tallet
mitt_tall = random.randint(1, bruker_tall)                                                             # Definerer et random tall mellom 1 og det brukeren har valgt
ditt_tall = 0                                                                                          # Definerer ditt_tall
antall_forsok = 0                                                                                      # Definerer antall_forsøk
nest_siste_gjett = 0                                                                                   # Definerer nest_siste_gjett                                                                                      
print(f"Jeg har et tall mellom 1 og {bruker_tall}. Du skal gjette mitt tall på færrest mulig forsøk.") # Printer ut spillteksten

while True:                                                                                            # Lager en while-løkke som kjører evig
    ditt_tall = int(input("Hva gjetter du? "))                                                         # Brukeren kan gjette et tall, koverteres til heltall
    if ditt_tall == mitt_tall:                                                                         # Hvis brukeren gjetter riktig så printer den ut at det er riktig og stopper koden
        print(f"Gratulerer! Du gjettet riktig. Du brukte {antall_forsok} forsøk.")                     # Hvis brukerens gjett er mindre eller større, gir den beskjed om det
        break                                                                                           
    antall_forsok = antall_forsok + 1                                                                  # Teller antall forsøk, gjelder for if-, elif- og else-setningene
    if ditt_tall < mitt_tall:                                                                          # Hvis brukerens gjett er mindre eller større, gir den beskjed om det
        print("Ditt tall er mindre enn mitt tall.")
    elif ditt_tall > mitt_tall:                                                                        
        print("Ditt tall er større enn mitt tall.")    
    if antall_forsok > 1:                                                                              # Hvis antall_forsøk er mindre eller større enn 1 finner den avstanden mellom gammel og ny gjett
        forrige_avstand = abs(nest_siste_gjett - mitt_tall)
        ny_avstand = abs(ditt_tall - mitt_tall)
        if forrige_avstand < ny_avstand:                                                               # Gjettet ditt viser om du har kommet lengere eller nærmere 
            print("Du gjettet lengere enn sist.")
        elif forrige_avstand > ny_avstand:
            print("Du gjettet nærmere enn sist.")   

    nest_siste_gjett = ditt_tall                                                                       # Definerer at det nest siste gjettet = ny gjett


# SKRIV UT ALLE TALLENE FRA OG MED 1, TIL OG MED 12 PÅ HVER SIN LINJE

for tall in range(1, 13):   # Lager en for-løkke
    print(tall)             # Printer ut tall fra 1-12


# SKRIV ET PROGRAM SOM KONVERTERER EN SERIE MED BELØP FRA EN VALUTA TIL EN ANNEN

valutakalkulator = "Velkommen til valutakalkulator"                          # Viser at de har kommet til valutakalkulator
print(valutakalkulator)
valuta_1 = input("Konverter fra: ")                                          # Brukeren skal skrive inn hvilke valutaer som skal konverteres
valuta_2 = input("Konverter til: ")

while True:                                                                  # Lager en evig while-løkke
    try:                                                                     # Sjekker om kurset er skrevet med tall
        kurs = float(input("Legg inn kurset mellom valgt valuta: "))
        antall = int(input("Hvor mange ganger skal du konvertere? "))
        break                                                                # Hvis brukeren skrev inn tall kjører koden, hvis ikke vil den sende en ValueError
    except ValueError:
        print("Du er nødt til å skrive inn et gyldig tall. Ikke bokstaver.") 

for penger in range(1, antall + 1):                                          # Lager en for-løkke, slik at de kan skrive de ulike beløpene som skal konverteres
    flere_beløp = float(input(f"Skriv inn beløp {penger}: "))

    konvertering = round((flere_beløp*kurs), 2)
    
    print(f"{flere_beløp} {valuta_1} er {konvertering} {valuta_2}.")         # Etter hver beløp skriver den ut konverteringen


# LAG ET SCRIPT SOM BRUKER TURTLE GRAPHICS TIL Å TEGNE UT EN MANGEKANT

import turtle                                                                                            # Importerer turle

kanter = int(input("Skriv inn antall kanter du vil figuren skal tegne: "))                               # Brukeren kan skrive antall kanter

if kanter < 3:                                                                                           # Hvis det er mindre enn 3 kanter, sender den ut en melding og koden stopper
    print(f"Du valgte {kanter} kanter. Det gir ikke en lukket figur og du kan derfor ikke prøve igjen.")
else:                                                                                                    # Mer enn 3 kanter, figuren starter turtle graphics
        figur = turtle.Turtle()
        snu = 360 / kanter                                                                               # Legger inn antall ganger den må snu slik at det blir en mangekant
        for tegn in range(kanter):

            figur.forward(50)
            figur.left(snu)

        turtle.done()

# LAG ER SCRIPT SOM TEGNER ULIKE ANTALL SIRKLER 

import turtle                    # Importerer turle

sirkel = 4                       # Definerer at det skal være 4 sirkler

figur = turtle.Turtle()
figur.speed(0.5)                 # Får figuren til å tegne sjappere
snu = 90
størrelse = 5                    # Radiusen til sirkelen

for tegn in range(20):           # Lager en for-løkke, 20 tilsvarer at den tegner flere ganger
     størrelse = størrelse + 5   # Radiusen skal øke med 5 for hver 4. sirkel
     figur.right(10)
     for draw in range(sirkel):
        figur.circle(størrelse)
        figur.left(snu)

turtle.done()