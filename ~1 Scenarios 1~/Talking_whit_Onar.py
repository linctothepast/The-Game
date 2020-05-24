print("TALKING WITH ONAR")
print("-----------------")
import random
question = random.randint(1,1)
if question == 1:
    repeat1 = True
    while repeat1:
        question1 = input("""Welcome to my home! Come inside, I think I have something you deserve, young lad.
A: Who are you?
B: Okay!
C: How do I know I can trust you?
D: I would never take trash from dirt like you.
""")
        question1 = question1.capitalize()
        if question1 == "A":
            repeat1 = False
            repeat2 = True
            while repeat2:
                question2 = input("""I am a paladin! Well at least a retired one... But that is not important... (he looks like he is remembering his past life)
Well anyways, enough about me, you seem like a good person so here I think you should have some money! (He hands you some money):
A: Where did you get this?
B: Thank you so much!
C: What's the catch?
D: Wow you really are an old fool!
""")
                question2 = question2.capitalize()
                if question2 == "A":
                    repeat2 = False
                    repeat3 = True
                    while repeat3:
                        question3 = input("""Well I suppose I could tell you a little story... I believe it was 12 years ago, me and a group of friends set out on a journey, it was small, but it was a journey.
Our journey was to defeat Salnosh The Terrible!:
A: Who was Salnosh The Terrible?
B: Who were your friends?
C: (Let him continue)
""")
                        question3 = question3.capitalize()
                        if question3 == "A":
                            repeat3 = False
                            repeat4 = True
                            while repeat4:
                                question4 = input("""Who is Salnosh The Terrible you ask? Well lad, he was none other than the most terrible ogre to ever exist! It took us two years, but we had finally made it to him after our long journey, and it was time for the battle!
A: Who were your friends?
B: (Let him continue)
""")
                                question4 = question4.capitalize()
                                if question4 == "A":
                                    repeat4 = False
                                    repeat5 = True
                                    while repeat5:
                                        question5 = input("""Well, let's see, I believe we were a party of 10, there was me, my best friend Aryl son of Faryl of the arctic dwarves, Elwin heir to the light elf kingdom, Spelf from the dark elves
Selia of the sea elves, Felafas of the wood elves, an amazing halfling named Melo, Shmelsh son of Felsh of the hill dwarves, Glingo son Bringo of the mountain dwarves, and finally a hill titan name Relfiah!
The battle against Salnosh lasted for a total of 6 days before it finally ended, but sadly, Elwin and Felsh didn't survive the battle (he says sadly).
After the battle we were able to each split 1/10 of Salnoshes Hoard of treasure (the extra 2/10 went towards the light elves and hill dwarves)!
Well that's all, I just thought you look like you should have some money!:
A: Well, thank you so much!
B: What a fool...
""")
                                        question5 = question5.capitalize()
                                        if question5 == "A":
                                            repeat5 = False
                                            print("No no! It's nothing! (He says, as he opens the nearby door for you to leave)")
                                        elif question5 == "B":
                                            repeat5 = False
                                            print("(His smile immediatly turns to a frown as you pull out your weapon, and he runs into a nearby room to get his weapon and you engage in comabt)")
                                elif question4 == "B":
                                        repeat4 = False
                                        repeat5 = True
                                        while repeat5:
                                            question5 = input("""The battle against Salnosh lasted for a total of 6 days before it finally ended, but sadly, Elwin and Felsh didn't survive the battle (he says sadly).
After the battle we were able to each split 1/10 of Salnoshes Hoard of treasure (the extra 2/10 went towards the light elves and hill dwarves)!
Well that's all, I just thought you look like you should have some money!:
A: Well, thank you so much!
B: What a fool...
""")
                                            question5 = question5.capitalize()
                                            if question5 == "A":
                                                repeat5 = False
                                                print("No no! It's nothing! (He says, as he opens the nearby door for you to leave)")
                                            elif question5 == "B":
                                                repeat5 = False
                                                print("(His smile immediatly turns to a frown as you pull out your weapon, and he runs into a nearby room to get his weapon and you engage in comabt)")
                        elif question3 == "B":
                            repeat3 = False
                            repeat4 = True
                            while repeat4:
                                question4 = input("""Well, let's see, I believe we were a party of 10, there was me, my best friend Aryl son of Faryl of the arctic dwarves, Elwin heir to the light elf kingdom, Spelf from the dark elves
Selia of the sea elves, Felafas of the wood elves, an amazing halfling named Melo, Shmelsh son of Felsh of the hill dwarves, Glingo son Bringo of the mountain dwarves, and finally a hill titan name Relfiah!
It took us two years, but we had finally made it to him after our long journey, and it was time for the battle!
A: Who was Salnosh The terrible?
B: (Let him continue)
""")
                                question4 = question4.capitalize()
                                if question4 == "A":
                                    repeat4 = False
                                    repeat5 = True
                                    while repeat5:
                                        question5 = input("""Who is Salnosh The Terrible you ask? Well lad, he was none other than the most terrible ogre to ever exist!
After the battle we were able to each split 1/10 of Salnoshes Hoard of treasure (the extra 2/10 went towards the light elves and hill dwarves)!
Well that's all, I just thought you look like you should have some money!:
A: Well, thank you so much!
B: What a fool...
""")
                                        question5 = question5.capitalize()
                                        if question5 == "A":
                                            repeat5 = False
                                            print("No no! It's nothing! (He says, as he opens the nearby door for you to leave)")
                                        elif question5 == "B":
                                            repeat5 = False
                                            print("(His smile immediatly turns to a frown as you pull out your weapon, and he runs into a nearby room to get his weapon and you engage in comabt)")


                                elif question4 == "B":
                                        repeat4 = False
                                        repeat5 = True
                                        while repeat5:
                                            question5 = input("""The battle against Salnosh lasted for a total of 6 days before it finally ended, but sadly, Elwin and Felsh didn't survive the battle (he says sadly).
After the battle we were able to each split 1/10 of Salnoshes Hoard of treasure (the extra 2/10 went towards the light elves and hill dwarves)!
Well that's all, I just thought you look like you should have some money!:
A: Well, thank you so much!
B: What a fool...
""")
                                            question5 = question5.capitalize()
                                            if question5 == "A":
                                                repeat5 = False
                                                print("No no! It's nothing! (He says, as he opens the nearby door for you to leave)")
                                            elif question5 == "B":
                                                repeat5 = False
                                                print("(His smile immediatly turns to a frown as you pull out your weapon, and he runs into a nearby room to get his weapon and you engage in comabt)")

                        elif question3 == "C":
                            repeat3 = False
                            repeat4 = True
                            while repeat4:
                                question4 = input("""It took us two years, but we had finally made it to him after our long journey, and it was time for the battle!
The battle against Salnosh lasted for a total of 6 days before it finally ended, but sadly, Elwin and Felsh didn't survive the battle (he says sadly).
After the battle we were able to each split 1/10 of Salnoshes Hoard of treasure (the extra 2/10 went towards the light elves and hill dwarves)!
Well that's all, I just thought you look like you should have some money!:
A: Well, thank you so much!
B: What a fool...
""")
                                question4 = question4.capitalize()
                                if question4 == "A":
                                    repeat4 = False
                                    print("No no! It's nothing! (He says, as he opens the nearby door for you to leave)")
                                elif question4 == "B":
                                    repeat4 = False
                                    print("(His smile immediatly turns to a frown as you pull out your weapon, and he runs into a nearby room to get his weapon and you engage in comabt)")

                elif question2 == "B":
                    repeat2 = False
                    repeat3 = True
                    while repeat3:
                        question3 = input("""Hey, your welcome, now come in! Come in! Let me tell you a little story!
A: Sure, why not!
B: I don't have time I'm sorry!
""")
                        question3 = question3.capitalize()
                        if question3 == "A":
                            repeat3 = False
                            repeat4 = True
                            while repeat4:
                                question4 = input("""I believe it was 12 years ago, me and a group of friends set out on a journey, it was small, but it was a journey.
Our journey was to defeat Salnosh The Terrible!:
A: Who was Salnosh The Terrible?
B: Who were your friends?
C: (Let him continue)
""")
                                question4 = question4.capitalize()
                                if question4 == "A":
                                    repeat4 = False
                                    repeat5 = True
                                    while repeat5:
                                        question5 = input("""Who is Salnosh The Terrible you ask? Well lad, he was none other than the most terrible ogre to ever exist! It took us two years, but we had finally made it to him after our long journey, and it was time for the battle!
A: Who were your friends?
B: (Let him continue)
""")
                                        question5 = question5.capitalize()
                                        if question5 == "A":
                                            repeat5 = False
                                            repeat6 = True
                                            while repeat6:
                                                question6 = input("""Well, let's see, I believe we were a party of 10, there was me, my best friend Aryl son of Faryl of the arctic dwarves, Elwin heir to the light elf kingdom, Spelf from the dark elves
Selia of the sea elves, Felafas of the wood elves, an amazing halfling named Melo, Shmelsh son of Felsh of the hill dwarves, Glingo son Bringo of the mountain dwarves, and finally a hill titan name Relfiah!
The battle against Salnosh lasted for a total of 6 days before it finally ended, but sadly, Elwin and Felsh didn't survive the battle (he says sadly).
After the battle we were able to each split 1/10 of Salnoshes Hoard of treasure (the extra 2/10 went towards the light elves and hill dwarves)!
Well that's all, I just thought you look like you should have some money!:
A: Well, thank you so much!
B: What a fool...
""")
                                                question6 = question6.capitalize()
                                                if question6 == "A":
                                                    repeat6 = False
                                                    print("No no! It's nothing! (He says, as he opens the nearby door for you to leave)")
                                                elif question6 == "B":
                                                    repeat6 = False
                                                    print("(His smile immediatly turns to a frown as you pull out your weapon, and he runs into a nearby room to get his weapon and you engage in comabt)")
                                        elif question5 == "B":
                                                repeat5 = False
                                                repeat6 = True
                                                while repeat6:
                                                    question5 = input("""The battle against Salnosh lasted for a total of 6 days before it finally ended, but sadly, Elwin and Felsh didn't survive the battle (he says sadly).
After the battle we were able to each split 1/10 of Salnoshes Hoard of treasure (the extra 2/10 went towards the light elves and hill dwarves)!
Well that's all, I just thought you look like you should have some money!:
A: Well, thank you so much!
B: What a fool...
""")
                                                    question6 = question5.capitalize()
                                                    if question6 == "A":
                                                        repeat6 = False
                                                        print("No no! It's nothing! (He says, as he opens the nearby door for you to leave)")
                                                    elif question6 == "B":
                                                        repeat6 = False
                                                        print("(His smile immediatly turns to a frown as you pull out your weapon, and he runs into a nearby room to get his weapon and you engage in comabt)")
                                elif question4 == "B":
                                    repeat4 = False
                                    repeat5 = True
                                    while repeat5:
                                        question5 = input("""Well, let's see, I believe we were a party of 10, there was me, my best friend Aryl son of Faryl of the arctic dwarves, Elwin heir to the light elf kingdom, Spelf from the dark elves
Selia of the sea elves, Felafas of the wood elves, an amazing halfling named Melo, Shmelsh son of Felsh of the hill dwarves, Glingo son Bringo of the mountain dwarves, and finally a hill titan name Relfiah!
It took us two years, but we had finally made it to him after our long journey, and it was time for the battle!
A: Who was Salnosh The terrible?
B: (Let him continue)
""")
                                        question5 = question4.capitalize()
                                        if question5 == "A":
                                            repeat5 = False
                                            repeat6 = True
                                            while repeat6:
                                                question6 = input("""Who is Salnosh The Terrible you ask? Well lad, he was none other than the most terrible ogre to ever exist!
After the battle we were able to each split 1/10 of Salnoshes Hoard of treasure (the extra 2/10 went towards the light elves and hill dwarves)!
Well that's all, I just thought you look like you should have some money!:
A: Well, thank you so much!
B: What a fool...
""")
                                                question6 = question5.capitalize()
                                                if question6 == "A":
                                                    repeat6 = False
                                                    print("No no! It's nothing! (He says, as he opens the nearby door for you to leave)")
                                                elif question6 == "B":
                                                    repeat6 = False
                                                    print("(His smile immediatly turns to a frown as you pull out your weapon, and he runs into a nearby room to get his weapon and you engage in comabt)")


                                        elif question5 == "B":
                                                repeat5 = False
                                                repeat6 = True
                                                while repeat6:
                                                    question6 = input("""The battle against Salnosh lasted for a total of 6 days before it finally ended, but sadly, Elwin and Felsh didn't survive the battle (he says sadly).
After the battle we were able to each split 1/10 of Salnoshes Hoard of treasure (the extra 2/10 went towards the light elves and hill dwarves)!
Well that's all, I just thought you look like you should have some money!:
A: Well, thank you so much!
B: What a fool...
""")
                                                    question6 = question5.capitalize()
                                                    if question6 == "A":
                                                        repeat6 = False
                                                        print("No no! It's nothing! (He says, as he opens the nearby door for you to leave)")
                                                    elif question6 == "B":
                                                        repeat6 = False
                                                        print("(His smile immediatly turns to a frown as you pull out your weapon, and he runs into a nearby room to get his weapon and you engage in comabt)")

                                elif question4 == "C":
                                    repeat4 = False
                                    repeat5 = True
                                    while repeat5:
                                        question5 = input("""It took us two years, but we had finally made it to him after our long journey, and it was time for the battle!
The battle against Salnosh lasted for a total of 6 days before it finally ended, but sadly, Elwin and Felsh didn't survive the battle (he says sadly).
After the battle we were able to each split 1/10 of Salnoshes Hoard of treasure (the extra 2/10 went towards the light elves and hill dwarves)!
Well that's all, I just thought you look like you should have some money!:
A: Well, thank you so much!
B: What a fool...
""")
                                        question5 = question5.capitalize()
                                        if question5 == "A":
                                            repeat5 = False
                                            print("No no! It's nothing! (He says, as he opens the nearby door for you to leave)")
                                        elif question5 == "B":
                                            repeat5 = False
                                            print("(His smile immediatly turns to a frown as you pull out your weapon, and he runs into a nearby room to get his weapon and you engage in comabt)")
                        elif question3 == "B":
                            repeat3 = False
                            print("Oh okay, well then goodbye! (He waves you off as you continue on your journey)")
                elif question2 == "C":
                    repeat2 = False
                    repeat3 = True
                    while repeat3:
