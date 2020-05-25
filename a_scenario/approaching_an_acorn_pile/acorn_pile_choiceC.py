import random
loop = True
rng = random.randint(1, 4)


def acorn_pile_choiceC():
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
