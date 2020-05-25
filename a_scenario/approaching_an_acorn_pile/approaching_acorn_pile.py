import random

# Function for the actual thing.


def approaching_acorn_pile():
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
            acorn_pile_choice_a()
            loop = False

        elif choice == "B":
            acorn_pile_choice_b()
            loop = False

        elif choice == "C":
            acorn_pile_choice_c()
            loop = False

        elif choice == "D":
            acorn_pile_choice_d()
            loop = False

        elif choice == "E":
            acorn_pile_choice_e()
            loop = False

        elif choice == "F":
            acorn_pile_choice_f()
            loop = False

        elif choice == "G":
            acorn_pile_choice_g()
            loop = False

        elif choice == "H":
            acorn_pile_choice_h()
            loop = False

        elif choice == "I":
            acorn_pile_choice_i()
            loop = False

        elif choice == "J":
            acorn_pile_choice_j()
            loop = False

    print("")
    print("SCENARIO ENDED")

# Function for choice A:


def acorn_pile_choice_a():
    loop = False
    print("""(You hear a shreik from the acorn pile as an angry acorn
monster rises from the pile, and you initiate combat)""")
    if loop:
        print("")


# Function for choice B:


def acorn_pile_choice_b():
    loop = False
    print("""(You hear a loud growl from the acorn pile as
an angry acorn monster rises from the pile, and you initiate combat)""")
    if loop:
        print("")


# Function for choice C:


def acorn_pile_choice_c():
    rng = random.randint(1, 4)
    loop = False
    if rng == 1:
        print("""(While walking over to poke the acorn with your finger,
you  accidently step on an acorn, then you hear a loud shreik from the acorn
pile as an angry acorn monster rises from the pile,
and you initiate combat)""")
    else:
        print("""(You poke the acorn pile with your finger,
and you hear a loud squeak from the acorn pile, and a passive acorn rises
looking angry, then tranforms into a hostile acorn monster
and you initiate in combat)""")
    if loop:
        print("")


# Function for choice D:


def acorn_pile_choice_d():
    rng = random.randint(1, 4)
    loop = False
    if rng == 1:
        print("""(While walking over to poke the acorn with a stick,
you accidently step on an acorn, then you hear a loud shreik from the acorn
pile as an angry acorn monster rises from the pile,
and you initiate combat)""")
    else:
        print("""(You poke the acorn pile with a stick, and you hear a
quiet squeak from the acorn pile, and a passive acorn rises looking angry,
then tranforms into a hostile acorn monster and you initiate combat)""")
    if loop:
        print("")


# Function for choice E:


def acorn_pile_choice_e():
    loop = False
    print("""(You hear an angry sqeaky voice say 'yes',
and you initiate combat)""")
    if loop:
        print("")


# Function for choice F:


def acorn_pile_choice_f():
    loop = False
    print("""(You hear a loud growl from the acorn pile as an angry acorn
monster rises from the pile, and you initiate combat)""")
    if loop:
        print("")


# Function for choice G:


def acorn_pile_choice_g():
    loop = False
    print("""(You go over and tickle the acorn pile with a stick,
and you hear a little giggle from the acorn pile. An adorable passive acorn
rises from the pile and says, 'You must be an ally,
you figured out how to approach us carefully!)""")
    rng = random.randint(1, 100)
    if rng == 1:
        print("""(The acorn offers you a pile of acorns, and in it,
you see a shiny blue acorn!) This is a blue acorn it shows that you are
trustorthy, show it to any member of my kind
and they will instantly trust you!""")
        blueacorn = True
        if not blueacorn:
            print("")
    else:
        print("(The acorn offers you a small pile of acorns!)")
    if loop:
        print("")


# Function for choice H:


def acorn_pile_choice_h():
    loop = False
    print("""(You decide to chop an acorn in half, and before
you even shop the acorn,
you hear a shreik from the acorn pile as an angry acorn monster rises
from the pile, and you initiate combat)""")
    if loop:
        print("")


# Function for choice I:


def acorn_pile_choice_i():
    loop = False
    print("""You step on an acorn, and you hear a loud shreik from the
acorn pile as an angry acorn monster rises from the pile,
and you initiate combat)""")
    if loop:
        print("")


# Function for choice J:


def acorn_pile_choice_j():
    loop = False
    print("(You ignore the acorn pile and go on your way)")
    if loop:
        print("")

# Playing the actual thing


approaching_acorn_pile()
