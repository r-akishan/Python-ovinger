#LES PROGRAMKODEN OG FORSTA UTEN A KJORE

masse = input("Skriv inn massen til objektet: ") # Definerer masse
masse_tall = float(masse)                        # Tallet skal ha desimaler
fart = input("Skriv inn farten til objektet: ")  # Definerer fart
fart_tall = float(fart)                          # Tallet skal ha desimaler
resultat = 0.5 * masse_tall * fart_tall**2       # Regner ut energien ved bruk E = 1/2*m*v**2
print(resultat)                                  # Printer ut energien til legemet


#SKRIV ET PROGRAM SOM KONVERTERER AVSTANDER FRA KILOMETER TIL NAUTISKE MIL

kilometer = input("Skriv inn avstanden i km: ")                          # Definerer kilometer
kilometer_tall = float(kilometer)                                        # Tallet skal ha desimaler
nautiske_mil = 1.852                                                     # Definerer nautiske mil
konvertering = kilometer_tall/nautiske_mil                               # Regner ut konverteringen fra km til nautiske mil
print(kilometer + "km er lik " + str(konvertering) + " i nautiske mil.") # Printer ut nautiske mil


#SKRIV ET PROGRAM SOM REGNER UT BREDDEN OG LENGDEN AV EN SKJERM I TOMMER
# import math
diagonal_tommer = input("Skriv inn antall tommer på skjermen: ")                                                  # Definerer antall tommer
diagonal_tommer_tall = float(diagonal_tommer)                                                                     # Tallet skal ha desimaler
diagonal = 16**2+9**2                                                                                             # Regner ut tallet for 16:9 format
x = (diagonal_tommer_tall**2 / diagonal)**0.5                                                                     # Finner lengden på én kloss
bredde = 16*x                                                                                                     # Regner ut bredden
høyde = 9*x                                                                                                       # Regner ut høyden
print("Bredden til skjermen er " + str(bredde) + " tommer, og høyden til skjermen er " + str(høyde) + " tommer.") # Printer ut bredden og høyden i antall tommer


#SKRIV ET PROGRAM SOM BRUKER TURTLE GRAPHICS TIL Å TEGNE EN FIGUR

import turtle
figur = turtle.Turtle() # Starter turtle graphics 

figur.left(90)          # Får figuren til å snu mot venstre
figur.forward(50)       # 50 piksler fremover
figur.left(45)          # Snur 45 grader til venstre
figur.forward(40)       # 50 piksler fremover
figur.right(90)         # Snur 90 grader til høyre
figur.forward(50)       # 50 piksler fremover
figur.right(90)         # Snur 90 grader til høyre
figur.forward(50)       # 50 piksler fremover
figur.right(90)         # Snur 90 grader til høyre
figur.forward(40)       # 50 piksler fremover
figur.left(45)          # Snur 45 grader til venstre
figur.forward(50)       # 50 piksler fremover

figur.done()            # Figuren er ferdig


#SKRIV ET PROGRAM SOM KONVERTERER AVSTANDER FRA NAUTISKE MIL TIL KILOMETER

nautiske_mil = input("Skriv inn avstanden i nautiske mil: ")              # Definerer nautiske mil
nautiske_mil_tall = float(nautiske_mil)                                   # Tallet skal ha desimaler
kilometer = 1.852                                                         # Definerer kilometer
konvertering = nautiske_mil_tall*kilometer                                # Regner ut konverteringen fra nautiske mil til km
print(nautiske_mil + " nautiske mil er lik " + str(konvertering) + "km.") # Printer ut kilometer


#UTVIDELSE AV PROGRAMMET SOM REGNER UT BREDDEN OG HØYDEN AV EN SKJERM I CM

diagonal_tommer = input("Skriv inn antall tommer på skjermen: ")                                            # Definerer antall tommer
diagonal_tommer_tall = float(diagonal_tommer)                                                               # Tallet skal ha desimaler
diagonal = 16**2+9**2                                                                                       # Regner ut tallet for 16:9 format
x = (diagonal_tommer_tall**2 / diagonal)**0.5                                                               # Finner lengden på én kloss
bredde = 16*x*2.54                                                                                          # Regner ut bredden i cm
høyde = 9*x*2.54                                                                                            # Regner ut høyden i cm
print("Bredden til skjermen er " + str(bredde) + "cm" + " og høyden til skjermen er " + str(høyde) + "cm.") # Printer ut bredden og høyden i cm


#PROGRAMMET SKAL REGNE UT I ANDRE SKJERMFORMATER ENN 16:9

diagonal_tommer = input("Skriv inn antall tommer på skjermen: ")                                            # Definerer antall tommer
diagonal_tommer_tall = float(diagonal_tommer)                                                               # Tallet skal ha desimaler
a = input("Skriv inn et tall for forholdet b: ")                                                            # Definerer forholdet til bredden
a_bredde = float(a)                                                                                         # Tallet skal ha desimaler
b = input("Skriv inn et tall for forholdet h: ")                                                            # Definerer forholdet til høyden
b_høyde = float(b)                                                                                          # Tallet skal ha desimaler
diagonal = a_bredde**2+b_høyde**2                                                                           # Regner ut tallet for gitt format
x = (diagonal_tommer_tall**2 / diagonal)**0.5                                                               # Finner lengden på én kloss
bredde = a_bredde*x*2.54                                                                                    # Regner ut bredden i cm
høyde = b_høyde*x*2.54                                                                                      # Regner ut høyden i cm
print("Bredden til skjermen er " + str(bredde) + "cm" + " og høyden til skjermen er " + str(høyde) + "cm.") # Printer ut bredden og høyden i cm


#LES PROGRAMKODEN OG FORSTA UTEN A KJORE

masse = input("Skriv inn massen til objektet: ") # Definerer masse
masse_tall = float(masse)                        # Tallet skal ha desimaler
fart = input("Skriv inn farten til objektet: ")  # Definerer fart
fart_tall = float(fart)                          # Tallet skal ha desimaler
resultat = 0.5 * masse * fart**2                 # Regner ut energien (J), men koden vil ikke kjøre fordi masse og fart tolkes som tekst
print(resultat)                                  # Printer ut energien til legemet, dersom koden kjører gjennom