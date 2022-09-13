import random

HP1 = 50
HP2 = 50
gamestatus = True
cooldown1 = 0
block1 = 0

while True:
    while gamestatus == True:

            #Player action
        if cooldown1 == 0:
            print("\033[36m" "Was willst du tun?")
            action = int(input("1.Angreifen; 2.Heilen" "\033[0m"))
            
            #Player attack
            if action == 1:
                zahl = random.randrange(1,10)
                HP2 -= zahl
                print("\033[32m" "Du hast "+ str(zahl) +" Schaden geamcht")
                if HP2 <= 0:
                    print("Du hast GEWONNEN!" "\033[0m")
                    gamestatus = False
                    break
                else:
                    print("Der Gegner hat noch " + str(HP2) + "HP" "\033[0m")
            
            #Player heal
            elif action == 2:
                zahl = random.randrange(1,7)
                HP1 += zahl
                print("\033[32m" "Du heilst dich um "+ str(zahl) + "HP")
                print("Du hast nun "+ str(HP1) +"HP" "\033[0m")
            
            #Player block
            elif action == 3:
                block1 = 1
                print("\033[32m" "Du schützt dich hinter deinem Schild" "\033[0m")

            #Player wrong input
            else:
                print("Wähle eine zulässig Zahl!")
                print("-------------------------------")
                break
        else:
            print("Du setzt eine Runde aus")
        print("-------------------------------")



        #Enemy action
        action2 = random.randrange(1,3)

        #Enemy attack
        if action2 == 1:
            if block1 == 0:
                zahl = random.randrange(1,10)
                HP1 -= zahl
                print("\033[31m" "Der PC hat " + str(zahl) + " Schaden gemacht")
                if HP1 <= 0:
                    print("Der PC hat gewonnen." "\033[0m")
                    gamestatus = False
                    break
                else:
                    print("Du hast noch " + str(HP1) + " HP" "\033[0m")
            else:
                zahl = random.randrange(1,5)
                HP1 -= zahl
                block1 = 0
                print("\033[31m" "Du blockst teile des Schadens mit deinem Schild ab")
                print("Der PC hat " + str(zahl) + " Schaden gemacht")
                if HP1 <= 0:
                    print("Der PC hat gewonnen." "\033[0m")
                    gamestatus = False
                    break
                else:
                    print("Du hast noch " + str(HP1) + " HP" "\033[0m")
        
        #Enemy heal
        else:
            zahl = random.randrange(1,7)
            HP2 += zahl
            print("\033[31m" "Der PC hat sich um " + str(zahl) + "HP geheilt")
            print("Der PC hat jetzt " + str(HP2) + "HP" "\033[0m")
            block1 = 0
        print("-------------------------------")
    
    #Restart or Quit
    if gamestatus == False:
        restart = int(input("1.Neustarten; 2.Beenden"))
        if restart == 1:
            gamestatus = True
            HP1 = 50
            HP2 = 50
            zahl = 0
            block1 = 0
            cooldown1 = 0
        elif restart == 2:
            break
        else:
            print("Wähle zwischen 1 und 2.")