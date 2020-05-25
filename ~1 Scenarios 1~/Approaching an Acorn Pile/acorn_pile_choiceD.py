import random
loop = True
rng = random.randint(1, 4)


def acorn_pile_choiceD():
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
