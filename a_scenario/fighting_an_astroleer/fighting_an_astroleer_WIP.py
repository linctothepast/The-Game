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
    astroleer_health = random.randint(57, 74)
if level == 14:
    astroleer_color = "red"
    astroleer_health = random.randint(62, 80)
if level == 15:
    astroleer_color = "pink"
    astroleer_health = random.randint(67, 86)
if level == 16:
    astroleer_color = "purple"
    astroleer_health = random.randint(73, 93)
if level == 17:
    astroleer_color = "indigo"
    astroleer_health = random.randint(79, 100)
if level == 18:
    astroleer_color = "black"
    astroleer_health = random.randint(86, 108)
if level == 19:
    astroleer_color = "silver"
    astroleer_health = random.randint(93, 116)
if level == 20:
    astroleer_color = "gold"
    astroleer_health = random.randint(100, 124)
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
