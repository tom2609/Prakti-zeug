import random

gamestatus = True
HP = 50
HP2 = 50
zahl = 0

while True:
    while gamestatus == True:
        #Spielerphase
        print("\033[36m" "Was willst du machen?")
        aktion = int(input("1. Angriff; 2. Heilen" "\033[0m"))
        if aktion == 1:
            zahl = random.randrange(1,10)
            HP2 -= zahl
            print("\033[32m" "Du hast " + str(zahl) + " Schaden gemacht")
            if HP2 <= 0:
                print("Du hast gewonnen." "\033[0m")
                gamestatus = False
                break
            else:
                print("Der PC hat noch " + str(HP2) + " HP" "\033[0m")
        elif aktion == 2:
            zahl = random.randrange(1,7)
            HP += zahl
            print("\033[32m" "Du hast dich um " + str(zahl) + " geheilt")
            print("Du hast jetzt " + str(HP) + " HP" "\033[0m")
        else:
            print("Eingabe nicht erkannt!")

        
        #PCphase
        aktion2 = random.randrange(1,3)
        if aktion2 == 1:
            zahl = random.randrange(1,10)
            HP -= zahl
            print("\033[31m" "Der PC hat " + str(zahl) + " Schaden gemacht")
            if HP <= 0:
                print("Der PC hat gewonnen." "\033[0m")
                gamestatus = False
                break
            else:
                print("Du hast noch " + str(HP) + " HP" "\033[0m")
        else:
            zahl = random.randrange(1,7)
            HP2 += zahl
            print("\033[31m" "Der PC hat sich um " + str(zahl) + "HP geheilt")
            print("Der PC hat jetzt " + str(HP2) + "HP" "\033[0m")

    if gamestatus == False:
        restart = int(input("\033[0m" "1.Neustarten; 2.Beenden" "\033[0m"))
        if restart == 1:
            gamestatus = True
            HP = 50
            HP2 = 50
            zahl = 0
        elif restart == 2:
            break
        else:
            print("Wähle zwischen 1 und 2.")