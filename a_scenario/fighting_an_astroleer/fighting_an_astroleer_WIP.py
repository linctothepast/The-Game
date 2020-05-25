import random
level = random.randint(10, 20)
# Creating the levels stuff
if level == 10:
    astroleer_color = "blue"
    astroleer_health = random.randint(42, 56)

elif level == 11:
    astroleer_color = "green"
    astroleer_health = random.randint(47, 62)

elif level == 12:
    astroleer_color = "yellow"
    astroleer_health = random.randint(52, 68)

elif level == 13:
    astroleer_color = "orange"

elif level == 14:
    astroleer_color = "red"

elif level == 15:
    astroleer_color = "pink"

elif level == 16:
    astroleer_color = "purple"

elif level == 17:
    astroleer_color = "indigo"

elif level == 18:
    astroleer_color = "black"

elif level == 19:
    astroleer_color = "silver"

elif level == 20:
    astroleer_color = "gold"

# Done

print("FIGHTING AN ASTROLEER")
print("---------------------")
repeat = True
while repeat:
    sleep = input("""It's been a long day, and you decide to settle down
in a nearby field, you could sleep on:
A: A soft patch of grass
B: Against a hard lonely tree
""")
    sleep = sleep.capitalize()
    if sleep == "A":
        fight = input("""You decide to sleep on a soft patch of grass for the
night, as you start to doze off, you hear a loud scream in the night,
instantly bolting you awake. You look around to see where it was coming from,
and when you turn around, you see a giant spherical being with what looks like
just a mouth fly at you. As it get's closer you see that it almost looks like
it is a floating eye with a mouth! You look up and see What should you do?:
A: Grab your bow and shoot an arrow at it
B: Pull out your sword to fight it
C: Run
D: Let it eat you
""")
        fight = fight.capitalize()
