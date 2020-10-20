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
