# TEGN EN SERIE MED FIREKANTER HVOR HVER SIDE HAR ULIK FARGE, HVER FIREKANT ER STØRRE ENN FORRIGE, HVER FIREKANT ER ROTERT I FORHOLD TIL FORRIGE

import turtle                         # Importerer turtle

firekant = turtle.Turtle()            # Definerer pilen som tegner som firekant
firekant.speed(0.5)                   # Tegner fortere
turtle.bgcolor("black")               # Endrer bakgrunnsfargen på tegningen til svart

side = 0                              # Definerer siden

for draw in range(50):                # Lager en for-løkke for å endre størrelsen og vinkelen på firekantene
    side += 5                         # Sidene øker med 5 for hver firekant
    firekant.penup()                  # Flytter firekanten til sentrum før den tegner noe
    firekant.goto(0, 0)
    firekant.setheading(draw * 6)     # Endrer vinkelen på hver hele firekant: første = 6, andre = 12 osv.
    firekant.backward(side / 2)       # Flytter firekanten slik at den tegner rundt sentrum og ikke fra sentrum
    firekant.left(90)
    firekant.backward(side / 2)
    firekant.right(90)
    firekant.pendown()                # Starter å tegne her
    for tegn in range(4):             # Lager en for-løkke for å tegne selve firekanten
        firekant.forward(side)        # Tegner 4 linjer og snur 90 grader slik at det blir en kvadrat
        firekant.left(90)
        if tegn == 0:                 # Lager en if-setning der hver side får sin egen farge
            firekant.color("green")
        elif tegn == 1:
            firekant.color("red")
        elif tegn == 2:
            firekant.color("yellow")
        else:
            firekant.color("blue")

turtle.done()                          # Viser fram tegninger og lar den stå


# TEGN EN MANGEKANT HVOR ALLE KANTER ER LIK ANTALL ELEMENTER I LISTA OVER FARGER OG HVOR HVER LINJE HAR SIN EGEN FARGE FRA LISTA

import turtle

kant = turtle.Turtle()
kant.speed(0.5)
turtle.bgcolor("black")

farger = ["red", "yellow", "green", "cyan", "blue", "magenta"]

def mangekant(fargenavn):
    side = 0
    grader = 360 / len(farger)
    for figur in range(50):
        side += 5
        kant.penup()
        kant.goto(0, 0)
        kant.setheading(figur * 6)
        kant.back(side + 1)
        kant.right(grader)
        kant.pendown()
        for kantar in range(len(farger)):
            kant.forward(side)
            kant.left(grader)
            kant.color(farger[kantar])
mangekant(farger)

turtle.done()


# TEGN HELE FIREKANTEN MED SAMME FARGE, MEN HVOR HVER FIREKANT HAR EGEN FARGE OG HVOR FARGEN ENDRER SEG GRADVIS FRA EN FIREKANT TIL DEN NESTE

import turtle                                                                           # Importerer turtle
from matplotlib.colors import LinearSegmentedColormap, to_hex                           # Importerer funksjonen som skaper en overgang mellom farger og gjør om fargekoder til en hex-tekstreng

firekant = turtle.Turtle()                                                              # Definerer pilen som tegner som firekant
firekant.speed(0.5)                                                                     # Tegner fortere
turtle.bgcolor("black")                                                                 # Endrer bakgrunnsfargen på tegningen til svart
side = 250                                                                              # Definerer side
farger = ["#FF0000", "#FFFF00", "#00FF00", "#00FFFF", "#0000FF", "#FF00FF"] # Definerer 6 heksadesimale fargekoder
fargekart = LinearSegmentedColormap.from_list("regnbue", farger)                        # Lager en fargeovergang mellom de 6 fargene

for draw in range(50):                                                                  # Lager en for-løkke for å endre størrelsen og vinkelen på firekantene
    side -= 5                                                                           # Sidene synker med 5 for hver firekant
    firekant.penup()                                                                    # Flytter firekanten til sentrum før den tegner noe
    firekant.goto(0, 0)
    firekant.setheading(draw * 6)                                                       # Endrer vinkelen på hver hele firekant: første = 6, andre = 12 osv.
    firekant.backward(side / 2)                                                         # Flytter firekanten slik at den tegner rundt sentrum og ikke fra sentrum
    firekant.left(90)
    firekant.backward(side / 2)
    firekant.right(90)
    firekant.pendown()                                                                  # Starter å tegne her
    firekant.color(to_hex(fargekart(draw / 49)))                                        # Gjør om fargekodene til hex-tekstreng, og deler på antall firekanter for å regne ut en prosentvis plassering av fargene
    firekant.begin_fill()                                                               # Fyller hele firekanten med fargen
    for tegn in range(4):                                                               # Lager en for-løkke for å tegne selve firekanten
        firekant.forward(side)                                                          # Tegner 4 linjer og snur 90 grader slik at det blir en kvadrat
        firekant.left(90)
    firekant.end_fill()                                                                 # Slutter å fylle firekanten med hele fargen
turtle.done()                                                                           # Viser fram tegninger og lar den stå

