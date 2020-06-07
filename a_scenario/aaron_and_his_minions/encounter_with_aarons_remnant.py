import random
player_health = 100
print("""A ghostly top half of a body with and evil grin
on his face, and a thin goatee floats over to you your
body shall be my new vessel in this world. He laughs at
you as a blue icy flame appears in his hand.""")
aarons_remnant_health = random.randint(15, 47)
aarons_remnant_attack = random.randint(1, 3)
if aarons_remnant_attack <= 2:
    print("""Aarons Remnant conjures and icy blue flame
and tosses it at you, you feel a cold burning feeling
all over your body.""")
    aarons_remnant_damage = random.randint(20, 25)
    print("you take " + str(aarons_remnant_damage) + " damage.")
    player_health -= aarons_remnant_damage
elif aarons_remnant_attack == 3:
    print("""Aarons Remnant flies over to you and reaches into
your body, you feel a cold hand pulling at your heart. """)
    con_saving_throw = random.randint(1, 20)
    if con_saving_throw >= 11:
        print("You are mostly unharmed and feel nothing else.")
    elif con_saving_throw < 11 and con_saving_throw >= 2:
        aarons_remnant_damage = random.randint(30, 40)
        print("""You feel a a cold pulling sensation in your
heart as it moves in ways it shouldn't, and you
take """ + str(aarons_remnant_damage) + """ damage.""")
        player_health -= aarons_remnant_damage
    else:
        aarons_remnant_damage = random.randint(60, 80)
        print("""You heart has a wretching cold feeling as
it is almost ripped out of your body the intense pain
makes blood drip out your mouth and ears, you
take """ + str(aarons_remnant_damage) + """ damage.""")
        player_health -= aarons_remnant_damage
