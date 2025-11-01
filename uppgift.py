class Sallad: #Skapar Sallads-klassen
    def __init__(self, namn, pris, ingredienser):#instansvariabler, namn ex:Grekisk Sallad (str) pris ex:87 (int) och ingredienser ex: tomat,gurka,parmesan(set)
        self.namn = namn.strip()
        self.pris = pris
        self.ingredienser = set(i.strip().lower() for i in ingredienser)

    def match(self, valdaIngredienser): #returnerar en int som visar endast de som bara är i valdaingrediener och ingredienser
        return len(self.ingredienser & valdaIngredienser)

    def mismatch(self, valdaIngredienser):#returnerar en int som endast visar antalet ingredienser som inte valdes
        return self.ingredienser - valdaIngredienser

    def __str__(self): #används vid print(sallad)
        ingredienserLista = sorted(self.ingredienser)
        return f"{self.namn} ({self.pris} kr): {', '.join(ingredienserLista)}"


def lasInIngredienser(filnamn): #läser in ingredienser.txt och skapar en ordbok med value = pris och key = ingrediens
    ingredienser = {}
    fil = open(filnamn, "r", encoding="utf-8") #filen öppnas
    for rad in fil:
        rad = rad.strip()
        if not rad or rad.startswith("#"): #skippar tomma rader och kommentarer
            continue
        if ";" in rad: 
            namn, pris = rad.split(";") #delar vid semikolon
            ingredienser[namn.strip().lower()] = int(pris.strip()) #här skapas dicten
    fil.close() #stänger filen
    print(f"Läste in {len(ingredienser)} ingredienser")
    return ingredienser


def lasInSallader(filnamn): #skapar en lista med sallader som blir salladsobjekt p.g.a class Sallad
    sallader = []
    fil = open(filnamn, "r", encoding="utf-8") #öppnas
    for rad in fil:
        rad = rad.strip()
        if not rad or rad.startswith("#"):#skippar tomma rader och kommentarer
            continue
        if ";" in rad:
            delar = [d.strip() for d in rad.split(";")]
            namn = delar[0]#första indexet är namnet
            pris = int(delar[1])#andra är priset
            ingrediensStrang = delar[2]
            ingrediensLista = [i.strip().lower() for i in ingrediensStrang.split(",")]#ingredienserna blir en lista i en lista. som delas vid komma istället för semikolon
            sallader.append(Sallad(namn, pris, ingrediensLista))
    fil.close()#stänggg
    print(f"Läste in {len(sallader)} sallader")
    return sallader


def hamtaValdaIngredienser(tillgangligaIngredienser):# här skriver användaren in sina ingredienser den vill ha. Dessa placeras i en set för att enkelt kunna jämföra med sallads objekten som finns
    valda = set()
    print("\nVälj ingredienser (skriv en i taget, enter för att avsluta):")
    while True:
        ingrediens = input("> ").strip().lower()
        if not ingrediens:
            break
        if ingrediens in tillgangligaIngredienser:
            valda.add(ingrediens)
            print(f" {ingrediens} tillagd... beep...boop...")
        else:
            print(f" '{ingrediens}' Du må söka annanstädes för denna ingrediens")
    return valda


def hittaBastaSallad(sallader, valdaIngredienser):
    perfektaMatchningar = []#kollar om samtliga ingredienser ingår i salladen
    for sallad in sallader:#går igenom alla index i sallader-listan
        if valdaIngredienser.issubset(sallad.ingredienser):#issubset returnerar true om alla valdaingredienser finns
            perfektaMatchningar.append(sallad)#då läggs den till
    
    if perfektaMatchningar:
        return perfektaMatchningar, True, False
    
    # Hitta alla sallader med flest matchningar
    salladerMedFlestMatch = []
    flestMatch = 0
    #räknar hur många ingredienser som varje sallad matchar
    for sallad in sallader: #ytterligare loop
        antalMatch = sallad.match(valdaIngredienser) #antalMatch blir integer från metoden
        if antalMatch > 0:
            if antalMatch > flestMatch:
                flestMatch = antalMatch
                salladerMedFlestMatch = [sallad]
            elif antalMatch == flestMatch:
                salladerMedFlestMatch.append(sallad)
    
    if not salladerMedFlestMatch: #om alla sallader är piss och inte matchar
        return [], False, False
    
    # Om flera har samma antal matchningar, välj den billigaste
    if len(salladerMedFlestMatch) > 1:
        billigast = salladerMedFlestMatch[0]  # Starta med första salladen
    
        for sallad in salladerMedFlestMatch:
            if sallad.pris < billigast.pris:
                billigast = sallad
    
    return [billigast], False, True #returnerar en lista på sallader, arPerfekt och ärBilligastVal
    


def visaMatchandeSallader(matchandeSallader, valdaIngredienser, arPerfekt, arBilligastVal):# nu ska vi visa salladerna
    if not matchandeSallader:#om inga sallader är klockrena
        print("Inga sallader matchar dina valda ingredienser.")
        return False
    
    
    if arPerfekt: #vi ser från förra funktionen att om denne får värdet True händer detta
        print(f" PERFEKT: {', '.join(sorted(valdaIngredienser))}")
    elif arBilligastVal:#om denne dock får värdet True händer detta
        sallad = matchandeSallader[0]
        print(f"Billigaste alternativet")
        print(f"Flera sallader matchar {sallad.match(valdaIngredienser)} ingredienser")
        print(f"Denna väljs för att den är billigast, vi förutsätter att i Kristerssons Sverige är plånboken lövtunn:")
    else:
        print(f" BRA MATCHNINGAR: {', '.join(sorted(valdaIngredienser))}")
    
    
    index = 1 #en räkneoperation
    for sallad in matchandeSallader:
        print(f"{index}. {sallad.namn} - {sallad.pris} kr")
        print(f"   Innehåller: {', '.join(sorted(sallad.ingredienser))}")
        if not arPerfekt:
            matchCount = sallad.match(valdaIngredienser)
            print(f"   Matchar {matchCount} av {len(valdaIngredienser)} valda ingredienser")
        print()
        index += 1
    return True


def valjSallad(matchandeSallader): # nu måste man ju välja salladen som man tycker är bäst
    if len(matchandeSallader) == 1: #finns det bara en relevant sallad är det ju onödigt att hålla på att skriva
        print("Det finns bara en matchande sallad. Väljer den automatiskt.")
        return matchandeSallader[0]
    
    while True:
        val = input("\nVälj en sallad (ange nummer, sedan enter): ").strip()
        if not val:
            print("Välj ett nummer från listan.")
            continue
        if val.isdigit():
            valtNummer = int(val)
            if 1 <= valtNummer <= len(matchandeSallader):#kontrollerar giltiga intervallet. måste vara större änlika med 1 och mindreän lika med max antal matchande sallader
                valdSallad = matchandeSallader[valtNummer - 1] #konverterar integers (uno,dos,tres) till index (zero,uno,dos)
                print(f"Ditt val: {valdSallad.namn}")
                return valdSallad
        print(f"Välj ett nummer mellan 1 och {len(matchandeSallader)}")


def laggaTillExtraIngredienser(tillgangligaIngredienser, nuvarandePris):#man bör lägga till parmesan på sin sallad. Denna funktion tillåter det
    extraIngredienser = []#skapar en lista
    totalPris = nuvarandePris#denna är här för att uppdateras senare
    print(f"\nVill du lägga till extra ingredienser? jaa det är klart")
    print("(Skriv ingrediensnamn, enter för att avsluta)")#glasklart vad användaren skall göra
    #inget knasigt här egentligen
    while True:
        val = input("> ").strip().lower()
        if not val:
            break
        if val in tillgangligaIngredienser:
            extraPris = tillgangligaIngredienser[val]#nyttjar ordboken och således kan priset uppdateras
            extraIngredienser.append(val)#
            totalPris += extraPris#uppdateringen
            print(f" {val} tillagd (+{extraPris} kr)")
            print(f"Totti {totalPris}")
        else:
            print(f" '{val}' finns inte i menyn")
    return extraIngredienser, totalPris


def skrivKvitto(sallad, extraIngredienser, totalPris, filnamn="kvitto.txt"):
    fil = open(filnamn, "w", encoding="utf-8")
    fil.write("GRAZIE GRAZIE!\n")
    fil.write(f"Sallad: {sallad.namn} kostade {sallad.pris}:kr\n")
    fil.write(f"Ingredienser: {', '.join(sorted(sallad.ingredienser))}\n")
    if extraIngredienser:
        fil.write(f"Extra: {', '.join(extraIngredienser)}\n")
    fil.write(f"TOTTI: {totalPris} kr\n")
    fil.write("Du är tämligen välkommen tillbaks!!\n")
    fil.close()
    print(f"\n Ditt kvitto går att finna i '{filnamn}'")


def main(): #nu till huvudprogrammet som läser in filerna och rattar användarinput
    print("Välkommen till min Salladsbar!")
    # Läs in data från filer
    ingredienser = lasInIngredienser("ingredienser.txt")
    sallader = lasInSallader("sallader.txt")
    # Kontrollera att filinläsningen lyckades
    if not ingredienser or not sallader:
        print("Kunde inte starta programmet. Troligtvis något fuffens med filerna.")
        return
    # Låt användaren välja ingredienser
    valda = hamtaValdaIngredienser(ingredienser) #användaren skriver vad denne vill ha
    if not valda:
        print("Inga ingredienser valda. Avslutar.")
        return
    # Hitta bästa matchande sallader baserat på användarens val
    matchandeSallader, arPerfekt, arBilligastVal = hittaBastaSallad(sallader, valda) # här är den här listan med sallader samt två boolean värden. Beroende på vad dessa är blir outputen olika. 
    #kallas tuple-unpacking
    # Visa matchande sallader - om inga finns, avsluta programmet
    if not visaMatchandeSallader(matchandeSallader, valda, arPerfekt, arBilligastVal): #om denna är tom
        return
    # Låt användaren välja en sallad från de matchande alternativen
    valdSallad = valjSallad(matchandeSallader) #salladen man valde
    # Lägg till extra ingredienser till den valda salladen
    extra, totalPris = laggaTillExtraIngredienser(ingredienser, valdSallad.pris) # tillaggda ingredienser med 
    # Skriv ut sammanfattning av beställningen
    print("Summan av kardemumman")
    print(f"Sallad: {valdSallad.namn}")
    print(f"Baspris: {valdSallad.pris} kr")
    if extra:
        print(f"Extra ingredienser: {', '.join(extra)}")
    print(f"TOTALPRIS: {totalPris} kr")
    print("önskas kvitto? skriv j' för ja och 'n' för nej")
    sistaValet=input(">")
    if sistaValet == "j":
        skrivKvitto(valdSallad, extra, totalPris)
    else:
     # Spara kvitto till fil och avsluta programmet
        print("\nTack för besöket! Smaklig måltid! Farväl! ")
main()