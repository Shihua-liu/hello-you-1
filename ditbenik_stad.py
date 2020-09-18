import sys

print("hallo ik ben shihua, wie ben jij?")
jouwnaam = input()
print("hallo " + jouwnaam + ", welkom bij mijn game. je kan zelf kiezen wat je doet, maar zonder goud kan je niet ver komen in mijn game, daarom ik heb een getal van 1 tot 5 in mijn hoofd. als je het goed heb, krijg je van mij 5 goud, kan jij het raden?")

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

print("laten we verder gaan.")
print("je komt bij een stad en je heb een id nodig om de stad binnen te komen, maar je hebt geen id.")
print("bij de ingang vertel je dat jij je id bent kwijt geraakt. de bewakers zeggen dat je er dan 1 moet kopen voor 2 goud of je gaat 3 zwijnen jagen en verkopen aan de bewakers. de bewakers zorgt er voor dat je een zwaard heb")

if goud <= 1:
   print("je heb geen keuze behalve zwijnen jagen")
if goud >= 2:
   print("a. id kopen voor 2 goud \nb. 3 zwijnen jagen")

answer2 = input()
if answer2.lower() == "a":
   goud = goud - 2
   print("je heb nog " + str(goud) + " goud over")
   print("je bent binnen gekomen, maar je heb geld nodig. je zoekt naar een baan dat je leuk vindt, maar je heb niks gevonden")
   print("je kiest dan om te jagen en dat te verkopen op het markt.")
   print("je hebt ook een zwaard gekocht voor 1 goud")
   goud = goud - 1
   print("je heb nog " + str(goud) + " goud over")
if answer2.lower() == "b":
   print("je gaat de bos in")