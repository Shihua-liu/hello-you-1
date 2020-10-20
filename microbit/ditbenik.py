print("hallo ik ben shihua, wie ben jij?")
jouwnaam = input()
print("hallo " + jouwnaam + ", welkom bij mijn game. je kan zelf kiezen wat je doet, maar zonder goud kan je niet verder in mijn game, daarom ik heb een getal van 1 tot 5 in mijn hoofd. als je het goed ben krijg je van mij 5 goud, kan jij het raden?")
answer1 = input()
if answer1 == "1":
   print("dat is goed, hier is je 5 goud")
   goud = "5"
if answer1 == "2":
   print("jammer, je krijgt 1 goud als troost prijs omdat je dichtbij was")
   goud = "1"
if answer1 == "3":
   print("bijna")
   goud = "0"
if answer1 == "4":
   print("fout, het was 1")
   goud= "0"
if answer1 == "5":
   print("dat is niet eens dichtbij")
   goud = "0"
print("je heb nu " + goud + " goud.")
print("laten we verder gaan.")
print("je komt bij een stad en je heb een id nodig om de stad binnen te komen, maar je heb geen id.")
print("bij de ingang vertel je dat jij je id bent kwijt geraakt. de bewakers zeggen dat je er dan 1 moet kopen voor 2 goud of je gaat 3 zwijnen jagen en verkopen aan de bewakers. de bewakers zorgt er voor dat je een zwaard heb")
print("wat ga je doen?")
print("a. id kopen voor 2 goud \nb. 3 zwijnen jagen")
answer2 = input()
if answer2 == "a":
   goud = goud - 2
   print("je heb nog " + goud + " goud over")
if answer2 == "A":
   goud = goud - 2
if answer2 == "b": 
   print("je gaat de bos in")
if answer2 == "B":
   print("je gaat de bos in")