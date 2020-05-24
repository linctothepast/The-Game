import random


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
D: What are YOU calling junk, you piece of junk?
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
