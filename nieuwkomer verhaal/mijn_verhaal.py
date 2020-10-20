import os

def nederland():
    print("je pakt je benodigheden in en gaat naar een transport bedrijf om te vragen of je mee kan reizen.")

def duitsland():
    print("je gaat naar een vriend toe om te vragen hoe je snel naar Duitsland kan komen.")

def vechten():
    print("je vraagt aan je buren of zei weten hoe je snel de leger in kan.\nJe buurman gaf je advies om naar hun kamp te gaan verder op in de stad.\nJe zoekt ze op en ze accepteren je omdat ze nu te kort komen.")

def vluchten():
    print("\nWaar wil je heen gaan?\na.Nederland\nb.Duitsland\nc.vechten\n")
    ans1 = input()
    if ans1.lower() == "a":
        os.system("cls")
        print("je kiest om naar Nederland te vluchten, maar je nog niet wat je nodig heb om naar Nederland te gaan vluchten.")
        nederland()
    elif ans1.lower() == "b":
        os.system("cls")
        print("je kiest om naar Duitsland te gaan, maar je niet hoe je wilt gaan.")
        duitsland()
    elif ans1.lower() == "c":
        os.system("cls")
        print("Je kiest ervoor om je eigen land te helpen met vechten.")
        vechten()


#wat is je naam?
print("Hallo wat is je naam?")
naam = input()
os.system('cls')
print("hallo " + naam + " ,jij gaat in de voeten staan van een vluchteling.\nDus elke antwoordt dat je kiest heeft invloed op je toekomst.")

#begin
print("Je leeft al jaren lang in Syrïe en je weet dat ISIS al een paar jaren bestaat.\nOp een dag sta op, maar je hoort in eens explosies verder op in je stad.\nJe rent naar buiten om te kijken wat er is gebeurt.\nJe ziet allemaal rook van verschillende plekken afkomen.\nJe twijfelt of je wilt blijven om voor je land te vechten of om te vluchten.")
vluchten()