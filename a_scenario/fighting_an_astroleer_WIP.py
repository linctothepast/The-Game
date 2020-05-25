print("ASTROLEER ENCOUNTER")
print("-------------------")
import random
repeat = True
while repeat:
    sleep = input("""It's been a long day, and you decide to settle down in a nearby field, you could sleep on:
A: A soft patch of grass
B: Against a hard lonely tree
""")
    sleep = sleep.capitalize()
    if sleep == "A":
        fight = input("""You decide to sleep on a soft patch of grass for the night, as you start to doze off, you hear a loud scream in the nigher, instantly bolting you awake.
You look around to see where it was coming from, and when you turn around, you see a giant spherical being with what looks like just a mouth fly at you.
As it get's closer you see that it almost looks like it is a floating eye with a mouth! What should you do?:
A: Grab your bow and shoot an arrow at it
B: Pull out your sword to fight it
C: Run
D: Let it eat you
""")
        fight = fight.capitalize()
        if fight == "A":
            
