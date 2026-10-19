# LAG ET PROGRAM SOM KONVERTERER MELLOM ULIKE MÅLEENHETER FOR AVSTAND

måleenhet = {                                         # Lager en dictionary med ulike måleenheter målt i meter
    "km": 1000,
    "m": 1,
    "dm": 0.1,
    "cm": 0.01,
    "mm": 0.001
}
        
navn = {
    "km": "kilometer",
    "m": "meter",
    "dm": "desimeter",
    "cm": "centimeter",
    "mm": "millimeter"
    }

overskrift = "Konverter tallet mellom måleenhetene!"
print(overskrift)

tall = float(input("Skriv inn tallet: "))            # Brukeren skriver inn tall og måleenhet
enhet = input("Skriv inn måleenhet: ")
konverter = input("Konverter til: ")                 # Brukeren velger hva den skal konverteres til

start = måleenhet[enhet]                             # Sjekker om brukerens måleenhet finnes i dictionary
slutt = måleenhet[konverter]                         # Sjekker om ny måleenhet finnes i dictionary

start_navn = navn[enhet]
slutt_navn = navn[konverter]

ny_tall = tall * start / slutt                       # Konverterer verdien til ny måleenhet
print(f"{tall:.1f} {start_navn} er det samme som {ny_tall:.4f} {slutt_navn}.")


# LAG ET PROGRAM SOM BRUKER SAMME SCRIPT FOR ENHETENE FOR ULIKE TING

import json

måleenhet = {}                                       # Lager en tom dictionary
konvertering = input("Hva vil du konvertere (vekt, tid, avstand)? ") # Brukeren skriv inn det som skal konverteres
filnavn = "Python-øvinger/Dictionaries,_klasser_og_objekter/Dictionaries/" + konvertering.capitalize() + ".json"

with open(filnavn, mode = "r", encoding = "utf-8") as fil: # Åpner filen for hva brukeren vil konvertere
    måleenhet = json.load(fil)                             # Henter utmåleenhetene fra json-filen og setter inn i dictionary
    print("Laster inn måleenheter: ", måleenhet)

tall = float(input("Skriv inn tallet: "))            # Brukeren skriver inn tall og måleenhet
enhet = input("Skriv inn måleenhet: ")
konverter = input("Konverter til: ")                 # Brukeren velger hva den skal konverteres til

start = måleenhet[enhet]                             # Sjekker om brukerens måleenhet finnes i dictionary
slutt = måleenhet[konverter]                         # Sjekker om ny måleenhet finnes i dictionary

ny_tall = tall * start / slutt                       # Konverterer verdien til ny måleenhet
print(f"{tall:.1f}{enhet} er det samme som {ny_tall:.4f}{konverter}.")