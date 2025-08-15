import random

# Introducerea

print(f"\nBuna ziua! Tu - Aventurier, si tu incepi o noua aventura! \nTu ai cazut intro locatie, dar nus tii cum ai cazut aici si tu trebuie sa iesi din locatia asta pina la palatul regelui. \nNoroc Tie!\n")

# Locatia
locations = {
    "padurea": {"desc": "Тu esti in padure, poti sa mergi spre munti, spre fum sau la o casuta, ce alegi: \n", "alegere": ["munti", "fum", "casuta"]},
    "casuta": {"desc": "Tu esti in casuta, aici gasesti o carte, cred ca a unui om, poti a citesti sau sa lasi cartea si sa mergi spre padure sau dupa casa pe drumul mai departe, ce alegi: \n", "alegere": ["citesti", "padurea", "drum"]},
    "drum": {"desc": "Tu ai mers pe drum si ai ajuns la padurea magiei, aici lai gasit pe sarpele rau si iti zice: \n", "alegere": ["padurea", "excalibur"]},
    "citesti": {"desc": "Tu ai citit cartea, si ai aflat ca palatul regelui se afla dupa vulca, dar sunt 2 drumuri spre asta, poti merge si ucide draconul care se afla la vulcan si ajungi la palatul regelui sau sa gasesti oglinda magica, care te poate duce oriunde ai dori, ai mai aflat ca este inca o legenda despre excalibur, si doar 1 din 1 000 000 poate sa il scoata, el se afla mai departe pe drumul dupa casa in padurea magica, unde se afla sarpele rau ,el iti da 3 sanse sa scoti excalinbur, dar dupa a treia oara daca nu se primeste te ucide, ce alegi: \n", "alegere": ["padure", "drum"]},
    "munti": {"desc": "Tu esti in munti, poti sa mergi spre padure sau spre pestera, ce alegi: \n", "alegere": ["padure", "pestera"]},
    "fum": {"desc": "Tu esti linga fum, dar asta e simplu un focusor de sageta arsa, poti sa mergi spre padure sau spre vulcan, ce alegi: \n", "alegere": ["padure", "vulcan"]},
    "pestera": {"desc": "Tu esti in pestera, poti sa mergi spre munti sau mai adinc in pestera, ce alegi: \n", "alegere": ["munti", "adinc pestera"]},
    "adinc pestera": {"desc": "Tu esti in adincimea pesterii, poti sa mergi spre pestera sau spre temnita, ce alegi: \n", "alegere": ["pestera", "temnita"]},
    "temnita": {"desc": "Tu esti in temnita, poti sa mergi spre adinc pestera sau spre camera bossului, ce alegi: \n", "alegere": ["adinc pestera", "camera bossului"]},
    "camera bossului": {"desc": "Tu esti in camera bossului, poti sa lupti cu el sau sa fugi, ce alegi: \n", "alegere": ["lupta", "fugi"]},
    "lupta cistigata": {"desc": "Tu ai cistigat lupta cu bossul, poti merge spre comoara sau te intorci in padure, ce alegi: \n", "alegere": ["padure", "comoara"]},
    "lupta pierduta": {"desc": "Tu ai pierdut lupta cu bossul, aventura ta s-a incheiat aici. Mai incearca o data!", "alegere": []},
    "comoara": {"desc": "Tu ai gasit comoara! Felicitari, tu ai gasit oglinda magica. Ea te poate duce oriunde, dar tu trebuie sa alegi unde vrei sa mergi: \n", "alegere": ["padure", "munti", "fum", "vulcan", "palatul regelui"]},
    "fugi": {"desc": "Tu ai fugit de la boss si te ai fugit pina la padure, acum ce alegi: \n", "alegere": ["munti", "fum"]},
    "vulcan": {"desc": "Tu esti in vulcan si vezi un dracon mare care doarme, linga el sunt multe sunducuri, si oameni morti, poti sa mergi inapoi pina ce nu sa trezit, sau sa te lupti cu el, sau sa te uiti in sunducuri ce e, sau sa iai de la oameni armele, scut si bronia , ce alegi: \n", "alegere": ["lupta", "sunducuri", "arme", "fugi"]},
    "palatul regelui": {"desc": "Tu ai ajuns la palatul regelui! Felicitari, aventura ta s-a incheiat cu succes!", "alegere": []}
}


inventory = []
health = 100
armor = 0
current_location = "padurea"
InPadure = 0
dragon_died = False
sarpele_died = False
boss_died = False

while True:
    location = locations[current_location]
    print(location["desc"])

    if current_location == "camera bossului":
        if not boss_died and inventory.count("excalibur") == 1:
            action = input("Vrei sa lupti sau sa fugi? (lupta/fugi): ").strip().lower()
            if action == "lupta":
                if random.randint(1, 100) > 20:
                    print(locations["lupta cistigata"]["desc"])
                    current_location = "lupta cistigata"
                    boss_died = True
                else:
                    print(locations["lupta pierduta"]["desc"])
                    break
            elif action == "fugi":
                print(locations["fugi"]["desc"])
                current_location = "fugi"
        elif not boss_died and inventory.count("excalibur") == 0:
            action = input("Vrei sa lupti sau sa fugi? (lupta/fugi): ").strip().lower()
            if action == "lupta":
                if random.randint(1, 100) > 85:
                    print(locations["lupta cistigata"]["desc"])
                    current_location = "lupta cistigata"
                    boss_died = True
                else:
                    print(locations["lupta pierduta"]["desc"])
                    break
            elif action == "fugi":
                print(locations["fugi"]["desc"])
                current_location = "fugi"

    elif current_location == "vulcan":
        if not dragon_died and inventory.count("excalibur") == 0:
            action = input("Vrei sa te lupti cu draconul, sa te uiti in sunducuri, sa iei armele de la oameni sau sa fugi? (lupta/sunducuri/arme/fugi): ").strip().lower()
            if action == "lupta":
                if random.randint(1, 100) > 95 :
                    print("Tu ai cistigat lupta cu draconul! Felicitari!")
                    dragon_died = True
                    current_location = "palatul regelui"
                else:
                    print("Tu ai pierdut lupta cu draconul! Mai incearca o data!")
                    break
            elif action == "sunducuri":
                print("Tu ai gasit niste obiecte in sunducuri, dar nu sunt foarte utile.")
                current_location = "vulcan"
            elif action == "arme":
                print("Tu ai luat armele de la oameni, acum ai un avantaj in lupta!")
                armor += 20
                inventory.append("arme")
                current_location = "Vulcan" 
            elif action == "fugi":
                print("Tu ai fugit de la dracon si te-ai intors la padure.")
                current_location = "padurea"
        elif not dragon_died and inventory.count("excalibur") == 1:
            action = input("Vrei sa te lupti cu draconul sau sa fugi? (lupta/fugi): ").strip().lower()
            if action == "lupta":
                if random.randint(1, 100) > 25 :
                    print("Tu ai cistigat lupta cu draconul! Felicitari!")
                    dragon_died = True
                    current_location = "palatul regelui"
                else:
                    print("Tu ai pierdut lupta cu draconul! Mai incearca o data!")
                    break
            elif action == "fugi":
                print("Tu ai fugit de la dracon si te-ai intors la padure.")
                current_location = "padurea"

    elif current_location == "drum":

        if InPadure > 0 and inventory.count("excalibur") == 0 and not sarpele_died:
            print("Sarpele: Tu iarasi ai venit? Eu tiam dat sansa sa fii in viata!")
            if random.randint(1, 100) > 98:
                print("Ai cistigat sarpele, ai primit Armor din pielea lui!")
                armor += 50
                current_location = "padurea"
                sarpele_died = True
            else:
                print("Ai pierdut lupta cu sarpele! Mai incearca o data!")
                heealth = 0
                break
        elif InPadure > 0 and inventory.count("excalibur") == 1 and not sarpele_died:
            print("Sarpele: Tu iarasi ai venit? Eu tiam dat sansa sa fii in viata!")
            if random.randint(1, 100) > 10:
                print("Ai cistigat sarpele, ai primit Armor din pielea lui!")
                armor += 50
                current_location = "padurea"
                sarpele_died = True
            else:
                print("Ai pierdut lupta cu sarpele! Mai incearca o data!")
                health = 0
                break
        else:
            action = input("Vrei sa mergi spre padure, sa incerci sa scoti excalibur sau sa te intorci la padure? (padure/excalibur): ").strip().lower()
            if action == "padure":
                current_location = "padurea"
            elif action == "excalibur":
                proba = 0
                success = False
                while proba < 3 and not success and InPadure == 0 and inventory.count("excalibur") == 0:
                    if random.randint(1, 100) > 80 :
                        print("Ai reusit sa scoti excalibur! Felicitari!")
                        inventory.append("excalibur")
                        success = True
                        current_location = "padurea"
                        InPadure += 1
                    else:
                        proba += 1
                        print(f"Nu ai reusit sa scoti excalibur. Mai ai {3 - proba} incercari ramase.")
                if proba == 3 and not success and InPadure == 0 and inventory.count("excalibur") == 0:
                    print("Sarpele: Ai incercat sa scoti excalibur de 3 ori, dar nu ai reusit. Acum trebuie rasplata! ")
                    print("Te rog nu! Intelegema, eu am cazut fara sa stiu cum, te rog lasa-ma sa plec!")
                    new_action = input("Sarpele: Vrei sa te lupti cu mine sau sa fugi? (lupta/fugi): ").strip().lower()
                    if new_action == "lupta":
                        if random.choice([True, False]):
                            print("Ai reusit sa invingi sarpele! Felicitari!")
                            current_location = "padurea"
                            InPadure += 1
                        else:
                            print("Ai pierdut lupta cu sarpele! Mai incearca o data!")
                            break
                    elif new_action == "fugi":
                        print("Ai fugit de la sarpe si te-ai intors la padure.")
                        current_location = "padurea"
                        InPadure += 1
                else:
                    (print("Tu deja ai excalibur, poti sa mergi spre padure. \n"))
                    current_location = "padurea"
            else:
                print("Alegerea ta nu este valida, incearca din nou.")
    else:
        action = input(f"Ce vrei sa faci? {(location['alegere'])}: ").strip().lower()
        if action in location["alegere"]:
            current_location = action
        else:
            print("Alegerea ta nu este valida, incearca din nou.")

    if current_location == "palatul regelui":
        print(locations["palatul regelui"]["desc"])
        break

print("\nAventura ta s-a incheiat! Multumim ca ai jucat! \n")
print("Inventarul tau:", inventory)
print("Sanatatea ta ramane:", health)
# Aici se termina aventura, poti sa adaugi mai multe locatii sau actiuni daca doresti