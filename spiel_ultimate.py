import random
import time

player_health = 20
enemy_health = 20
action = 0
game = True
retry = 0
timeout = False
enemy_timeout = False

while True:

    while game == True:

        if timeout == False:
            print("Du bist dran: ")
            print("\033[1m"+"Du hast "+str(player_health)+" Leben, dein Gegner hat "+str(enemy_health)+" Leben"+"\033[0m")
            action = int(input("\033[31m"+"Angreifen (1), "+"\033[32m"+"Heilen (2), "+"\033[36m"+"Special Attack (3) "+"\033[0m"))
            print("-------------------------------------------------------------------------------")
            time.sleep(random.randrange(0,2))

            while action != 1 and action != 2 and action != 3:
                print("Du bist dran: ")
                print("\033[1m"+"Du hast "+str(player_health)+" Leben, dein Gegner hat "+str(enemy_health)+" Leben"+"\033[0m")
                action = int(input("\033[31m"+"Angreifen (1), "+"\033[32m"+"Heilen (2), "+"\033[36m"+"Special Attack (3) "+"\033[0m"))
                print("-------------------------------------------------------------------------------")
                time.sleep(random.randrange(0,2)) 

            if action == 1:
                print("Du hast "+"\033[31m"+"Angriff "+"\033[0m"+"ausgewählt: ")
                attack = random.randrange(1,10)
                print("Du hast "+str(attack)+" Schaden gemacht")
                enemy_health = enemy_health-attack
                if enemy_health <= 0:
                    print("-------------------------------------------------------------------------------")
                    print("\033[32m"+"Du hast Gewonnen! Dein Gegner ist tot"+"\033[0m")
                    print("-------------------------------------------------------------------------------")
                    game = False
                    break
                else:
                    print("\033[1m"+"Dein Gegner hat noch "+str(enemy_health)+" Leben"+"\033[0m")
                    print("-------------------------------------------------------------------------------")
                time.sleep(random.randrange(0,2))

            elif action == 2:
                print("Du hast "+"\033[32m"+"Heilen "+"\033[0m"+"ausgewählt: ")
                heal = random.randrange(1,10)
                print("Du hast dich um "+str(heal)+" Leben geheilt")
                player_health = player_health+heal
                print("\033[1m"+"Du hast jetzt "+str(player_health)+" Leben"+"\033[0m")
                if player_health > 100:
                    print("-------------------------------------------------------------------------------")
                    print("\033[32m"+"Du hast Gewonnen! Du bist Unbesiegbar"+"\033[0m")
                    print("-------------------------------------------------------------------------------")
                    game = False
                    break
                print("-------------------------------------------------------------------------------")
                time.sleep(random.randrange(0,2))
            
            elif action == 3:
                print("Du hast "+"\033[36m"+"Special Attack "+"\033[0m"+"ausgewählt: ")
                print("Du machst diese Runde 15 Schaden, aber setzt nächste Runde aus")
                special_attack = 15
                enemy_health = enemy_health-special_attack
                if enemy_health <= 0:
                    print("-------------------------------------------------------------------------------")
                    print("\033[32m"+"Du hast Gewonnen! Dein Gegner ist tot"+"\033[0m")
                    print("-------------------------------------------------------------------------------")
                    game = False
                    break
                else:
                    print("\033[1m"+"Dein Gegner hat noch "+str(enemy_health)+" Leben"+"\033[0m")
                    print("-------------------------------------------------------------------------------")
                timeout = True
                time.sleep(random.randrange(0,2))

        elif timeout == True:
            print("Du bist dran: ")
            print("Du hast letzte Runde "+"\033[36m"+"Special Attack "+"\033[0m"+"ausgewählt, du musst dich regenerieren")
            print("Du hast diese Runde kein Schaden gemacht")
            print("-------------------------------------------------------------------------------")
            timeout = False
            time.sleep(5)

        if enemy_timeout == False:
            print("Dein Gegner ist dran: ")
            enemy_action = random.randrange(1,4)

            if enemy_action == 1:
                print("Dein Gegner hat "+"\033[31m"+"Angriff "+"\033[0m"+"ausgewählt: ")
                attack = random.randrange(1,10)
                print("Dein Gegner hat dir "+str(attack)+" Schaden gemacht")
                player_health = player_health-attack
                if player_health <= 0:
                    print("-------------------------------------------------------------------------------")
                    print("\033[31m"+"Du hast Verloren, du wurdest besiegt"+"\033[0m")
                    print("-------------------------------------------------------------------------------")
                    game = False
                    break
                else:
                    print("\033[1m"+"Du hast noch "+str(player_health)+" Leben"+"\033[0m")
                    print("-------------------------------------------------------------------------------")
                time.sleep(random.randrange(0,2))

            elif enemy_action == 2:
                print("Dein Gegner hat "+"\033[32m"+"Heilen "+"\033[0m"+"ausgewählt: ")
                heal = random.randrange(1,10)
                print("Dein Gegner hat sich um "+str(heal)+" Leben geheilt")
                enemy_health = enemy_health+heal
                print("\033[1m"+"Dein Gegner hat jetzt "+str(enemy_health)+" Leben"+"\033[0m")
                if enemy_health > 100:
                    print("-------------------------------------------------------------------------------") 
                    print("\033[31m"+"Du hast Verloren! Dein Gegner ist Unbesiegbar"+"\033[0m")
                    print("-------------------------------------------------------------------------------")
                    game = False
                    break
                print("-------------------------------------------------------------------------------")
                time.sleep(random.randrange(0,2))
            
            elif enemy_action == 3:
                print("Dein Gegner hat "+"\033[36m"+"Special Attack "+"\033[0m"+"ausgewählt: ")
                print("Er machst diese Runde 15 Schaden, aber setzt nächste Runde aus")
                special_attack = 15
                player_health = player_health-special_attack
                if player_health <= 0:
                    print("-------------------------------------------------------------------------------")
                    print("\033[31m"+"Du hast Verloren! Du wurdest besiegt"+"\033[0m")
                    print("-------------------------------------------------------------------------------")
                    game = False
                    break
                else:
                    print("\033[1m"+"Du hast noch "+str(player_health)+" Leben"+"\033[0m")
                    print("-------------------------------------------------------------------------------")
                enemy_timeout = True
                time.sleep(random.randrange(0,2))

        elif enemy_timeout == True:
            print("Dein Gegner ist dran: ")
            print("Dein Gegner hat letzte Runde "+"\033[36m"+"Special Attack "+"\033[0m"+"ausgewählt, er muss sich regenerieren")
            print("Dein Gegner hat diese Runde kein Schaden gemacht")
            print("-------------------------------------------------------------------------------")
            enemy_timeout = False
            time.sleep(5)
    
    if game == False:
        while retry != 1 and retry != 2:
            retry = int(input("\033[32m"+"Nochmal spielen (1)"+"\033[0m"+"\033[1m"+" oder "+"\033[0m"+"\033[31m"+"Beenden (2) "+"\033[0m"))
            if retry == 1:
                player_health = 20
                enemy_health = 20
                game = True
                timeout = False
                enemy_timeout = False
            elif retry == 2:
                quit() 
    retry = 0