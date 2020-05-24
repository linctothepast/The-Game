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
    
