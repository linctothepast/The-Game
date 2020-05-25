def approaching_acorn_pile():
    import acorn_pile_choiceA
    import acorn_pile_choiceB
    import acorn_pile_choiceC
    import acorn_pile_choiceD
    import acorn_pile_choiceE
    import acorn_pile_choiceF
    import acorn_pile_choiceG
    import acorn_pile_choiceH
    import acorn_pile_choiceI
    import acorn_pile_choiceJ
    print("APROACHING AN ACORN PILE")
    print("---------------------------")
    loop = True
    while loop:
        choice = input("""You're walking through the Forest of Kloa,
and you come across a small pile of acorns (they seem to be twitching).
How should you approach this?:
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
            acorn_pile_choiceA.acorn_pile_choiceA()
            loop = False

        elif choice == "B":
            acorn_pile_choiceB.acorn_pile_choiceB()
            loop = False

        elif choice == "C":
            acorn_pile_choiceC.acorn_pile_choiceC()
            loop = False

        elif choice == "D":
            acorn_pile_choiceD.acorn_pile_choiceD()
            loop = False

        elif choice == "E":
            acorn_pile_choiceE.acorn_pile_choiceE()
            loop = False

        elif choice == "F":
            acorn_pile_choiceF.acorn_pile_choiceF()
            loop = False

        elif choice == "G":
            acorn_pile_choiceG.acorn_pile_choiceG()
            loop = False

        elif choice == "H":
            acorn_pile_choiceH.acorn_pile_choiceH()
            loop = False

        elif choice == "I":
            acorn_pile_choiceI.acorn_pile_choiceI()
            loop = False

        elif choice == "J":
            acorn_pile_choiceJ.acorn_pile_choiceJ()
            loop = False

    print("")
    print("SCENARIO ENDED")


approaching_acorn_pile()
