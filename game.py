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
    print("'But what if I want to read the acts!!' (You think).")
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

    barabbas_on = False

    while True:

        question = input("> ").lower()

        if question == "hello":
            print("Hello my friend.")
        elif "who are you" in question:
            print("I am Mark, the author of the first gospel.")
        elif "real or myth" in question:
            print("I was writing a myth for my own purposes.")
        elif "how" and "know" in question:
            print("By analyizing my text, I can give you an example if you wish.")
        elif "example" in question:
            print("You are surely familiar with the episode at the crucifixion,"
                  "where Pilate makes the people chose between Jesus and Barabbas")
            print("At first glance it might seem like some historical truth under the myth.")
            print("But that's not what it is.")
            barabbas_on = True
        elif barabbas_on and "barabbas" in question:
            print("This is the story as I've told it in my gospel.")
            print("At the feast, Pilate used to release to them one prisoner of their choice. "
                  "And there was one called Barabbas, chained up with those who'd engaged in rebellion, " 
                  "who in the insurrection had committed murder. "
                  "The mob went up and began to ask him to do what he usually did for them. "
                  "And Pilate answered them, saying, 'Do you want me to release to you the King of the Jews?' " 
                  "For he realized the chief priests had seized [Jesus] out of jealousy. "
                  "But the chief priests stirred up the mob, so he would release Barabbas to them instead. "
                  "And Pilate again answered and said to them, 'So what should I do about the one you call the King of the Jews?' " 
                  "And they cried out again, 'Crucify him!' And Pilate said, 'What evil has he done?' But they cried out more, " 
                  "'Crucify him!' And Pilate, wishing to satisfy the mob, released to them Barabbas, "
                  "and sent Jesus to be whipped and crucified (Mk 15.6-15)")
        elif "what is it" in question:
            print("It's an allegory for the Jewish ritual at Yom Kippur.")
            print("During the ritual two goats were chosen: ")
            print("one to be released in the wild containing the sins of Israel, the other to be slaughtered.")
        elif "what does barabbas mean" in question:
            print("Son of the Father in Aramaic.")
        elif "what were your purposes" in question:
            print("Depict one revolutionary against the other, Barabbas the murderous leader of a military revolution.")
            print("The messiah the people wanted.")
            print("Vs. Jesus, the spiritual saviour, the messiah as God wanted him to be.")
        else:
            print("I don't know that.")

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
