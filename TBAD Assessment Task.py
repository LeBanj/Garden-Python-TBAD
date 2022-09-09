import time
import sys
import random
from datetime import date

# defining non room functions
def MV(message):
    print("Mysterious Voice: " + message)


def wait(seconds):
    time.sleep(seconds)


# room functions
def welcome_room():
    print("WELCOME TO THE GARDEN!")
    wait(6)
    print("Do you wish to play?")
    print("yes/no")
    action = input("> ")
    if action == "yes":
        wait(4)
        state["room"] = "cliff"
    elif action == "no":
        state["room"] = "quit"
    else:
        print("unknown input")
        print("yes/no")
        action = input("> ")


def cliff_room():
    # player forced to move forwards and fall off the cliff
    print(
        "You find yourself atop a barren, windy clifftop after being knocked unconcious walking home one night."
    )
    wait(2)
    print("Actions: forward")
    action = input("> ")
    if action == "forward":
        state["room"] = "cliffedge"
    elif action == "quit":
        state["room"] = "quit"
    else:
        print("cannot do that here")


def cliffedge_room():
    # this is the initiation of the game and the player cannot do anything here
    print(
        "As you walk closer to the edge of the cliff, a strong gust of wind surges past,"
    )
    wait(2)
    print(
        "knocking you over the edge of the cliff and plunging into the darkness below."
    )
    state["room"] = "gardenstart1"


def gardenstart1_room():
    # the cutscene to the garden
    wait(2)
    print("You land in a puddle of mud in a dark, swampy garden.")
    wait(3)
    print("You feel as if you are being watched.")
    wait(3)
    MV("Welcome to the garden, if you are lucky you will make it out alive.")
    wait(4)
    MV("Your objective is to escape. There are no rules, no exceptions, and no hints.")
    wait(5)
    MV("Good luck, you'll need it")
    state["room"] = "gardenstart3"
    # the intro is now over and you can actually play the game


def gardenstart2_room():
    # what happens when "look" is typed or when the room is re-entered, and my desperate solution to the first time cutscene problem :D
    print("You are standing in a puddle of mud in a dark, swampy garden.")
    state["room"] = "gardenstart3"


def gardenstart3_room():
    # action room of the FIRST ROOM
    wait(2)
    print("Actions: forward, look")
    action = input("> ")
    if action == "forward":
        state["room"] = "maingarden"
    elif action == "look":
        state["room"] = "gardenstart2"
    elif action == "quit":
        state["room"] = "quit"
    else:
        print("cannot do that here")
        print("Actions: forward, look")
        action = input("> ")


def maingarden_room():
    # this is where the garden opens up. there is a key in a pond to the left and a key up a tree to the right
    wait(1)
    print(
        "You are standing in a large open garden. To your left is a murky pond and to your right is a dark, looming tree"
    )
    wait(2)
    print("Actions: forward, backward, left, right, look")
    action = input("> ")
    if action == "forward":
        state["room"] = "gardendoor"
    elif action == "backward":
        state["room"] = "gardenstart2"
    elif action == "left":
        state["room"] = "gardenpond"
    elif action == "right":
        state["room"] = "gardentree"
    elif action == "look":
        print(
            "You are standing in a large open garden. To your left is a murky pond and to your right is a dark, looming tree"
        )
        print("Actions: forward, backward, left, right, look")
        action = input("> ")
    elif action == "quit":
        state["room"] = "quit"
    else:
        print("cannot do that here")
        print("Actions: forward, backward, left, right, look")
        action = input("> ")


def gardenpond_room():
    wait(1)
    print(
        "You are standing in front of a murky pond. You feel as if you can see eyes from within the water."
    )
    if state["key1"]:
        print("Actions: backward, look")
    elif state["looked_for_key1"]:
        print("Actions: backward, look, pickup")
    else:
        print("Actions: backward, look")

    action = input("> ")
    if action == "backward":
        state["room"] = "maingarden"
    elif action == "look":
        print("You spot a key on the floor.")
        state["looked_for_key1"] = True
    elif action == "pickup":
        print("You picked up the blue key!")
        state["key1"] = True
    elif action == "quit":
        state["room"] = "quit"
    else:
        print("cannot do that here")
        print("Actions: forward, look")
        action = input("> ")


def gardentree_room():
    wait(1)
    print(
        "You are standing at the bottom of a tall, looming tree with its long spooky leaves and creaky branches."
    )
    if state["key2"]:
        print("Actions available: backward, look")
    elif state["looked_for_key2"]:
        print("Actions available: backward, look, pickup")
    else:
        print("Actions available: backward, look")

    action = input("> ")
    if action == "backward":
        state["room"] = "maingarden"
    elif action == "look":
        print("You spot a key on the floor.")
        state["looked_for_key2"] = True
    elif action == "pickup":
        print("You picked up the red key!")
        state["key2"] = True
    elif action == "quit":
        state["room"] = "quit"
    else:
        print("cannot do that here")
        print("Actions: forward, look")
        action = input("> ")


def gardendoor_room():
    wait(1)
    print("In front of you is a large spruce door. You can see it has a red keyhole.")
    if state["key2"] is True:
        print("Actions available: forward, backward, look")
    else:
        print("Actions available: backward, look")
    action = input("> ")
    if action == "forward":
        if state["key2"] is True:
            state["room"] = "boss"
    elif action == "backward":
        state["room"] = "maingarden"
    elif action == "look":
        print(
            "In front of you is a large spruce door. You can see it has a red keyhole."
        )
        state["room"] = "gardendoor"
    elif action == "quit":
        state["room"] = "quit"
    else:
        print("cannot do that here")
        print("Actions: forward, look")
        action = input("> ")


def boss_room():
    wait(1)
    print("You unlocked the door and passed through it.")
    wait(1)
    print("You can see the exit at the other side of this room.")
    wait(1)
    print("In the way is a silver plated knight wielding a rusty mace.")
    wait(1)
    print("You walk toward the knight, picking up a sword lying on the floor")
    wait(1)
    print("You swing at the knight, hitting his plated elbow and dealing 0.0001 damage")
    wait(1)
    print(
        "The knight bring the mace down right where your head was 1 second ago, a lucky miss"
    )
    wait(1)
    print("HP: 50/50     Enemy HP: 49.9999/50")
    wait(1)
    print("The knight isn't very good at fighting, but he's very bulky")
    wait(1)
    print("You watch as the knight runs around flailing his arms")
    wait(1)
    print("You walk to the end of the room where there is a lever")
    wait(1)
    print("Actions: pull")
    action = input("> ")
    if action == "pull":
        print("You pull the lever and the room starts to collapse")
        wait(1)
        print("Rocks are falling everywhere, almost crushing you")
        wait(1)
        print(
            "The knight looks up right as a boulder crushes him, dealing lethal damage."
        )
        wait(1)
        print("HP: 50/50")
        wait(2)
        game_complete()
    elif action == "quit":
        state["room"] = "quit"
    else:
        print("cannot do that here")


def quit_room():
    wait(2)
    print("BYE BYE")
    wait(5)
    sys.exit()


def game_complete():
    wait(1)
    MV("Damnit, I had money on that ones death.")
    MV("Oh well, better luck next year I guess.")
    wait(3)
    sys.exit()


state = {
    "room": "welcome",
    "looked_for_key1": False,
    "looked_for_key2": False,
    "key1": False,
    "key2": False,
    "bluekey": False,
    "redkey": False,
}

# this is where code starts doing code


today = date.today()

# dd/mm/YY
ddmmyy = today.strftime("%d/%m/%Y")
print("Banjo Stapledon, Date:", ddmmyy)

while True:
    if state["room"] == "welcome":
        welcome_room()
    elif state["room"] == "cliff":
        cliff_room()
    elif state["room"] == "cliffedge":
        cliffedge_room()
    elif state["room"] == "gardenstart1":
        gardenstart1_room()
    elif state["room"] == "gardenstart2":
        gardenstart2_room()
    elif state["room"] == "gardenstart3":
        gardenstart3_room()
    elif state["room"] == "maingarden":
        maingarden_room()
    elif state["room"] == "gardentree":
        gardentree_room()
    elif state["room"] == "gardenpond":
        gardenpond_room()
    elif state["room"] == "gardendoor":
        gardendoor_room()
    elif state["room"] == "boss":
        boss_room()
    elif state["room"] == "quit":
        quit_room()
