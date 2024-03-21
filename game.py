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
            print("You hear someone screaming, 'Come on in, the door is open!'")
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
    print("You find yourself in a library with the biblical texts, up on display.")
    print("in the middle are the epistles of Paul.")
    print("On your left are the gospels of Luke and Mark.")
    print("On your right are the gospels of Matthew and John.")
    print("'But I want to read the acts!!' (You think).")
    print("It's on the floor.")
    print("Where do you want to start?")


    while True:

        choice = input("> ").lower()

        if choice == "paul":
            talk_with_paul()
        elif choice == "mark":
            talk_with_mark()
        elif choice == "luke":
            talk_with_luke()
        elif choice == "matthew":
            talk_with_matthew()
        elif choice == "john":
            talk_with_john()
        elif choice == "acts":
            fuck_the_acts()
        else:
            print("I will not comply with that.")

def talk_with_paul():
    print("You made it")
    exit(0)

def talk_with_mark():
    print("Welcome my friend.")
    print("What do you want to know?")

    while True:

        question = input("> ").lower()

        if question == "hello":
            print("Hello my friend.")
        elif "jesus" in question:
            print("example")
        else:
            print("I don't know that.")
            exit(0)



    exit(0)

def talk_with_luke():
    print("Luke")
    exit(0)

def talk_with_matthew():
    print("Matthew")
    exit(0)

def talk_with_john():
    print("John")
    exit(0)

def fuck_the_acts():
    print("ACt")
    exit(0)

def dead(reason):
    print(reason, "You Died.")
    exit(0)

start()
