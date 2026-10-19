class Bok:                                                                                # Definerer klassen Bok
    def __init__(self, tittel, forfatter, utgivelsesår, eksemplar_totalt = 1):            # Skriver inn parametere der self er boken som lages nå
        self.tittel = tittel
        self.forfatter = forfatter
        self.utgivelsesår = utgivelsesår
        self.eksemplar_totalt = eksemplar_totalt
        self.eksemplar_na = eksemplar_totalt

    def __str__(self):                                                                    # Definerer funksjonen som skriver ut teksten for bokinfo
        if self.eksemplar_na > 0:
            tilgjengelighet = f"{self.eksemplar_na} eksemplar er tilgjengelig for utlån"
        else:
            tilgjengelighet = "Det er ingen eksemplarer tilgjenglig for utlån!"
        
        return f"{self.tittel} av {self.forfatter}. Utgivelsesår: {self.utgivelsesår}, Antall eksemplarer: {self.eksemplar_totalt}, Tilgjengelige eksemplarer: {tilgjengelighet}"

    def laan_ut(self):                                                                    # Definerer funksjonen for å låne bøker
        if self.eksemplar_na > 0:                                                         # Sjekker om det finnes bøker i biblioteket
            self.eksemplar_na -= 1                                                        # Boken som blir lånt ut blir trukket ut fra biblioteket
            print(f"KVITTERING: Utlån vellykket. Du har lånt {self.tittel}.")
            return True
        else:
            print(f"KVITTERING: Utlån mislykkes. {self.tittel} er allerede lånt ut.")     # Hvis ikke mulig, så vil det gi beskjed om at boka ikke er tilgjengelig
            return False

    def lever_inn(self):                                                                  # Definerer funksjonen for å levere bøker
        if self.eksemplar_na == self.eksemplar_totalt:                                    # Sjekker om alle bøkene er på plass
            print(f"KVITTERING: Innlevering mislykkes. {self.tittel} er allerede levert inn.")
            raise ValueError("Alle eksemplarer er på plass!")
        else:
            self.eksemplar_na += 1                                                        # Hvis ikke, så er det mulig å levere bøker
            print(f"KVITTERING: Innlevering vellykket. Du har levert {self.tittel}")
            return True

        
                                                                                          # Oppretter noen bokobjekter basert på gitt parametere
bok1 = Bok("Starting out with Python, 6. utgave", "Tony Gaddis", int(2000))
bok2 = Bok("Python for realfag, 3. utgave", "Finn Aakre Hugen og Marius Lysaker", int(1980))
bok3 = Bok("Objektorientert programmering med Python", "Henrik Hillestad Løvold", int(2019))

                                                                                          # Skriver ut informasjon om bøkene
print(bok1)
print(bok2)
print(bok3)
utlaan = bok1.laan_ut()                                                                   # Tester ut utlån
print(f"Lån av bok1: {utlaan}")
utlaan_2 = bok2.laan_ut()
print(f"Lån av bok2: {utlaan_2}")
utlaan_3 = bok3.laan_ut()
print(f"Lån av bok3: {utlaan_3}")

print("\n--- Status etter utlån ---")                                                     # Sjekker statusen etter at bøkene er lånt ut
print(bok1)
print(bok2)
print(bok3)

innlevering = bok1.lever_inn()                                                            # Tester ut innlevering
print(f"Levering av bok1: {innlevering}")
innlevering_2 = bok2.lever_inn()
print(f"Levering av bok2: {innlevering_2}")
innlevering_3 = bok3.lever_inn()
print(f"Levering av bok3: {innlevering_3}")

print("\n--- Status etter innlevering ---")                                               # Sjekker statusen etter at bøkene er lånt ut
print(bok1)
print(bok2)
print(bok3)


print("\n--- Ny bibliotek ---")
class bibliotek:                                                                          # Definerer en ny klasse som bibliotek
    def __init__(self, boker_liste = None):                                               # Gir en default verdi som sier at bokser_liste = None
        if boker_liste is None:                                                           # Hvis None, så skriver den ut en tom liste
            self.boker = []
        else:
            self.boker = boker_liste

    def legg_til_bok(self, ny_bok):                                                       # Lager en funksjon for å legge til bøker
        self.boker.append(ny_bok)


    def vis_alle_boker(self):                                                             # Lager en funksjon som viser hele biblioteket etter at bøkene er lagt inn
       for bok in self.boker:
           print(bok)

mitt_biblotek = bibliotek()                                                               # Definerer klassen bibliotek som et annet variabel
#mitt_biblotek.legg_til_bok(bok1)                                                         # Legger til bok1, bok2 og bok3
#mitt_biblotek.legg_til_bok(bok2)
#mitt_biblotek.legg_til_bok(bok3)
#mitt_biblotek.vis_alle_boker()                                                           # Bruker klassen og funksjonen til å skrive ut hele biblioteket

print("\n--- Menysystem ---")

print("1 Legg til bok? \n2 Lån bok. \n3 Lever bok. \n4 Vis bibliotek.")                   # Overskrift for hva brukeren kan gjøre
while True:                                                                               # Lager en while-løkke
    try:
        valg = int(input("\nHva vil du gjøre? "))                                         # Brukeren må velge et tall mellom 1-4 for å gjøre det han vil, hvis ikke vil det gi en feilmelding
    except ValueError:
        print("Bruk tall for å definere det du vil gjøre.")
        continue

    if valg == 1:                                                                         # Brukeren har muligheten til å legge til en bok inn i biblioteket
        book = Bok(input("Tittel: "), input("Forfatter: "), input("Utgivelsesår: "))
        mitt_biblotek.legg_til_bok(book)

    elif valg == 2:                                                                       # Brukeren prøver å låne bok
        if len(mitt_biblotek.boker) == 0:                                                 # Sjekker om det er bøker i biblioteket, hvis ikke så gir det en feilmelding
            print("Biblioteket er tom, legg inn en bok først.")
            continue
        mitt_biblotek.vis_alle_boker()
        while True:
            try:
                bok_valg = int(input("Hvilket boknummer vil du låne (0, 1, 2, ...)? "))   # Brukeren kan velge en boknummer basert på lengden på antall bøker
            except ValueError:
                print("Velg en av de tilgjengelige boknummerene!")
                continue
            if bok_valg >=0 and bok_valg < len(mitt_biblotek.boker):                      # Sjekker om brukerens nummer er gyldig
                mitt_biblotek.boker[bok_valg].laan_ut()                                   # Hvis gyldig er det mulig å låne
                break
            else:
                print("Dette boknummeret finnes ikke i biblioteket")

    elif valg == 3:                                                                       # Brukeren prøver å levere bok 
        if len(mitt_biblotek.boker) == 0:
            print("Biblioteket er tom, legg inn en bok først.")                           # Sjekker om det er bøker i biblioteket, hvis ikke så gir det en feilmelding
            continue
        mitt_biblotek.vis_alle_boker()
        while True:
            try:
                bok_levering = int(input("Hvilket boknummer vil du levere (0, 1, 2, ...)? ")) # Brukeren kan velge en boknummer basert på lengden på antall bøker
            except ValueError:
                print("Velg en av de tilgjengelige boknummerene!")
                continue
            if bok_levering >=0 and bok_levering < len(mitt_biblotek.boker):              # Sjekker om brukerens nummer er gyldig
                try:
                    mitt_biblotek.boker[bok_levering].lever_inn()                         # Hvis gyldig er det mulig å levere
                except ValueError:
                    print("Alle eksemplarer er allerede på plass i biblioteket.")
                break
            else:
                print("Dette boknummeret finnes ikke i biblioteket")
    
    elif valg == 4:
        while True:
            if len(mitt_biblotek.boker) == 0:
                print("Biblioteket er tomt! Legg inn bøkene du vil låne.")
                break
            else:
                mitt_biblotek.vis_alle_boker()
                break
            
    else:
        print("Ugyldig menyvalg, vennligst velg mellom 1, 2, 3 og 4")
        continue