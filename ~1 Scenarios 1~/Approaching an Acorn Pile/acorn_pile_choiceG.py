import random
loop = True


def acorn_pile_choiceG():
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
    else:
        print("(The acorn offers you a small pile of acorns!)")
    if loop:
        print("")
