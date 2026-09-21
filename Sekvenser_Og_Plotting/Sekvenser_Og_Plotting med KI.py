# KI PROGRAMMERINGS KODE

import csv
import matplotlib.pyplot as plt

filnavn = "timestrafikk_sykkelmotorveien_juni_2026.csv"

# Be brukeren om en dato
bruker_dato = input("Skriv inn en dato (f.eks. 2026-06-01): ").strip()

# Lister for å lagre tider og trafikkmengde til plottet
tid_sandnes = []
trafikk_sandnes = []
tid_stavanger = []
trafikk_stavanger = []

# Åpne filen med riktig tegnkoding (utf-8)
with open(filnavn, mode="r", encoding="utf-8") as fil:
    # Fortell Python at kolonner er separert med semikolon (;)
    leser = csv.reader(fil, delimiter=";")
    
    # Hopper over den aller første linjen (overskriftene)
    overskrifter = next(leser)
    
    # Gå gjennom filen linje for linje
    for rad in leser:
        # Sjekk om raden har nok kolonner, og om datoen (kolonne indeks 5) matcher
        if len(rad) > 9 and rad[5] == bruker_dato:
            felt = rad[8]         # Kolonnen "Felt"
            tid = rad[6]          # Kolonnen "Fra tidspunkt"
            trafikkmengde = int(rad[9])  # Gjør om trafikkmengde fra tekst til tall
            
            # Sorter dataene inn i riktig liste basert på retning
            if felt == "Totalt i retning Sandnes":
                tid_sandnes.append(tid)
                trafikk_sandnes.append(trafikkmengde)
            elif felt == "Totalt i retning Stavanger":
                tid_stavanger.append(tid)
                trafikk_stavanger.append(trafikkmengde)

# Plotting (akkurat som før, men med vanlige Python-lister)
if not tid_sandnes and not tid_stavanger:
    print(f"Fant ingen data for {bruker_dato}.")
else:
    plt.figure(figsize=(12, 6))
    plt.plot(tid_sandnes, trafikk_sandnes, marker="o", color="blue", label="Mot Sandnes")
    plt.plot(tid_stavanger, trafikk_stavanger, marker="s", color="orange", label="Mot Stavanger")
    
    plt.title(f"Sykkelpasseringer per time – {bruker_dato}")
    plt.xlabel("Klokkeslett")
    plt.ylabel("Antall passeringer")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# SJEKK OM KI SITT SCRIPT VIRKER OG FIKS EVENTUELLE FEIL

import csv
import matplotlib.pyplot as plt

filnavn = "Python-øvinger/Sekvenser_Og_Plotting/timestrafikk_sykkelmotorveien_juni_2026.csv"

# Be brukeren om en dato
bruker_dato = input("Skriv inn en dato (f.eks. 2026-06-01): ").strip()

# Lister for å lagre tider og trafikkmengde til plottet
tid_sandnes = []
trafikk_sandnes = []
tid_stavanger = []
trafikk_stavanger = []

# Åpne filen med riktig tegnkoding (utf-8)
with open(filnavn, mode="r", encoding="utf-8") as fil:
    # Fortell Python at kolonner er separert med semikolon (;)
    leser = csv.reader(fil, delimiter=";")
    
    # Hopper over den aller første linjen (overskriftene)
    overskrifter = next(leser)
    
    # Gå gjennom filen linje for linje
    for rad in leser:
        # Sjekk om raden har nok kolonner, og om datoen (kolonne indeks 5) matcher
        if len(rad) > 9 and rad[5] == bruker_dato:
            felt = rad[8]         # Kolonnen "Felt"
            tid = rad[6]          # Kolonnen "Fra tidspunkt"
            trafikkmengde = int(rad[9])  # Gjør om trafikkmengde fra tekst til tall
            
            # Sorter dataene inn i riktig liste basert på retning
            if felt == "Totalt i retning Sandnes":
                tid_sandnes.append(tid)
                trafikk_sandnes.append(trafikkmengde)
            elif felt == "Totalt i retning Stavanger":
                tid_stavanger.append(tid)
                trafikk_stavanger.append(trafikkmengde)

# Plotting (akkurat som før, men med vanlige Python-lister)
if not tid_sandnes and not tid_stavanger:
    print(f"Fant ingen data for {bruker_dato}.")
else:
    plt.figure(figsize=(12, 6))
    plt.plot(tid_sandnes, trafikk_sandnes, marker="o", color="blue", label="Mot Sandnes")
    plt.plot(tid_stavanger, trafikk_stavanger, marker="s", color="orange", label="Mot Stavanger")
    
    plt.title(f"Sykkelpasseringer per time – {bruker_dato}")
    plt.xlabel("Klokkeslett")
    plt.ylabel("Antall passeringer")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# ANALYSER HVOR LETT DU SYNES KI-EN SITT SCRIPT ER Å LESE

import csv                                                                                   # Importerer csv-filer
import matplotlib.pyplot as plt                                                              # Importerer matplotlib.pylot for å lage figur/grafer/diagram

filnavn = "Python-øvinger/Sekvenser_Og_Plotting/timestrafikk_sykkelmotorveien_juni_2026.csv" # Definerer filnavnet

# Be brukeren om en dato
bruker_dato = input("Skriv inn en dato (f.eks. 2026-06-01): ").strip()                       # Brukeren skriver inn en dato

# Lister for å lagre tider og trafikkmengde til plottet                                      # Lager ulike lister slik at det er mulige å plotte inn det som tilhører riktig liste
tid_sandnes = []                                                                              
trafikk_sandnes = []
tid_stavanger = []
trafikk_stavanger = []

# Åpne filen med riktig tegnkoding (utf-8)
with open(filnavn, mode="r", encoding="utf-8") as fil:                                       # Åpner filen i lesemodus, bruker with slik at den lukker automatisk selv
    # Fortell Python at kolonner er separert med semikolon (;)
    leser = csv.reader(fil, delimiter=";")                                                   # Definerer leser, forteller at kolonnene er separert med semikolonne ved bruk av delimiter
    
    # Hopper over den aller første linjen (overskriftene)
    overskrifter = next(leser)                                                               # Hopper over overskriften (1. linja) i csv-filen fordi tekst ikke kan gjøre om til tall
    
    # Gå gjennom filen linje for linje
    for rad in leser:                                                                        # Lager en for-løkke, går gjennom filen linje for linje
        # Sjekk om raden har nok kolonner, og om datoen (kolonne indeks 5) matcher
        if len(rad) > 9 and rad[5] == bruker_dato:                                           # Sjekker om det e rminst 10 elementer og kolonne 5
            felt = rad[8]         # Kolonnen "Felt"                                          # Definerer "felt" fra listen
            tid = rad[6]          # Kolonnen "Fra tidspunkt"                                 # Definerer "fra tidspunkt" fra listen
            trafikkmengde = int(rad[9])                                                      # Gjør om trafikkmengde fra tekst til heltall          
            
            # Sorter dataene inn i riktig liste basert på retning
            if felt == "Totalt i retning Sandnes":                                           
                tid_sandnes.append(tid)                                                      # Kolonne 6 blir lagt inn i listen tid_sandnes
                trafikk_sandnes.append(trafikkmengde)                                        # Kolonne 9 blir lagt inn i listen trafikk_sandnes
            elif felt == "Totalt i retning Stavanger":                                       
                tid_stavanger.append(tid)                                                    # Kolonne 6 blir lagt inn i listen tid_stavanger
                trafikk_stavanger.append(trafikkmengde)                                      # Kolonne 9 blir lagt inn i listen trafikk_stavanger

# Plotting (akkurat som før, men med vanlige Python-lister)
if not tid_sandnes and not tid_stavanger:
    print(f"Fant ingen data for {bruker_dato}.")                                             # Hvis ingen data blir flyttet inn i listene
else:
    plt.figure(figsize=(12, 6))
    plt.plot(tid_sandnes, trafikk_sandnes, marker="o", color="blue", label="Mot Sandnes")    # (x-akse, y-akse, markeringstype, farge, navn på markeringstypen)
    plt.plot(tid_stavanger, trafikk_stavanger, marker="s", color="orange", label="Mot Stavanger") # (x-akse, y-akse, markeringstype, farge, navn på markeringstypen)
    
    plt.title(f"Sykkelpasseringer per time - {bruker_dato}")
    plt.xlabel("Klokkeslett")
    plt.ylabel("Antall passeringer")
    plt.xticks(rotation=45)                                                                  # Tidene er rotert 45 grader
    plt.grid(True)                                                                           # Lager rutenett
    plt.legend()                                                                             # Viser til hvilke markeringer som er hva
    plt.tight_layout()
    plt.show()

# Koden i seg selv er grei å forstå, men var usikker på hva delimiter gjorde.
# Brukte litt tid på å forstå for-rad-løkken


# ANALYSER HVOR ROBUST SCRIPTET ER

import csv
import matplotlib.pyplot as plt

filnavn = "Python-øvinger/Sekvenser_Og_Plotting/timestrafikk_sykkelmotorveien_juni_2026.csv"

# Be brukeren om en dato
bruker_dato = input("Skriv inn en dato (f.eks. 2026-06-01): ").strip()

# Lister for å lagre tider og trafikkmengde til plottet
tid_sandnes = []
trafikk_sandnes = []
tid_stavanger = []
trafikk_stavanger = []

# Åpne filen med riktig tegnkoding (utf-8)
with open(filnavn, mode="r", encoding="utf-8") as fil:
    # Fortell Python at kolonner er separert med semikolon (;)
    leser = csv.reader(fil, delimiter=";")
    
    # Hopper over den aller første linjen (overskriftene)
    overskrifter = next(leser)
    
    # Gå gjennom filen linje for linje
    for rad in leser:
        # Sjekk om raden har nok kolonner, og om datoen (kolonne indeks 5) matcher
        if len(rad) > 9 and rad[5] == bruker_dato:
            felt = rad[8]         # Kolonnen "Felt"
            tid = rad[6]          # Kolonnen "Fra tidspunkt"
            trafikkmengde = int(rad[9])  # Gjør om trafikkmengde fra tekst til tall
            
            # Sorter dataene inn i riktig liste basert på retning
            if felt == "Totalt i retning Sandnes":
                tid_sandnes.append(tid)
                trafikk_sandnes.append(trafikkmengde)
            elif felt == "Totalt i retning Stavanger":
                tid_stavanger.append(tid)
                trafikk_stavanger.append(trafikkmengde)

# Plotting (akkurat som før, men med vanlige Python-lister)
if not tid_sandnes and not tid_stavanger:
    print(f"Fant ingen data for {bruker_dato}.")
else:
    plt.figure(figsize=(12, 6))
    plt.plot(tid_sandnes, trafikk_sandnes, marker="o", color="blue", label="Mot Sandnes")
    plt.plot(tid_stavanger, trafikk_stavanger, marker="s", color="orange", label="Mot Stavanger")
    
    plt.title(f"Sykkelpasseringer per time – {bruker_dato}")
    plt.xlabel("Klokkeslett")
    plt.ylabel("Antall passeringer")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Scriptet er robust nok til å skrive feilelding dersom det er feilformatert, eller skrevet inn noe annet enn en dato
# Men den gir bare en felles feilmelding for alt sammen som ikke er i riktig format
# Mangler også en try-, except- med tanke på åpning av fil og ved int()


# TESTER PROGRAMET MED EN ANNEN CSV-FIL OG GJØR DEN MER ROBUST

import csv                                                                                                                            # Importerer csv
import matplotlib.pyplot as plt                                                                                                       # Importerer matplotlib.pylot for å lage figur, grafer, diagrammer

try:                                                                                                                                  # Skriver alt i en try- except-
    filnavn = "Python-øvinger/Sekvenser_Og_Plotting/timestrafikk_sykkelmotorveien_juni_2026_innlagte_feil.csv"                        # Definerer filen som filnavn

    gyldige_datoer = ["2026-06-01", "2026-06-02", "2026-06-03", "2026-06-04", "2026-06-05", "2026-06-06", "2026-06-07", "2026-06-08"] # Definerer de gyldige datoene
    while True:                                                                                                                       # Lager en while-løkke for brukerens input
        bruker_dato = input("Skriv inn en dato mellom 2026-06-01/08 (format: YYYY-MM-DD): ").strip()
        if len(bruker_dato) < 10:                                                                                                     # Sjekker om brukerens input er mindre enn 10 elementer
            print("Du må skrive inn riktig format innen de gyldige datoene.")
        elif bruker_dato not in gyldige_datoer:                                                                                       # Sjekker om brukerens dato = en av de gyldige datoene
            print("Skriv inn en dato mellom 06-01 og 06-08.")
        else:                                                                                                                         # Hvis riktig hopper den ut av while-løkken
            break
            
    
    alle_timer = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]
    # Definerer alle timer, grunnet filen mangler noen timer
    timer_sandnes = {}                                                                                                                # Definerer timer_sandnes som dictionary
    timer_stavanger = {}                                                                                                              # Definerer timer_stavanger som dictionary
    x_tid_sandnes = []
    y_trafikk_sandnes = []
    x_tid_stavanger = []
    y_trafikk_stavanger = []
    fant_data = False                                                                                                                 # Definerer fant_data

    with open(filnavn, mode="r", encoding="utf-8") as fil:                                                                            # Åpner filen med riktig tegnkoding
        leser = csv.reader(fil, delimiter=";")                                                                                        # Leser filen og viser til delimiter (at semikolonn deler de ulike elementene)
  
        overskrifter = next(leser)                                                                                                    # Hopper over den første linjen, altså overskriften

        for klokkeslett in alle_timer:                                                                                                # Lager en for-løkke for alle timer
            timer_sandnes[klokkeslett] = 0                                                                                            # Setter alle timer = 0
            timer_stavanger[klokkeslett] = 0                                                                                          # Setter alle_timer = 0

        for rad in leser:                                                                                                             # Lager en for-løkke som leser filen linje for linje
            if len(rad) > 9 and rad[5] == bruker_dato:                                                                                # Sikrer at raden har nok kolonner til å hente ut trafikkmengde og om brukerens dator = rad[5
                fant_data = True                                                                                                      # Hvis brukerensdato er lik, fant_data = True
                felt = rad[8]                                                                                                         # Hvis like, definerer element 8 som felt
                tid = rad[6]                                                                                                          # Hvis like, definerer element 6 som tid
                try:                                                                                                                  # Tester om trafikkmengden kan gjøre om til heltall
                    trafikkmengde = int(rad[9])  
                except ValueError:                                                                                                    # Hvis ikke, trafikkmengen = 0
                    trafikkmengde = 0
                
                if felt == "Totalt i retning Sandnes".strip():                                                                        # Sjekker felt, bruker strip() for å fjerne tomrom
                    timer_sandnes[tid] = trafikkmengde                                                                                # Trafikkmengden lagres i dictionary for gitt time
                elif felt == "Totalt i retning Stavanger".strip():                                                                    
                    timer_stavanger[tid] = trafikkmengde

        for klokkeslett in alle_timer:                                                                                                # Lager en for-løkke for alle timer
            x_tid_sandnes.append(klokkeslett)                                                                                         # Setter inn alle klokkeslettene inn i listen x_tid_sandnes
            y_trafikk_sandnes.append(timer_sandnes[klokkeslett])                                                                      # Henter inn de lagrede trafikkmengdene fra dictionary og sjekker opp med riktig klokkeslett
            x_tid_stavanger.append(klokkeslett)
            y_trafikk_stavanger.append(timer_stavanger[klokkeslett])

    if not fant_data:                                                                                                                 # Sjekker om verdiene blir funnet og er True
        print(f"Fant ingen data for {bruker_dato}.")
    else:                                                                                                                             # Hvis verdiene funker, tegn ved bruk av matplotlib.pyplot
        plt.figure(figsize=(12, 6))
        plt.plot(x_tid_sandnes, y_trafikk_sandnes, marker="o", color="blue", label="Mot Sandnes")
        plt.plot(x_tid_stavanger, y_trafikk_stavanger, marker="s", color="orange", label="Mot Stavanger")
        
        plt.title(f"Sykkelpasseringer per time – {bruker_dato}")
        plt.xlabel("Klokkeslett")
        plt.ylabel("Antall passeringer")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
    
except FileNotFoundError:                                                                                                             # Sjekker om filen blir funnet
    print("Filen er ikke eksisterende.")


# PLOTT TO SEPERATE DATOER FOR Å SAMMENLIKNE DEM

import csv                                                                                                                            # Importerer csv
import matplotlib.pyplot as plt                                                                                                       # Importerer matplotlib.pylot for å lage figur, grafer, diagrammer

try:                                                                                                                                  # Skriver alt i en try- except-
    filnavn = "Python-øvinger/Sekvenser_Og_Plotting/timestrafikk_sykkelmotorveien_juni_2026_innlagte_feil.csv"                        # Definerer filen som filnavn

    gyldige_datoer = ["2026-06-01", "2026-06-02", "2026-06-03", "2026-06-04", "2026-06-05", "2026-06-06", "2026-06-07", "2026-06-08"] # Definerer de gyldige datoene
    while True:                                                                                                                       # Lager en while-løkke for brukerens input
        bruker_dato_1 = input("Skriv inn en dato mellom 2026-06-01/08 (format: YYYY-MM-DD): ").strip()
        if len(bruker_dato_1) < 10:                                                                                                     # Sjekker om brukerens input er mindre enn 10 elementer
            print("Du må skrive inn riktig format innen de gyldige datoene.")
        elif bruker_dato_1 not in gyldige_datoer:                                                                                       # Sjekker om brukerens dato = en av de gyldige datoene
            print("Skriv inn en dato mellom 06-01 og 06-08.")
        else:
            break
    while True:
        bruker_dato_2 = input("Skriv inn en annen dato mellom 2026-06-01/08 (format: YYYY-MM-DD): ").strip()    
        if len(bruker_dato_2) < 10:                                                                                                     # Sjekker om brukerens input er mindre enn 10 elementer
            print("Du må skrive inn riktig format innen de gyldige datoene.")
        elif bruker_dato_2 not in gyldige_datoer:                                                                                       # Sjekker om brukerens dato = en av de gyldige datoene
            print("Skriv inn en dato mellom 06-01 og 06-08.")
        else:                                                                                                                         # Hvis riktig hopper den ut av while-løkken
            break
            
    
    alle_timer = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]
    # Definerer alle timer, grunnet filen mangler noen timer
    timer_sandnes_1 = {}                                                                                                                # Definerer timer_sandnes som dictionary
    timer_sandnes_2 = {}
    timer_stavanger_1 = {}                                                                                                              # Definerer timer_stavanger som dictionary
    timer_stavanger_2 = {}
    x_tid_sandnes_1 = []
    x_tid_sandnes_2 = []
    y_trafikk_sandnes_1 = []
    y_trafikk_sandnes_2 = []
    x_tid_stavanger_1 = []
    x_tid_stavanger_2 = []
    y_trafikk_stavanger_1 = []
    y_trafikk_stavanger_2 = []
    fant_data = False                                                                                                                 # Definerer fant_data

    with open(filnavn, mode="r", encoding="utf-8") as fil:                                                                            # Åpner filen med riktig tegnkoding
        leser = csv.reader(fil, delimiter=";")                                                                                        # Leser filen og viser til delimiter (at semikolonn deler de ulike elementene)
  
        overskrifter = next(leser)                                                                                                    # Hopper over den første linjen, altså overskriften

        for klokkeslett in alle_timer:                                                                                                # Lager en for-løkke for alle timer
            timer_sandnes_1[klokkeslett] = 0                                                                                          # Setter alle timer = 0
            timer_stavanger_1[klokkeslett] = 0                                                                                        # Setter alle_timer = 0
            timer_sandnes_2[klokkeslett] = 0
            timer_stavanger_2[klokkeslett] = 0

        for rad in leser:                                                                                                             # Lager en for-løkke som leser filen linje for linje
            if len(rad) > 9:
                if rad[5] == bruker_dato_1:
                    fant_data = True                                                                                                      # Hvis brukerensdato er lik, fant_data = True
                    felt = rad[8]                                                                                                         # Hvis like, definerer element 8 som felt
                    tid = rad[6]                                                                                                          # Hvis like, definerer element 6 som tid
                    try:                                                                                                                  # Tester om trafikkmengden kan gjøre om til heltall
                        trafikkmengde = int(rad[9])  
                    except ValueError:                                                                                                    # Hvis ikke, trafikkmengen = 0
                        trafikkmengde = 0
                    
                    if felt == "Totalt i retning Sandnes".strip():                                                                        # Sjekker felt, bruker strip() for å fjerne tomrom
                        timer_sandnes_1[tid] = trafikkmengde                                                                              # Trafikkmengden lagres i dictionary for gitt time
                    elif felt == "Totalt i retning Stavanger".strip():                                                                    
                        timer_stavanger_1[tid] = trafikkmengde
                    
                if rad[5] == bruker_dato_2:                                                                              # Sikrer at raden har nok kolonner til å hente ut trafikkmengde og om brukerens dator = rad[5
                    fant_data = True                                                                                                      # Hvis brukerensdato er lik, fant_data = True
                    felt = rad[8]                                                                                                         # Hvis like, definerer element 8 som felt
                    tid = rad[6]                                                                                                          # Hvis like, definerer element 6 som tid
                    try:                                                                                                                  # Tester om trafikkmengden kan gjøre om til heltall
                        trafikkmengde = int(rad[9])  
                    except ValueError:                                                                                                    # Hvis ikke, trafikkmengen = 0
                        trafikkmengde = 0
                    
                    if felt == "Totalt i retning Sandnes".strip():                                                                        # Sjekker felt, bruker strip() for å fjerne tomrom                                                                            
                        timer_sandnes_2[tid] = trafikkmengde                                                                              # Trafikkmengden lagres i dictionary for gitt time
                    elif felt == "Totalt i retning Stavanger".strip():                                                                    
                        timer_stavanger_2[tid] = trafikkmengde

        for klokkeslett in alle_timer:                                                                                                # Lager en for-løkke for alle timer
            x_tid_sandnes_1.append(klokkeslett)                                                                                         # Setter inn alle klokkeslettene inn i listen x_tid_sandnes
            y_trafikk_sandnes_1.append(timer_sandnes_1[klokkeslett])                                                                      # Henter inn de lagrede trafikkmengdene fra dictionary og sjekker opp med riktig klokkeslett
            x_tid_stavanger_1.append(klokkeslett)
            y_trafikk_stavanger_1.append(timer_stavanger_1[klokkeslett])
            x_tid_sandnes_2.append(klokkeslett)                                                                                         # Setter inn alle klokkeslettene inn i listen x_tid_sandnes
            y_trafikk_sandnes_2.append(timer_sandnes_2[klokkeslett])                                                                      # Henter inn de lagrede trafikkmengdene fra dictionary og sjekker opp med riktig klokkeslett
            x_tid_stavanger_2.append(klokkeslett)
            y_trafikk_stavanger_2.append(timer_stavanger_2[klokkeslett])

    if not fant_data:                                                                                                                 # Sjekker om verdiene blir funnet og er True
        print(f"Fant ingen data for {bruker_dato_1}.")
        print(f"Fant ingen data for {bruker_dato_2}.")
    else:                                                                                                                             # Hvis verdiene funker, tegner ved bruk av matplotlib.pyplot
        plt.figure(figsize=(12, 6))
        plt.plot(x_tid_sandnes_1, y_trafikk_sandnes_1, marker="o", color="blue", label="Mot Sandnes")
        plt.plot(x_tid_stavanger_1, y_trafikk_stavanger_1, marker="s", color="orange", label="Mot Stavanger")
        plt.title(f"Sykkelpasseringer per time – {bruker_dato_1}")
        plt.xlabel("Klokkeslett")
        plt.ylabel("Antall passeringer")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        plt.figure(figsize=(12, 6))  
        plt.plot(x_tid_sandnes_2, y_trafikk_sandnes_2, marker="o", color="blue", label="Mot Sandnes")
        plt.plot(x_tid_stavanger_2, y_trafikk_stavanger_2, marker="s", color="orange", label="Mot Stavanger")
        plt.title(f"Sykkelpasseringer per time – {bruker_dato_2}")
        plt.xlabel("Klokkeslett")
        plt.ylabel("Antall passeringer")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        plt.show()
    
except FileNotFoundError:                                                                                                             # Sjekker om filen blir funnet
    print("Filen er ikke eksisterende.")


# SAMMENLIKN DATAENE FRA AUGUST 2025 OG AUGUST 2026

import csv                                                                                                                            # Importerer csv
import matplotlib.pyplot as plt                                                                                                       # Importerer matplotlib.pylot for å lage figur, grafer, diagrammer

try:                                                                                                                                  # Skriver alt i en try- except-
    filnavn_1 = "Python-øvinger/Sekvenser_Og_Plotting/timestrafikk_sykkelmotorveien_juni_2026_innlagte_feil.csv"                        # Definerer filen som filnavn

    gyldige_datoer_1 = ["2026-06-01", "2026-06-02", "2026-06-03", "2026-06-04", "2026-06-05", "2026-06-06", "2026-06-07", "2026-06-08"] # Definerer de gyldige datoene
    while True:                                                                                                                       # Lager en while-løkke for brukerens input
        bruker_dato_1 = input("Skriv inn en dato mellom 2026-06-01/08 (format: YYYY-MM-DD): ").strip()
        if len(bruker_dato_1) < 10:                                                                                                     # Sjekker om brukerens input er mindre enn 10 elementer
            print("Du må skrive inn riktig format innen de gyldige datoene.")
        elif bruker_dato_1 not in gyldige_datoer_1:                                                                                       # Sjekker om brukerens dato = en av de gyldige datoene
            print("Skriv inn en dato mellom 06-01 og 06-08 og husk riktig årstall.")
        else:
            break

    filnavn_2 = "Python-øvinger/Sekvenser_Og_Plotting/timetrafikk_sykkelmotorveien_juni_2025.csv"

    gyldige_datoer_2 = ["2025-06-01", "2025-06-02", "2025-06-03", "2025-06-04", "2025-06-05", "2025-06-06", "2025-06-07", "2025-06-08"]   
    while True:
        bruker_dato_2 = input("Skriv inn en annen dato mellom 2025-06-01/08 (format: YYYY-MM-DD): ").strip()    
        if len(bruker_dato_2) < 10:                                                                                                     # Sjekker om brukerens input er mindre enn 10 elementer
            print("Du må skrive inn riktig format innen de gyldige datoene.")
        elif bruker_dato_2 not in gyldige_datoer_2:                                                                                       # Sjekker om brukerens dato = en av de gyldige datoene
            print("Skriv inn en dato mellom 06-01 og 06-08 og husk riktig årstall.")
        else:                                                                                                                         # Hvis riktig hopper den ut av while-løkken
            break
            
    
    alle_timer = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]
    # Definerer alle timer, grunnet filen mangler noen timer
    timer_sandnes_1 = {}                                                                                                                # Definerer timer_sandnes som dictionary
    timer_sandnes_2 = {}
    timer_stavanger_1 = {}                                                                                                              # Definerer timer_stavanger som dictionary
    timer_stavanger_2 = {}
    x_tid_sandnes_1 = []
    x_tid_sandnes_2 = []
    y_trafikk_sandnes_1 = []
    y_trafikk_sandnes_2 = []
    x_tid_stavanger_1 = []
    x_tid_stavanger_2 = []
    y_trafikk_stavanger_1 = []
    y_trafikk_stavanger_2 = []
    fant_data = False                                                                                                                 # Definerer fant_data

    with open(filnavn_1, mode="r", encoding="utf-8") as fil_1, open(filnavn_2, mode="r", encoding="utf-8") as fil_2:                                                                            # Åpner filen med riktig tegnkoding
        leser_1 = csv.reader(fil_1, delimiter=";")                                                                                        # Leser filen og viser til delimiter (at semikolonn deler de ulike elementene)
        overskrifter = next(leser_1)                                                                                                    # Hopper over den første linjen, altså overskriften

        leser_2 = csv.reader(fil_2, delimiter=";")
        overskrifter = next(leser_2)

        for klokkeslett in alle_timer:                                                                                                # Lager en for-løkke for alle timer
            timer_sandnes_1[klokkeslett] = 0                                                                                          # Setter alle timer = 0
            timer_stavanger_1[klokkeslett] = 0                                                                                        # Setter alle_timer = 0
            timer_sandnes_2[klokkeslett] = 0
            timer_stavanger_2[klokkeslett] = 0

        for rad in leser_1:                                                                                                             # Lager en for-løkke som leser filen linje for linje
            if len(rad) > 9:
                if rad[5] == bruker_dato_1:
                    fant_data = True                                                                                                      # Hvis brukerensdato er lik, fant_data = True
                    felt = rad[8]                                                                                                         # Hvis like, definerer element 8 som felt
                    tid = rad[6]                                                                                                          # Hvis like, definerer element 6 som tid
                    try:                                                                                                                  # Tester om trafikkmengden kan gjøre om til heltall
                        trafikkmengde = int(rad[9])  
                    except ValueError:                                                                                                    # Hvis ikke, trafikkmengen = 0
                        trafikkmengde = 0
                    
                    if felt == "Totalt i retning Sandnes".strip():                                                                        # Sjekker felt, bruker strip() for å fjerne tomrom
                        timer_sandnes_1[tid] = trafikkmengde                                                                              # Trafikkmengden lagres i dictionary for gitt time
                    elif felt == "Totalt i retning Stavanger".strip():                                                                    
                        timer_stavanger_1[tid] = trafikkmengde

        for rad in leser_2:    
            if len(rad) > 9 and rad[5] == bruker_dato_2:                                                                              # Sikrer at raden har nok kolonner til å hente ut trafikkmengde og om brukerens dator = rad[5
                fant_data = True                                                                                                      # Hvis brukerensdato er lik, fant_data = True
                felt = rad[8]                                                                                                         # Hvis like, definerer element 8 som felt
                tid = rad[6]                                                                                                          # Hvis like, definerer element 6 som tid
                try:                                                                                                                  # Tester om trafikkmengden kan gjøre om til heltall
                    trafikkmengde = int(rad[9])  
                except ValueError:                                                                                                    # Hvis ikke, trafikkmengen = 0
                    trafikkmengde = 0
                
                if felt == "Totalt i retning Sandnes".strip():                                                                        # Sjekker felt, bruker strip() for å fjerne tomrom                                                                            
                    timer_sandnes_2[tid] = trafikkmengde                                                                              # Trafikkmengden lagres i dictionary for gitt time
                elif felt == "Totalt i retning Stavanger".strip():                                                                    
                    timer_stavanger_2[tid] = trafikkmengde

        for klokkeslett in alle_timer:                                                                                                # Lager en for-løkke for alle timer
            x_tid_sandnes_1.append(klokkeslett)                                                                                         # Setter inn alle klokkeslettene inn i listen x_tid_sandnes
            y_trafikk_sandnes_1.append(timer_sandnes_1[klokkeslett])                                                                      # Henter inn de lagrede trafikkmengdene fra dictionary og sjekker opp med riktig klokkeslett
            x_tid_stavanger_1.append(klokkeslett)
            y_trafikk_stavanger_1.append(timer_stavanger_1[klokkeslett])
            x_tid_sandnes_2.append(klokkeslett)                                                                                         # Setter inn alle klokkeslettene inn i listen x_tid_sandnes
            y_trafikk_sandnes_2.append(timer_sandnes_2[klokkeslett])                                                                      # Henter inn de lagrede trafikkmengdene fra dictionary og sjekker opp med riktig klokkeslett
            x_tid_stavanger_2.append(klokkeslett)
            y_trafikk_stavanger_2.append(timer_stavanger_2[klokkeslett])

    if not fant_data:                                                                                                                 # Sjekker om verdiene blir funnet og er True
        print(f"Fant ingen data for {bruker_dato_1}.")
        print(f"Fant ingen data for {bruker_dato_2}.")
    else:                                                                                                                             # Hvis verdiene funker, tegner ved bruk av matplotlib.pyplot
        plt.figure(figsize=(12, 6))
        plt.plot(x_tid_sandnes_1, y_trafikk_sandnes_1, marker="o", color="blue", label="Mot Sandnes 2026")
        plt.plot(x_tid_stavanger_1, y_trafikk_stavanger_1, marker="s", color="orange", label="Mot Stavanger 2026")
        plt.plot(x_tid_sandnes_2, y_trafikk_sandnes_2, marker="o", color="red", label="Mot Sandnes 2025")
        plt.plot(x_tid_stavanger_2, y_trafikk_stavanger_2, marker="s", color="green", label="Mot Stavanger 2025")
        plt.title(f"Sykkelpasseringer per time den {bruker_dato_1} og den {bruker_dato_2}")
        plt.xlabel("Klokkeslett")
        plt.ylabel("Antall passeringer 2025 og 2026")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
    
except FileNotFoundError:                                                                                                             # Sjekker om filen blir funnet
    print("Filen er ikke eksisterende.")