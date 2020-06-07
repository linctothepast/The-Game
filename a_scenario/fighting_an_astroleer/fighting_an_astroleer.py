"""
Fighting_an_astroleer

Description:
"""
import random

def fighting_an_astroleer():
    global astroleer_attack
    global your_health
    global astroleer_health
    your_health = random.randint(50, 150)
    astroleer_lvl()
    print("FIGHTING AN ASTROLEER")
    print("---------------------")
    repeat1 = True
    while repeat1:
        sleep = input("""It's been a long day, and you decide to settle down
in a nearby field, you could sleep on:
A: A soft patch of grass
B: Against a hard lonely tree
""")
        sleep = sleep.capitalize()
        if sleep == "A":
            repeat1 = False
            openfight = True
            while openfight:
                fight = input("""
You decide to sleep on a soft patch of grass for the night, as you start to
doze off, you hear a loud scream in the night, instantly bolting you awake.
You look around to see where it was coming from, and when you turn around,
you see a giant spherical being with what looks like just a mouth fly at you.
As it get's closer you see that it almost looks like it is a floating eye with
a mouth! You look up and see an entire group of astroleers, each one has a
""" + astroleer_color + """ pupil, luckily those ones don't yet see you...
What should you do?:
A: Grab your bow and shoot an arrow at it
B: Pull out your sword to fight it
C: Run
D: Let it eat you
""")
                fight = fight.capitalize()
                if fight == "A":
                    openfight = False
                    astroleer_bow_attack()
                    your_turn = True
                    fight_loop = True
                    print("""You are able to get one more
attack on the astroleer""")
                    while fight_loop:
                        if your_turn:
                            fight_input = input("""What do you want to
attack with?
A: Your sword
B: Your bow
""")
                            fight_input = fight_input.capitalize()
                            if fight_input == "A":
                                astroleer_sword_attack()
                                your_turn = False
                                input("<PAUSE>")
                                print("")
                                if astroleer_health <= 0:
                                    break
                            elif fight_input == "B":
                                astroleer_bow_attack()
                                your_turn = False
                                input("<PAUSE>")
                                print("")
                                if astroleer_health <= 0:
                                    break
                        elif not your_turn:
                            atroleer_damage()
                            astroleer_turn()
                            your_turn = True
                            input("<PAUSE>")
                            print("")
                            if your_health <= 0:
                                break

                elif fight == "B":
                    openfight = False
                    astroleer_sword_attack()
                    your_turn = True
                    fight_loop = True
                    print("""You are able to get one more
attack on the astroleer""")
                    while fight_loop:
                        if your_turn:
                            fight_input = input("""What do you want to
attack with?
A: Your sword
B: Your bow
""")
                            fight_input = fight_input.capitalize()
                            if fight_input == "A":
                                astroleer_sword_attack()
                                your_turn = False
                                input("<PAUSE>")
                                print("")
                                if astroleer_health <= 0:
                                    break
                            elif fight_input == "B":
                                astroleer_bow_attack()
                                your_turn = False
                                input("<PAUSE>")
                                print("")
                                if astroleer_health <= 0:
                                    break
                        elif not your_turn:
                            atroleer_damage()
                            astroleer_turn()
                            your_turn = True
                            input("<PAUSE>")
                            print("")
                            if your_health <= 0:
                                break

                elif fight == "C":
                    openfight = False
                    print("""You try running from the astroleer,
but theres no hope, it immeditaly catches up,
you have to fight it...""")
                    your_turn = True
                    fight_loop = True
                    while fight_loop:
                        if your_turn:
                            fight_input = input("""What do you want to
attack with?
A: Your sword
B: Your bow
""")
                            fight_input = fight_input.capitalize()
                            if fight_input == "A":
                                astroleer_sword_attack()
                                your_turn = False
                                input("<PAUSE>")
                                print("")
                                if astroleer_health <= 0:
                                    break
                            elif fight_input == "B":
                                astroleer_bow_attack()
                                your_turn = False
                                input("<PAUSE>")
                                print("")
                                if astroleer_health <= 0:
                                    break
                        elif not your_turn:
                            atroleer_damage()
                            astroleer_turn()
                            your_turn = True
                            input("<PAUSE>")
                            print("")
                            if your_health <= 0:
                                break
                elif fight == "D":
                    openfight = False

        elif sleep == "B":
            repeat1 = False
            seen = random.randint(1, 100)
            if seen >= 1:
                fight = input("""
You decide to sleep against the lone tree
in the field you are in, as you start to doze off, you hear a loud shreik
bolting you awake, you look around and see a group of astroleers in the sky,
each with there """ +astroleer_color + """ colored eyes.
You look around a bit more, and you see an astroleer in it's teeth form floating towards you.
What should you do?:
A: Grab your bow and shoot an arrow at it
B: Pull out your sword to fight it
C: Run
D: Let it eat you
""")
                fight = fight.capitalize()
                if fight == "A":
                    openfight = False
                    astroleer_bow_attack()
                    your_turn = True
                    fight_loop = True
                    print("""You are able to get one more
attack on the astroleer""")
                    while fight_loop:
                        if your_turn:
                            fight_input = input("""What do you want to
attack with?
A: Your sword
B: Your bow
""")
                            fight_input = fight_input.capitalize()
                            if fight_input == "A":
                                astroleer_sword_attack()
                                your_turn = False
                                input("<PAUSE>")
                                print("")
                                if astroleer_health <= 0:
                                    break
                            elif fight_input == "B":
                                astroleer_bow_attack()
                                your_turn = False
                                input("<PAUSE>")
                                print("")
                                if astroleer_health <= 0:
                                    break
                        elif not your_turn:
                            atroleer_damage()
                            astroleer_turn()
                            your_turn = True
                            input("<PAUSE>")
                            print("")
                            if your_health <= 0:
                                break

                elif fight == "B":
                    openfight = False
                    astroleer_sword_attack()
                    your_turn = True
                    fight_loop = True
                    print("""You are able to get one more
attack on the astroleer""")
                    while fight_loop:
                        if your_turn:
                            fight_input = input("""What do you want to
attack with?
A: Your sword
B: Your bow
""")
                            fight_input = fight_input.capitalize()
                            if fight_input == "A":
                                astroleer_sword_attack()
                                your_turn = False
                                input("<PAUSE>")
                                print("")
                                if astroleer_health <= 0:
                                    break
                            elif fight_input == "B":
                                astroleer_bow_attack()
                                your_turn = False
                                input("<PAUSE>")
                                print("")
                                if astroleer_health <= 0:
                                    break
                        elif not your_turn:
                            atroleer_damage()
                            astroleer_turn()
                            your_turn = True
                            input("<PAUSE>")
                            print("")
                            if your_health <= 0:
                                break

                elif fight == "C":
                    openfight = False
                    print("""You try running from the astroleer,
but theres no hope, it immeditaly catches up,
you have to fight it...""")
                    your_turn = True
                    fight_loop = True
                    while fight_loop:
                        if your_turn:
                            fight_input = input("""What do you want to
attack with?
A: Your sword
B: Your bow
""")
                            fight_input = fight_input.capitalize()
                            if fight_input == "A":
                                astroleer_sword_attack()
                                your_turn = False
                                input("<PAUSE>")
                                print("")
                                if astroleer_health <= 0:
                                    break
                            elif fight_input == "B":
                                astroleer_bow_attack()
                                your_turn = False
                                input("<PAUSE>")
                                print("")
                                if astroleer_health <= 0:
                                    break
                        elif not your_turn:
                            atroleer_damage()
                            astroleer_turn()
                            your_turn = True
                            input("<PAUSE>")
                            print("")
                            if your_health <= 0:
                                break
                elif fight == "D":
                    openfight = False

            else:
                print("""As you begin to fall alseep against the tree,
you see a group of astroleers in the sky, luckily they don't see you...""")

    if astroleer_health <= 0:
        print("Your last hit makes the astroleer scream in pain, and it's limp 'body' falls on the ground.")
        print("The rest of the astroleers in the sky all scream at you.")
        print("'Oh no...' you say to yourself and you start running.")
        print("You had " +str(your_health) +" health left...")
    if your_health <= 0:
        print("The astroleer bites you and you fall over... ")
        print("The astroleer had " +str(astroleer_health) +" health left...")

# The function for astroleers level and health stuff:

# Right here:
def astroleer_lvl():
    global astroleer_color
    global astroleer_health
    global astroleer_level
    astroleer_level = random.randint(10, 20)
    # Creating the astroleer_levels stuff
    if astroleer_level == 10:
        astroleer_color = "blue"
        astroleer_health = random.randint(42, 56)
    elif astroleer_level == 11:
        astroleer_color = "green"
        astroleer_health = random.randint(47, 62)
    elif astroleer_level == 12:
        astroleer_color = "yellow"
        astroleer_health = random.randint(52, 68)
    elif astroleer_level == 13:
        astroleer_color = "orange"
        astroleer_health = random.randint(57, 74)
    elif astroleer_level == 14:
        astroleer_color = "red"
        astroleer_health = random.randint(62, 80)
    elif astroleer_level == 15:
        astroleer_color = "pink"
        astroleer_health = random.randint(67, 86)
    elif astroleer_level == 16:
        astroleer_color = "purple"
        astroleer_health = random.randint(73, 93)
    elif astroleer_level == 17:
        astroleer_color = "indigo"
        astroleer_health = random.randint(79, 100)
    elif astroleer_level == 18:
        astroleer_color = "silver"
        astroleer_health = random.randint(86, 108)
    elif astroleer_level == 19:
        astroleer_color = "gold"
        astroleer_health = random.randint(93, 116)
    elif astroleer_level == 20:
        astroleer_color = "black"
        astroleer_health = random.randint(100, 124)

# Astroleer whole equation

def atroleer_damage():
    global astroleer_attack

    if astroleer_level == 10:
        crit = random.randint(1, 20)
        if crit == 20:
            astroleer_attack = random.randint(28, 34)
        else:
            astroleer_attack = random.randint(14, 17)

    elif astroleer_level == 11:
        crit = random.randint(1, 20)
        if crit == 20:
            astroleer_attack = random.randint(32, 36)
        else:
            astroleer_attack = random.randint(16, 18)

    elif astroleer_level == 12:
        crit = random.randint(1, 20)
        if crit == 20:
            astroleer_attack = random.randint(34, 38)
        else:
            astroleer_attack = random.randint(17, 19)

    elif astroleer_level == 13:
        crit = random.randint(1, 20)
        if crit == 20:
            astroleer_attack = random.randint(36, 40)
        else:
            astroleer_attack = random.randint(18, 20)

    elif astroleer_level == 14:
        crit = random.randint(1, 20)
        if crit == 20:
            astroleer_attack = random.randint(38, 42)
        else:
            astroleer_attack = random.randint(19, 21)

    elif astroleer_level == 15:
        crit = random.randint(1, 20)
        if crit == 20:
            astroleer_attack = random.randint(40, 44)
        else:
            astroleer_attack = random.randint(20, 22)

    elif astroleer_level == 16:
        crit = random.randint(1, 20)
        if crit == 20:
            astroleer_attack = random.randint(32, 36)
        else:
            astroleer_attack = random.randint(21, 23)

    elif astroleer_level == 17:
        crit = random.randint(1, 20)
        if crit == 20:
            astroleer_attack = random.randint(44, 46)
        else:
            astroleer_attack = random.randint(22, 23)

    elif astroleer_level == 18:
        crit = random.randint(1, 20)
        if crit == 20:
            astroleer_attack = random.randint(44, 48)
        else:
            astroleer_attack = random.randint(22, 24)

    elif astroleer_level == 19:
        crit = random.randint(1, 20)
        if crit == 20:
            astroleer_attack = random.randint(46, 50)
        else:
            astroleer_attack = random.randint(23, 25)


    elif astroleer_level == 20:
        teeth_of_steel = random.randint(1, 4)
        if teeth_of_steel == 1:
            print("""The astroleer roars and it's teeth turn to steel as it
uses it's teeth of steel!""")
            crit = random.randint(1, 20)
            if crit == 20:
                astroleer_attack = random.randint(72, 78)
            else:
                astroleer_attack = random.randint(36, 39)
        else:
            crit = random.randint(1, 20)
            if crit == 20:
                astroleer_attack = random.randint(48, 52)
            else:
                astroleer_attack = random.randint(24, 26)



def astroleer_bow_attack():
    global astroleer_health
    global your_turn
    print("""
You pull out your bow and grab an arrow from your quiver and,""")
    bow_rng = random.randint(1, 20)
    if bow_rng <= 12:
        print("you completely miss...")
        your_turn = False
    elif bow_rng > 12 and bow_rng <= 19:
        bow_attack = random.randint(20, 30)
        astroleer_health -= bow_attack
        attack_response = random.randint(1, 4)
        if attack_response == 1:
            print("""your arrow directly hits the astoleer and it
screams in pain, as you do """ + str(bow_attack) + """ damage!""")
        elif attack_response == 2:
            print("""your arrow hits the astroleer in the back and it
yells in pain, and you do """ + str(bow_attack) + """ damage!""")
        elif attack_response == 3:
            print("""your arrow barely hits the astroleer, but you can still
hear it scream in pain, as you do """ + str(bow_attack) + """ damage!""")
        else:
            print("""your arrow peirces through the astroleer
and it cries in pain, as you do """ + str(bow_attack) + """ damage!""")
        your_turn = False
    elif bow_rng > 19:
        bow_attack = random.randint(40, 60)
        astroleer_health -= bow_attack
        print("""your attack goes straight into the throat of the astroleers
and you get a critical hit for """ + str(bow_attack) + """ damage!""")

    your_turn = False

def astroleer_sword_attack():
    global sword_rng
    global astroleer_health
    global your_turn
    print("""
You grab your sword from it sheath and,""")
    sword_hits = random.randint(1, 3)
    if sword_hits == 1:
        print("you swing once!")
        sword_rng = random.randint(1, 20)
        if sword_rng <= 5:
            print("But completely miss...")
            print("")
            your_turn = False
        elif sword_rng > 5 and sword_rng <= 10:
            print("But you barely hit!")
            sword_attack = random.randint(5, 10)
            print("You do " + str(sword_attack) + " damage!")
            astroleer_health -= sword_attack
            print("")
        elif sword_rng > 10 and sword_rng <= 19:
            print("And you hit!")
            sword_attack = random.randint(10, 20)
            print("Doing " + str(sword_attack) + " damage!")
            astroleer_health -= sword_attack
            print("")
        elif sword_rng > 19:
            print("And you get a CRITICAL HIT!")
            sword_attack = random.randint(20, 40)
            print("That does " + str(sword_attack) + " damage!")
            print("")
    elif sword_hits == 2:
        print("and your able to swing twice!")
        sword1_rng = random.randint(1, 20)
        if sword1_rng <= 5:
            print("But you completely miss your first swing...")
            print("")
        elif sword1_rng > 5 and sword1_rng <= 10:
            print("But you barely hit your first swing!")
            sword_attack = random.randint(5, 10)
            print("You do " + str(sword_attack) + " damage!")
            print("")
            astroleer_health -= sword_attack
        elif sword1_rng > 10 and sword1_rng <= 19:
            print("And you hit your first swing!")
            sword_attack = random.randint(10, 20)
            print("Doing " + str(sword_attack) + " damage!")
            print("")
            astroleer_health -= sword_attack
        elif sword1_rng > 19:
            print("And you get a CRITICAL HIT on your FIRST swing!")
            sword_attack = random.randint(20, 40)
            print("That does " + str(sword_attack) + " damage!")
            print("")

        sword2_rng = random.randint(1, 20)
        if sword2_rng <= 5:
            print("And you completely miss your second swing...")
            print("")
        elif sword2_rng > 5 and sword2_rng <= 10:
            print("And you barely hit your second swing!")
            sword_attack = random.randint(5, 10)
            print("You do " + str(sword_attack) + " damage!")
            print("")
            astroleer_health -= sword_attack
        elif sword2_rng > 10 and sword2_rng <= 19:
            print("And you hit your second swing!")
            sword_attack = random.randint(10, 20)
            print("Doing " + str(sword_attack) + " damage!")
            print("")
            astroleer_health -= sword_attack
        elif sword2_rng > 19:
            print("And you get a CRITICAL HIT on your second swing!")
            sword_attack = random.randint(20, 40)
            print("That does " + str(sword_attack) + " damage!")
            print("")

    elif sword_hits == 3:
        print("and your able to swing three times!")
        sword1_rng = random.randint(1, 20)
        if sword1_rng <= 5:
            print("But you completely miss your first swing...")
            print("")
        elif sword1_rng > 5 and sword1_rng <= 10:
            print("But you barely hit your first swing!")
            sword_attack = random.randint(5, 10)
            print("You do " + str(sword_attack) + " damage!")
            print("")
            astroleer_health -= sword_attack
        elif sword1_rng > 10 and sword1_rng <= 19:
            print("And you hit your first swing!")
            sword_attack = random.randint(10, 20)
            print("Doing " + str(sword_attack) + " damage!")
            print("")
            astroleer_health -= sword_attack
        elif sword1_rng > 19:
            print("And you get a CRITICAL HIT on your FIRST swing!")
            sword_attack = random.randint(20, 40)
            print("That does " + str(sword_attack) + " damage!")
            print("")

        sword2_rng = random.randint(1, 20)
        if sword2_rng <= 5:
            print("And you completely miss your second swing...")
            print("")
        elif sword2_rng > 5 and sword2_rng <= 10:
            print("And you barely hit your second swing!")
            sword_attack = random.randint(5, 10)
            print("You do " + str(sword_attack) + " damage!")
            print("")
            astroleer_health -= sword_attack
        elif sword2_rng > 10 and sword2_rng <= 19:
            print("And you hit your second swing!")
            sword_attack = random.randint(10, 20)
            print("Doing " + str(sword_attack) + " damage!")
            print("")
            astroleer_health -= sword_attack
        elif sword2_rng > 19:
            print("And you get a CRITICAL HIT on your second swing!")
            sword_attack = random.randint(20, 40)
            print("That does " + str(sword_attack) + " damage!")
            print("")

        sword3_rng = random.randint(1, 20)
        if sword3_rng <= 5:
            print("And you completely miss your third swing...")
            print("")
        elif sword3_rng > 5 and sword3_rng <= 10:
            print("And you barely hit your third swing!")
            sword_attack = random.randint(5, 10)
            print("You do " + str(sword_attack) + " damage!")
            print("")
            astroleer_health -= sword_attack
        elif sword3_rng > 10 and sword3_rng <= 19:
            print("And you hit your third swing!")
            sword_attack = random.randint(10, 20)
            print("Doing " + str(sword_attack) + " damage!")
            print("")
            astroleer_health -= sword_attack
        elif sword3_rng > 19:
            print("And you get a CRITICAL HIT on your third swing!")
            sword_attack = random.randint(20, 40)
            print("That does " + str(sword_attack) + " damage!")
            print("")

        your_turn = False


def astroleer_turn():
    global your_turn
    global your_health
    global astroleer_attack

    print("The astroleer flies towards you,")
    astroleer_hit = random.randint(1,20)
    if astroleer_hit < 5:
        astroleer_dodge_response = random.randint(1, 4)
        if astroleer_dodge_response == 1:
            print("and you dodge it's teeth.")
            print("")
        elif astroleer_dodge_response == 2:
            print("and the astroleer just misses!")
        elif astroleer_dodge_response ==  3:
            print("and you jump over the astroleer!")
            print("")
        elif astroleer_dodge_response == 4:
            print("and the astroleer bites to early!")
            print("")

    elif astroleer_hit >= 5:

        astroleer_hit_response = random.randint(1, 4)
        if astroleer_hit_response == 1:
            print("and bites you on the arm, dealing " + str(astroleer_attack) + " damage!")
            print("")
            your_health -= astroleer_attack
        elif astroleer_hit_response == 2:
            print("and bites your foot, dealing " + str(astroleer_attack) + " damage!")
            print("")
            your_health -= astroleer_attack
        elif astroleer_hit_response == 3:
            print("and bites your ear, dealing " + str(astroleer_attack) + " damage!")
            print("")
            your_health -= astroleer_attack
        elif astroleer_hit_response == 4:
            print("and bites you on the chest, dealing " + str(astroleer_attack) + " damage!")
            print("")
            your_health -= astroleer_attack
    your_turn = True
fighting_an_astroleer()
