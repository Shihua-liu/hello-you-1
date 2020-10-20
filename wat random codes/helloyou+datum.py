print("Hello You!, ik ben Shi Hua")
print("Wie ben jij?")
username = input ()
print("Hello " + username)
print("wat is de datum van vandaag?")
date = input ("datum:")
print("En de tijd?")
time = input ("tijd:")
print("dus het is " + date + " en " + time +"?")
answer = input("Enter ja of nee: ") 
if answer == "ja": 
    print("bedankt voor het zeggen")
elif answer =="nee":
    print("oh wat dan?")
    datumtijd = input ("enter datum en tijd")
    print("ok het is dus " + datumtijd)
    print("bedankt voor het zeggen") 
else:
    print("er kan alleen geantwoord worden met ja of nee")