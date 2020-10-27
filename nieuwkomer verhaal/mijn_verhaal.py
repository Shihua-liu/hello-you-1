import os
#stuk21
def sparen():
    os.system("cls")
    print("je denk dat het beter is om te sparen voor dat je verder gaat reizen.\nvoor de komen de jaren werk je 6 dagen in een week maar verdien je heel weinig.\nuit windelijk ben je om het leven gekomen vanwege te veel werken\n\n\n\nEINDE")
    

#stuk20
def gebruiken():
    os.system("cls")
    print("je gebruikt je geld om naar een andere land te komen. \nje probeert met verschillende vervoer te gaan, maar bij de grens werd je opgepakt vanwege omdat je het land probeert binnen te komen. je zegt dat je zit te vluchten, maar ze geloven je niet. \nze hebben je in een gevangenis gegooit en je bent heel erg boos dat ze je niet geloven en dat ze je geen hulp geven.\n\n\n\nEINDE")
    

#stuk19
def nederland():
    os.system("cls")
    print("je lift mee met verschillende auto's. \nje heb hulp gevraagt aan verschillende bestuurders hoe het met de vluchtelingen kamp werkt in nederland. \nze hebben het opgezocht en zeiden dat naar de vluchtelingenwerk moesten gaan en dat ze daar verder konnen helpen. \njaren later is de inburgerings proceduren gelukt en je kan normaal leven in Nederland.\n\n\n\nEINDE")
    

#stuk18
def duitsland():
    os.system("cls")
    print("je probeert mee te liften met verschillende auto's en je slaapt in een slaapzak buiten. \nuit eindelijk is het je gelukt om in duitsland te komen naar weken lang reizen. \nje vluchteling procedure duurde sneller dan je dacht. \nuit eindelijk kan je rustig en normaal leven in duitsland.\n\n\n\nEINDE")
    

#stuk17
def blijven():
    os.system("cls")
    print("je vindt dat je genoeg heb gehad en dat je in de vluchtelingen kamp van Griekenland blijft. \nDe eerste paar weken zaten ze je heel goed te verzorgen, maar daarna deden ze niks meer. \nje leven is enorm slecht geworden en het is heel moeilijk te leven. \niedereen steelt van iedereen en jij hoopt dat je snel in griekenland zelf mag wonen, maar je heb na maanden niks gehoord van de regering. \nin de tussentijd heb je een beetje gewerkt om geld te verdienen. \nwat wil je doen met je geld?\n\na.door sparen\nb.gebruiken om verder te reizen.")
    ans8 = input()
    if ans8.lower() == "a":
        sparen()
    else:
        gebruiken()

#stuk16
def doorgaan():
    print("je denk dat het handiger is om verder te reizen naar een andere land te vluchten. \nje heb genoeg geld om een paar maanden te overleven. \nje twijvelt om naar Duitsland of naar Nederland te vluchten.\n\na.Nederland\nb.Duitsland")
    ans9 = input()
    if ans9.lower() == "a":
        nederland()
    else:
        duitsland()


#stuk15
def linkerg():
    os.system("cls")
    print("Je kies er voor om in de linker bootje te zitten en daar in te reizen. \nDe bestuurders komen achter dat de motor stuk is, waardoor het een langer duurt voor dat je vertrekt. Ze hadden afgesproken dat de rechter alvast begint met varen richting griekenland. \n40 minuten later is de boot opgestart en zitten jullie te varen. Je hoopt dat de boot niet zal omkiepen tijdens de rit. \nGelukkig waren jullie veilig aangekomen in griekenland, maar toen je om je heen zat te kijken zie de boot niet dat eerder was gaan gegaan. \nje heb al een gevoel wat er is gebeurt en je kiest er voor om niet door te gaan kijken.\nde vluchtelingen kamp geeft je de keuze om of verder te reizen of in de kampen hier te leven.\n\na.blijven\nb.door reizen\n")
    ans7 = input()
    if ans7.lower() == "a":
        os.system("cls")
        blijven()
    else:
        doorgaan()

#stuk14
def rechterg():
    os.system("cls")
    print("je heb de rechter bootje gekozen en gelukkig had het geen kapotte motor zoals de linker. \nJe was opgelucht dat je niet langer hoefte te wachten maar onderweg is iets erger gebeurd dan een kapotte motor. \nJe bootje was opeens omgekiept. \nIedereen probeerde terug te zwemmen naar de boot om boven water te blijven, maar sommigen hadden dat gehaalt, maar jij had het jammer genoeg niet gehaald.\n\n\n\nEINDE")
    

#stuk13
def verder():
    os.system("cls")
    print("je koos ervoor om door te rijden en gelukkig had je een goede keuze gemaakt, omdat de stad net werd aangevallen. \nBij de grens kwam je zonder problemen er door maar toen je bij de grens was bij Turkije zat werd je aangehouden, omdat je illegale spullen had meegenomen van je huis. \nje vond dat raar en je legt uit dat het in Syrïe heel legaal was, maar de agentan namen dat niet.\nje werdt naar de gevangenis gestuurd om daar een paar maanden te leven\n\n\n\n WORDT VERVOLGT")
    

#stuk12
def stad():
    os.system("cls")
    print("je stopt om wat spullen te kopen zodat verder kan rijden met benodigdheden. \nJammer genoeg was het een hele slechte keuze, omdat na 10 minuten ISIS de stad kwam binnen stormen en je was gevangen genomen en vermoord.\n\n\n\nEINDE")
    

#stuk11
def bootI():
    os.system("cls")
    print("je betaalt je reis zonder problemen, maar onderweg kwamen er problemen aan. \nEr was enorme sterke wind, maar jullie hadden het grote problemen Italïe gehaald. je komt in een vluchtelingen kamp terecht en je leeft daar voor de komen de paar maanden heel erg blij. \nje bent later ook geaccepteerd dat je in Italïe mag wonen.\n\n\n\nEINDE")
    

#stuk10
def bootg():
    os.system("cls")
    print("Je vindt dat met de boot iets sneller dan met de auto en je wilt ook niet de risico nemen dat je wordt opgepakt bij de grens. \nJe heb een kaartje gekocht dicht bij de pier zodat je op een boot kan. \nVerder op zie je 2 kleine bootjes. \nJe kan kiezen voor de linker of de rechter.\n\na.linker\nrechter\n")
    ans4 = input()
    if ans4.lower() == "a":
        linkerg()
    else:
        rechterg()

#stuk9
def auto():
    os.system("cls")
    print("je kiest je auto omdat je erge verhalen heb gehoord over boten en je wilt niet dood gaan. \nna een paar uurtjes rijden zie je stad. \nga je erin om wat te kopen of rij je verder?\n\na.kopen\nb.verder rijden\n")
    ans5 = input()
    if ans5.lower() == "a":
        stad()
    else:
        verder()

#stuk8
def italie():
    os.system("cls")
    print("je kiest er voor om naar Italïe te vluchten, maar je weet niet op welke manier. \nje hebt al eerder gehoord dat via de zee erg gevaarlijk kan zijn, maar als je met je auto gaat kan je opgepakt worden bij de grens van Syrïe.\n\nhoe wil je gaan?\na.auto\nb.boot\n")
    ans3 = input()
    if ans3.lower() == "a":
        bootI()
    else:
        auto()
#stuk7
def griekenland():
    os.system("cls")
    print("je kiest er voor om naar Griekenland te vluchten, maar je weet niet op welke manier. \nje heb al eerder gehoord dat via de zee erg gevaarlijk kan zijn, maar als je met je auto gaat kan je opgepakt worden bij de grens van Syrïe.\n\nhoe wil je gaan?\na.auto\nb.boot\n")
    ans6 = input()
    if ans6.lower() == "a":
        auto()
    else:
        bootg()

#stuk6
def weg_rennen():
    print("je pakt je benodigheden in en je gaat met je auto zo snel mogelijk weg rijden.\nje weet dat je naar europa wilt vluchten, maar je twijvelt naar welke land je wilt vluchten.")
    print("\nwelke land kies je?\na.Griekenland\nb.Italïe")
    ans2 = input()
    if ans2.lower() == "a":
        os.system("cls")
        griekenland()
    else:
        os.system("cls")
        italie()
#stuk5
def aanvallen():
    os.system("cls")
    print("om 6 uur 's ochtend hebben jullie besloten om het aan te vallen. \nDe eerste paar dagen was het moeilijk omdat hun verdediging erg sterk was, maar uit eindelijk was het gelukt om de stad over te nemen. \nJij en je team zaten gebouwen te checken om te kijken of alles veilig was, maar je zag een man die heel hard naar je toe zat te rennen en riep:'Allah akbar.' \nJe gelukkig bent heel zwaar gewond geraakt en je werd getransporteerd naar de eerste hulp. \n\n\n\n WORDT VERVOLDT")
    
#stuk4
def weigeren():
    os.system("cls")
    print("je heb geweigerd en gezegt dat je liever je basis de basis verdedigt. Een paar dagen later werd je basis gebombardeerd en was je jammer genoeg om het leven gekomen. \n\n\n\nEINDE")
    
#stuk3
def vechten():
    os.system("cls")
    print("Je vraagt aan je buren of zei weten hoe je snel de leger in kan.\nJe buurman gaf je advies om naar hun kamp te gaan verder op in de stad.\nJe zoekt ze op en ze accepteren je. Na een paar weken training werd je in gezet om te vechten tegen ISIS. \nMaanden lang zit je ISIS terug te vechten zonder veel problemen. \nOp een dag had je een keuze om een stad aanvallen dat onder de controle was van ISIS.\nwil je het doen\nja of nee?")
    ans_dicht = input()
    if ans_dicht.lower == "ja":
        aanvallen()
    else:
        weigeren()

#stuk2
def vluchten():
    print("\nwat ga je doen?\na.vluchten\nb.vechten voor je land\n")
    ans1 = input()
    if ans1.lower() == "a":
        os.system("cls")
        print("je kiest om te vluchten.")
        weg_rennen()
    elif ans1.lower() == "b":
        os.system("cls")
        print("je probeert jezelf zo snel mogelijk op te geven zodat je tegen ISIS kan vechten. Want je vindt dat ze onnodige dingen doen en dat het je tegen moet protesteren.")
        vechten()


#stuk1
def begin():
    os.system("cls")
    print("Je leeft al jaren lang in Syrïe en je weet dat ISIS al een paar jaren bestaat.\nOp een dag sta op, maar je hoort in eens explosies verder op in je stad.\nJe rent naar buiten om te kijken wat er is gebeurt.\nJe ziet allemaal rook van verschillende plekken afkomen.\nJe twijfelt of je wilt blijven om voor je land te vechten of om te vluchten.")
    vluchten()

#wat is je naam
def naam():
    os.system("cls")
    print("Hallo wat is je naam?")
    naam = input()
    os.system('cls')
    print("hallo " + naam + " ,jij gaat in de voeten staan van een vluchteling.\nDus elke antwoordt dat je kiest heeft invloed op je toekomst.")
    begin()

naam()

while True:
    print("\n\n\nopnieuw?  y/n")
    ansloop = input()
    if ansloop.lower() == "y":
        naam()
        continue
    else:
        os.system("cls")
        break