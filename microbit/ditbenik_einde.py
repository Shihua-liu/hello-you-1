import sys

# hier introduceer ik mezelf
print("hallo ik ben shihua, wie ben jij?")
jouwnaam = input()
print("hallo " + jouwnaam + ", welkom bij mijn game. je kan zelf kiezen wat je doet, maar zonder goud kan je niet ver komen in mijn game, daarom ik heb een getal van 1 tot 5 in mijn hoofd. als je het goed heb, krijg je van mij 5 goud, kan jij het raden?")

# hier gok je welke nummer ik heb in mijn hoofd
answer1 = input()
goud = 0
if answer1 == "1":
   print("dat is goed, hier is je 5 goud")
   goud = 5
if answer1 == "2":
   print("jammer, je krijgt 2 goud als troost prijs omdat je dichtbij was")
   goud = 2
if answer1 == "3":
   print("bijna")
   goud = 0
if answer1 == "4":
   print("fout, het was 1")
   goud= 0
if answer1 == "5":
   print("dat is niet eens dichtbij")
   goud = 0
print("je heb nu " + str(goud) + " goud.")

# hier kies je hoe je de stad binnen komt
print("laten we verder gaan.")
print("je komt bij een stad en je heb een id nodig om de stad binnen te komen, maar je hebt geen id.")
print("bij de ingang vertel je dat jij je id bent kwijt geraakt.\n de bewakers zeggen dat je er dan 1 moet kopen voor 2 goud of je gaat 3 zwijnen jagen en verkopen aan de bewakers. de bewakers zorgt er voor dat je een zwaard heb")

# als je 2 of meer goud heb kan je naar binnen gaan
if goud <= 1:
   print("je heb geen keuze behalve zwijnen jagen")
if goud >= 2:
   print("a. id kopen voor 2 goud \nb. 3 zwijnen jagen")

# je wilt geld verdienen
answer2 = input()
if answer2.lower() == "a":
   goud = goud - 2
   print("je heb nog " + str(goud) + " goud over")
   print("je bent binnen gekomen, maar je heb geld nodig.")
   print("je kiest dan om te jagen en dat te verkopen op het markt.")
   print("je hebt ook een zwaard gekocht voor 1 goud")
   goud = goud - 1
   print("je heb nog " + str(goud) + " goud over")
if answer2.lower() == "b":
   print("je gaat de bos in")
# jagen
print("na 5 minuten lopen kom je bij de bos en je ziet gelijk al een paar zwijnen rond lopen.")
print("je hebt zonder problemen alle zwijnen gedood, maar tijdens de tocht naar de ingang werdt je aangevallen door 2 bandieten.")
print("wat ga je doen?")

print("a. wegrennen \nb. vechten \nc. alles geven")

# wat je gaat doen na dat je bent aangevallen
answer3 = input()
if answer3.lower() == "a":
    print("je rent richting de stad toe en je schreeuwt om hulp, maar niemand hoort je. na een paar seconden krijg je een pijl door je hart en je bent in één klap dood.\n \n \n GAME OVER")
    sys.exit()

if answer3.lower() == "b":
    print("je neemt het gevecht aan en het lukt je om eentje erg zwaar gewond te maken, maar de tweede steekt zijn zwaard je hart in. je bent dood.\n \n \n GAME OVER")
    sys.exit()

if answer3.lower() == "c":
   if goud > 0:
    print ("je geeft je goud aan hun en je zwijnen die je net heb gejaagt en ze spaarde je leven.")
   if goud == 0:
    print("je heb je zwijnen aan hen gegeven en verlaten je zonder problemen.")

# hier roep je om hulp
print("je loopt richting de stad toe en onderweg zie je een groep ridders van een bepaalde club.\nJe vertelt wat er is gebeurd en ze gaan er achteraan.")
print("ze hebben niks kunnen vinden en je gaat terug de stad in.")
# hier zoek je werk
print("je begint te denken wat je kan doen, want je hebt niks op zak en je hebt geld nodig om te blijven overleven.\nJe gaat werken waar een plekje over is.")
print("wat ga je kiezen?")
print("a. in een bar werken.\nb. bij een winkel.\nc. bij de bouw.\nd. je geeft je zelf op voor de leger")
answer4 = input()
if answer4.lower() == "a":
   print("je begint te werken in een bar genaamd:'the dakin'.\nVoor de komende paar maanden werk je daar elke dag. Je kies om een appartement te kopen en je heb geen problemen om je huur te betalen.\nde rest van je leven kies je er voor om bij de bar te werken.\n \n \n EINDE")
   sys.exit()

elif answer4.lower() == "b":
   print("je liep de winkel binnen en je werdt gelijk aan genomen omdat ze nog naar werknemers zochten.\nOp een dag werdt je winkel berooft terwijl je zat te werken.\nJe probeerd om ze te stoppen, maar ze hadden je binnen een minuut dood gemaakt.\n \n \n GAME OVER")
   sys.exit()

elif answer4.lower() == "c":
   print("je soliciteer je en op je eerste dag was je bij een ongeluk en viel een huis in elkaar en jij was een van de slachtoffers.\n \n \n GAME OVER")
   sys.exit()

elif answer4.lower() == "d":
   print("je ging jezelf opgeven op om de leger in te gaan en een maand later breekt een oorlog uit met een andere land.\nJe stond voor in maar toen ze gingen aanvallen  was je zwaar gewond geraakt en een paar minuten later was je dood gegaan van bloedingen.\n \n \n GAME OVER")
   sys.exit()