import random

input("~The Game~")



print("")
infinity = True
while infinity:
    in1 = input("""What would you like to do?
1: View Scenarios
2: View Art
""")
    if in1 == "1":
        infinity = False
        print("")
        fish = True
        while fish:
            in2 = input("Which scenario do you want to view?: ")
            if in2 == "talk_loki":
                fish = False
                print("")
                print("")


                print("Talking to Loki!")
                print("----------------")
                intro_num = random.randint(1,150)
                wloop = False
                if intro_num == 1:

                    while not wloop:
                        response = input("""Have any good food? I'm starving!
A: Here I have some rations I could spare.
B: No, I don't have any food I couls spare you, sorry...
C: No, but we can still trade!
D: I would never give food to dirt like you!
                """)
                        response = response.capitalize()
                        if response == "A":
                            wloop = True
                            wloop2 = False
                            while not wloop2:
                                response = input("Ahh yes, thank you! (He says as you give him some of your rations) Now to buisness, would you like to trade?: ")
                                if response == "yes":
                                    wloop2 = True
                                    print("Ahh yes, come see my wares! (You and Loki go do some trading!)")

                                if response == "no":
                                    wloop2 = True
                                    print("Okay, we can trade later! (Loki looks at you suspiciously with a grin)")

                        elif response == "B":
                            wloop = True
                            wloop2 = False
                            while not wloop2:
                                response = input("Ahh okay, that is fine (he says with a sigh), but anyways, would you like to trade?: ")
                                if response == "yes":
                                    wloop2 = True
                                    print("Ahh yes, come see my wares! (You and Loki go do some trading!)")
                                if response == "no":
                                    wloop2 = True
                                    print("Okay, we can trade later! (Loki looks at you suspiciously with a grin)")
                        elif response == "C":
                            wloop = True
                            print("Yes why of course! Come on over here, so I can show you my wares (he says suspiciously)")
                        elif response == "D":
                            wloop = True
                            print("(You see Loki's eyebrows wrinkle, as he pulls a dagger from his jacket, and you engage in combat)")
                elif intro_num > 1 and intro_num <= 50:
                    wloop = False
                    while not wloop:
                        response = input("""Great items, great prices!
A: Here, can I have a look at your wares?
B: Thank you, but I can't trade right now!
C: I can't trade, but we can still talk.
D: I would never trade with dirt like you!
                """)
                        response = response.capitalize()
                        if response == "A":
                            wloop = True
                            print("Ahh yes, come see my wares! (You and Loki go do some trading!)")
                        elif response == "B":
                            wloop = True
                            print("Ahh, okay, that is fine... I guess (he whispered). (As you walk away, Loki looks at you suspiciously with a grin)")
                        elif response == "C":
                            wloop = True
                            print("Ahh, okay, but sadly I do not have enough time to talk. (As you walk away, Loki looks at you suspiciously with a grin)")
                        elif response == "D":
                            wloop = True
                            print("(You see Loki's eyebrows wrinkle, as he pulls a dagger from his jacket, and you engage in combat)")
                elif intro_num > 50 and intro_num <= 100:
                    wloop = False
                    while not wloop:
                        response = input("""Have you heard of any treasures nearby? I'm running low...
A: Yeah, I heard of a dragon's hoard down south.
B: No, not recently.
C: No, but why do you need treasure?
D: I am NOT telling you where MY treasure is!
                """)
                        response = response.capitalize()
                        if response == "A":
                            wloop = True
                            wloop2 = False
                            while not wloop2:
                                response = input("Ahh, I think that I actually have an okay stock of treasure (he says fearfully), hey do you wanna do some trading?: ")
                                if response == "yes":
                                    wloop2 = True
                                    print("Ahh yes, come see my wares! (You and Loki go do some trading!)")

                                if response == "no":
                                    wloop2 = True
                                    print("Okay, we can trade later! (Loki looks at you suspiciously with a grin)")
                        elif response == "B":
                            wloop = True
                            wloop2 = False
                            while not wloop2:
                                response = input("Oh, that's okay... Hey wanna do some trading? (He says with a grin): ")
                                if response == "yes":
                                    wloop2 = True
                                    print("Ahh yes, come see my wares! (You and Loki go do some trading!)")

                                if response == "no":
                                    wloop2 = True
                                    print("Okay, we can trade later! (Loki looks at you suspiciously with a grin)")
                        elif response == "C":
                            wloop = True
                            wloop2 = False
                            while not wloop2:
                                response = input("Ahh, yes, because I am LOKI THE MERCHANT (He yells), now let's trade!: ")
                                if response == "yes":
                                    wloop2 = True
                                    print("Ahh yes, come see my wares! (You and Loki go do some trading!)")

                                if response == "no":
                                    wloop2 = True
                                    print("Okay, we can trade later! (Loki looks at you suspiciously with a grin)")
                        elif response == "D":
                            wloop = True
                            print("Well in that case,(You see Loki's eyebrows wrinkle, as he pulls a dagger from his jacket, and you engage in combat)")
                elif intro_num > 100 and intro_num <= 150:
                    wloop = False
                    while not wloop:
                        response = input("""You have a lot of junk on you! Do you want me to lighten your load? I have very reasonable prices!
A: Yes please! I've been looking for a merchant to help me get rid of stuff!
B: No, no, I'm good, but thank you!
C: I would, but I don't have time!
D: What are YOU calling junk?
                """)
                        response = response.capitalize()
                        if response == "A":
                            wloop = True
                            print("(You and Loki go to do some trading)")
                        elif response == "B":
                            wloop = True
                            print("Okay, we can trade later! (Loki looks at you suspiciously with a grin)")
                        elif response == "C":
                            wloop = True
                            print("Okay, we can trade later! (Loki looks at you suspiciously with a grin)")
                        elif response == "D":
                            wloop = True
                            print("Well in that case,(You see Loki's eyebrows wrinkle, as he pulls a dagger from his jacket, and you engage in combat)")
                print("")
                print("")
                infinity = True






            elif in2 == "approaching_acorn":
                fish = False
                print("")
                print("")
                print("APROACHING AN ACORN PILE")
                print("---------------------------")
                import random
                rng = random.randint(1, 4)
                acorn = True
                while acorn:
                    choice = input("""You're walking through the Forest of Kloa, and you come across a small pile of acorns (they seem to be twitching). How should you approach this?
A: Shout at the pile of acorns, 'Is anyone there?'
B: Say quietly to the pile of acorns, 'Is anyone there?'
C: Poke the pile of acorns with your finger
D: Poke the acorn pile with a stick
E: Ask the pile 'Are you an acorn sprite?'
F: Throw a rock at the acorns
G: Tickle the acorn pile with a stick
H: Chop an acorn in half
I: Step on an acorn
J: Ignore the acorn pile
""")
                    choice = choice.capitalize()
                    if choice == "A":
                        acorn = False
                        print("(You hear a shreik from the acorn pile as an angry acorn monster rises from the pile, and you initiate combat)")
                    elif choice == "B":
                        acorn = False
                        print("(You hear a loud growl from the acorn pile as an angry acorn monster rises from the pile, and you initiate combat)")
                    elif choice == "C":
                        acorn = False
                        if rng == 1:
                            print("(While walking over to poke the acorn with your finger, you accidently step on an acorn, then you hear a loud shreik from the acorn pile as an angry acorn monster rises from the pile, and you initiate combat)")
                        else:
                            print("(You poke the acorn pile with your finger, and you hear a loud squeak from the acorn pile, and a passive acorn rises looking angry, then tranforms into a hostile acorn monster and you initiate combat)")
                    elif choice == "D":
                        acorn = False
                        if rng == 1:
                            print("(While walking over to poke the acorn with a stick, you accidently step on an acorn, then you hear a loud shreik from the acorn pile as an angry acorn monster rises from the pile, and you initiate combat)")
                        else:
                            print("(You poke the acorn pile with a stick, and you hear a quiet squeak from the acorn pile, and a passive acorn rises looking angry, then tranforms into a hostile acorn monster and you initiate combat)")
                    elif choice == "E":
                        acorn = False
                        print("(You hear an angry sqeaky voice say 'yes', and you initiate combat)")
                    elif choice == "F":
                        acorn = False
                        print("(You hear a loud growl from the acorn pile as an angry acorn monster rises from the pile, and you initiate combat)")
                    elif choice == "G":
                        acorn = False
                        print("(You go over and tickle the acorn pile with a stick, and you hear a little giggle from the acorn pile. An adorable passive acorn rises from the pile and says 'You must be an ally, you figured out how to approach us carefully!)")
                        rng = random.randint(1, 100)
                        if rng == 1:
                            print("(The acorn offers you a pile of acorns, and in it, you see a shiny blue acorn!) This is a blue acorn it shows that you are trustorthy, show it to any member of my kind and they will instantly trust you!")
                        else:
                            print("(The acorn offers you a small pile of acorns!)")
                    elif choice == "H":
                        acorn = False
                        print("(You decide to chop an acorn in half, and before you even shop the acorn, you hear a shreik from the acorn pile as an angry acorn monster rises from the pile, and you initiate combat)")
                    elif choice == "I":
                        acorn = False
                        print("You step on an acorn, and you hear a loud shreik from the acorn pile as an angry acorn monster rises from the pile, and you initiate combat)")
                    elif choice == "J":
                        acorn = False
                        print("(You ignore the acorn pile and go on your way)")
                print("SCENARIO ENDED")
                print("")
                print("")
                infinity = True


            elif in2 == "wood_pixie_encounter":
                fish = False
                print("")
                print("")
                print("WOOD PIXIE ENCOUNTER")
                print("--------------------")
                blueacorn=input("Do you have a blue acorn? y/n?: ")
                if blueacorn=="y":
                    sleep=input("""You are walking through the forest, having received a blue acorn and becoming allies with the species of Acorn Sprites.
You feel drowsy and decide to lay down and take a nap. Where should you rest?
A: On the grass
B: Against a tree
""")
                    sleep=sleep.capitalize()
                    if sleep=="A":
                        print("You fall asleep peacefully. You wake up an hour later and continue your journey.")
                    elif sleep=="B":
                        print("""You lean against a tree and chip off a piece of bark accidentally. A nearby Wood Pixie notices and yells, startling you.
You stand up, accidentally snapping a branch off the tree. The Wood Pixie screams and says something in a different language.
More Wood Pixies begin swarming around and then scream, in your language, 'ATTACK!'. You engage in combat.
""")
                elif blueacorn=="n":
                    fight=input("Did you just fight an Acorn Sprite? y/n?: ")
                    if fight=="y":
                        sleep=input("""You are walking through the forest, exhausted from your fight with the Acorn Sprite. You decide to take a nap. Where should you rest?
A: On the grass
B: Against a tree
""")
                        sleep=sleep.capitalize()
                        if sleep=="A":
                            print("You fall asleep peacefully. You wake up an hour later and continue your journey.")
                        elif sleep=="B":
                            print("""You lean against a tree and chip off a piece of bark accidentally. A nearby Wood Pixie notices and yells, startling you.
You stand up, accidentally snapping a branch off the tree. The Wood Pixie screams and says something in a different language.
More Wood Pixies begin swarming around and then scream, in your language, 'ATTACK!'. You engage in combat.
""")
                    elif fight=="n":
                        sleep=input("""You are walking through the forest, and you feel a sudden drowsyness. You decide to take a nap. Where should you rest?
A: On the grass
B: Against a tree
""")
                        sleep=sleep.capitalize()
                        if sleep=="A":
                            print("You fall asleep peacefully. You wake up an hour later and continue your journey.")
                        elif sleep=="B":
                            print("""You lean against a tree and chip off a piece of bark accidentally. A nearby Wood Pixie notices and yells, startling you.
You stand up, accidentally snapping a branch off the tree. The Wood Pixie screams and says something in a different language.
More Wood Pixies begin swarming around and then scream, in your language, 'ATTACK!'. You engage in combat.
""")

























        if in1 == "2":
            infinity = False
            in2 = input("What art do you want to see?: ")
            if in2 == "loki":
                print("oof")
