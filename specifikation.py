# En lista av Salladsobjekt där varje sallad har instansvariablerna. namn, pris och ingredienser
# namn på salladen
# pris på salladen
# och en lista med ingredienser

# I kronologisk ordning skall följande ske.
# Först skall filerna sallader.txt och ingredienser.txt läsas in och skapa en lista med Sallad-objekt respektive en ingrediens ordbok som innehåller all relevant information.

# Sedan skall en funktion som hanterar användarinmatning skapas

# Sedan skall en funktion som hittar den bästa salladen skapas
# Sedan skall en funktion som visar de lämpliga salladerna visas
# Sedan skall en funktion som ger användaren möjligheten att välja den mest lämpliga salladen skapas
# Sedan skall en funktion som ger användaren möjligheten att lägga till extraingredienser skapas
# Sedan skall en funktion som skapar en kvitto skapas
# Sedan skall en mainfunktion som binder ihop alla dessa rörliga delar skapas
class Sallad: #Skapar Sallads-klassen
    def __init__(self, namn, pris, ingredienser):
        pass
    def match(self, valdaIngredienser):
        pass
    def mismatch(self, valdaIngredienser):
        pass
    def __str__(self):
        pass
def lasInIngredienser(filnamn):
    #kod som läser in ingredienserna
    pass
def lasInSallader(filnamn):
    #kod som läser in Salladerna
    pass
def hamtaValdaIngredienser(tillgangligaIngredienser):
    #kod som låter användaren knappa in de ingredienser han har
    pass
def hittaBastaSallad(sallader, valdaIngredienser):
    #kod som letar efter den bästa sallader
    pass
def visaMatchandeSallader(matchandeSallader, valdaIngredienser, arPerfekt, arBilligastVal):
    #kod som visar upp de sallader som hittaBastaSallad hittade
    pass
def valjSallad(matchandeSallader):
    #kod som låter användaren välja vilken sallad den vill ha av de som erbjöds av visaMatchandeSallader
    pass
def laggaTillExtraIngredienser(tillgangligaIngredienser, nuvarandePris):
    #låter användaren lägga till ingredienser
    pass
def skrivKvitto(sallad, extraIngredienser, totalPris, filnamn):
    #skriver kvitto på fil
    pass
def main():
    #limmet, ryggraden i hela programmet som binder ihop alla funktioner
    #sallader = lasInSallader
    #ingredienser = lasInIngredienser
    #hamtavaldaIngredienser, returnerar valdaIngredienser
    #hittabästasallad nyttjar dessa ingredienser och dubbelkollar salladerna. Returnerar en tuple unpacking, list, bool bool
    #visa matchande sllader väljer vad den vill göra utifrån vad det står i tuple unpackingen
    #ifall en viss grej hände hoss visaMatchandeSallader används valjSallad, exempelvis om det finns flera lämpliga sallader men ingen klockren. Finns det en klock
    #ren behvs inte denne
    #nu om vederbörande vill lägga till ingredienser
    #skriv kvittot

    pass