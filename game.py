from sys import exit
from time import sleep
import random as r


def start():
    print("You're on the quest for the historical jesus.")
    # sleep(1)
    print("You are in a cave with three paths.")
    # sleep(2)
    print("From what path do you start? North, east or west?")
    
    choice = input("> ").lower()

    if "west" in choice:
        door_puzzle()
    elif "east" in choice:
        extrabiblical_sources()
    elif "north" in choice:
        jesus_not_here_room()
    else:
        dead("Upon too much pondering the holy spirit engulfes you and carries you to heaven. "
             "Maybe Jesus is crucified there.")


def door_puzzle():
    print("The path you chose brings you to a tall door.")
    print("What do you do?")

    door_open = False

    while True:

        action = input("> ").lower()

        if 'knock' in action:
            print("You hear someone screaming, 'Come on in door is open!'")
        elif action == 'jesus christ':
            print("The door opens with a loud creeking sound.")
            door_open = True
        elif 'look' and 'door' in action:
            print("It's a very sturdy door. There's some writing on it.")
        elif 'read' and 'writing' in action:
            print("The writing says 'λόγος'")
        elif action == 'enter' and door_open:
            print("You enter the library.")
            biblical_sources()
        else:
            print("I cannot do that.")

def biblical_sources():
    print("There you are.")
    exit(0)

def dead(reason):
    print(reason, "You Died.")
    exit(0)

start()
