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
    
def extrabiblical_sources():
    sources = ["Clement of Rome", "Ignatius of Antioch", "Eusebius", "Hegesippus", "Josephus", "Pliny", "Tacitus", "Suetonius", "George Syncellus"]
    phrases = [
        "I don't know him personally, but I've been told he spoke thus: \n“Be merciful, that ye may obtain mercy.\nForgive, that ye may be forgiven.\nAs ye do, so shall it be done unto you.",
        "How was he manifested to the world?\nA star shone forth in heaven above all the other stars,\nthe light of which was inexpressible,\nwhile its novelty struck men with astonishment.\nAnd all the rest of the stars,"
        "with the sun and moon,\nformed a chorus to this star,\nand its light was exceedingly great above them all.",
        "Well, a very stupid man called Papias told Iraneus, that told me, that the Lord used to teach about the end of times:\n'The days will come when vines will grow, each having ten thousand shoots,"
        "and on each shoot ten thousand branches, and on each branch ten thousand twigs,\nand on each twig ten thousand clusters, and in each cluster ten thousand grapes,"
        "and each grape when crushed will yield twenty-five measures of wine.'\nDo with that what you will my friend!",
        "I know of the brother of the Lord James, he was holy from his mother's womb;\nand he drank no wine nor strong drink, nor did he eat flesh."
        "No razor came upon his head; he did not anoint himself with oil, and he did not use the bath.\nHe alone was permitted to enter into the holy place; for he wore not woolen but linen garments."
        "The sects before mentioned did not believe, either in a resurrection or in the coming of one to requite every man according to his works; \nbut those who did believe, believed because of James."
        "The aforesaid scribes and Pharisees accordingly set James on the summit of the temple, and cried aloud to him, and said:\n'O just one, whom we are all bound to obey, forasmuch as the people are in error,"
        "and follow Jesus the crucified, do tell us what is the door of Jesus the crucified'.\nAnd he answered: 'Why ask me concerning Jesus the Son of Man? He Himself sits in heaven, at the right hand of the Great Power,"
        "and shall come on the clouds of heaven.' And, when many were fully convinced by these words, and said, 'Hosanna to the son of David',\nthe Pharisees and scribes said to one another:"
        "'We have not done well in procuring this testimony to Jesus. But let us go up and throw him down'.\nThus they fulfilled the Scripture written in Isaiah: 'Let us away with the just man, because he is troublesome to us:"
        "therefore shall they eat the fruit of their doings'. So they went up and threw down the just man, and said to one another: 'Let us stone James the Just'.\nAnd they began to stone him: for he was not killed by the fall;"
        "but he turned, and kneeled down, and said: 'I beseech Thee, Lord God our Father, forgive them; for they know not what they do'\nAnd so he suffered martyrdom; and they buried him on the spot.",
        "I'm afraid, my friend, that they are making me say words I've never written down.\nI was listing the known crimes of the Roman man known as Pontius Pilate, and a brief passage about this man Jesus appears there."
        "But if you know of my character, my friend, you will believe it to be fake. I explain things in great detail, and this passage is too brief and vague.\nAnd the funny part is that, the sentence after it says:"
        "'About the same time also another sad calamity put the Jews into disorder.'",
        "I know this Christ was a god worshipped by some cultists. They were in the habit of meeting on a certain fixed day before it was light," 
        "when they sang in alternate verses a hymn to Christ, as to a god, and bound themselves by a solemn oath, not to any wicked deeds,"
        "but never to commit any fraud, theft or adultery, never to falsify their word, nor deny a trust when they should be called upon to deliver it up;"
        "after which it was their custom to separate, and then reassemble to partake of food, but food of an ordinary and innocent kind.",
        "Ah! I talk about 'ChrEstianus' being accused and tortured by Nero during the fire of Rome,\nChrestus is also mentioned by our friend Suetonius here in his history,"
        "I'm being told something was added to it! About Pontius Pilate crucifying their leader Christ!\nBut their leader was Chrestus! Filthy superstitious cultists!",
        "I know nothing of the man Christ, only a bit about the Jew Chrestus, and I know of Christians being persecuted!",
        "I read in a Sextus Julius Africanus work, that was quoting another lost work of the historian Thallus,"
        "that he reported the eclipse and earthquake that happened on the day of the death of Jesus.\nBut my friend Eusebius here says I'm lying! Thallus never said anything relating the eclipse to the death of Jesus!"
        "He was just mentioning an eclipse and earthquake in Bythinia!"
        ]
    dates = ["95 CE or 60 CE, depending on who you ask.", "110 CE", "130 and 150 CE but I wrote in the 4th century", "180 CE", "93 CE", "112 CE", "116 CE", "121 CE", "50 CE (allegedly) but I wrote in the 9th century"]

    index = r.randint(0, 8)

    print("The path leads you to a dining hall.")
    #sleep(1)
    print("Nine men are sitting around a table.")
    #sleep(1)
    print("""They don't really bother to invite you to sit down, 
    but you can see there's an empty chair and plate for you.""")
    #sleep(1)
    print(f"""You sit next to one of them, and he presents himself.
    'Hello friend, my name is {sources[index]}'""")

    while True:
        dialogue = input("> ").lower()

        if "hello" in dialogue:
            print("Greetings! What do you want to know my friend?")
        elif "jesus" and "exist" in dialogue:
            print(f"{phrases[index]}")
        elif "change seat" in dialogue:
            index = r.randint(0, 8)
            print(f"Hello friend, I'm {sources[index]}.")
        elif "when" and "written" in dialogue:
            print(f"Around the year {dates[index]}.")
        elif "go back" in dialogue:
            start()
        elif "made" and "choice" in dialogue:
            pick_your_jesus()
        else:
            print("I don't know that.")

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
            fuck_the_acts()
        else:
            print("I cannot do that.")

def fuck_the_acts():
    print("ACt")
    exit(0)

def jesus_not_here_room():
    print("Jesus is not here!!")
    print("But you do find the credits for this game.")
    print("Credits to 'On the historicity of Jesus' by Richard Carrier.")
    print("""And all those little rascal authors of ancient Christianity,
    that made all of this possible.""")

    choice = input("Do you want to go back to the start?\n> ").lower()

    if choice == "yes":
        start()
    elif choice == "no":
        print("Hope to see you again friend.")
        exit(0)
    else:
        dead("Mythical Jesus spears you from outer space with the sword of justice.")

def pick_your_jesus():
    print("You find yourself in a room with two statues")
    print("In one Jesus is portrayed like an angel")
    print("In the other he is portrayed like a man.")
    print("Which one do you pick?")

    choice = input("> ").lower()

    if "angel" and not "man" in choice:
        gold_room()
    elif "man" and not "angel" in choice:
        silver_room()
    else:
        dead("Jesus urged you to make a choice with his angel sword.")

def gold_room():
    print("You believe that Jesus was a mythical entity.")
    print("Crucified in a level of heaven by demons.")
    print("You win 1000 pieces of gold.")
    exit(0)

def silver_room():
    print("You believe that Jesus was a historical man.")
    print("Crucified by Romans on earth.")
    print("You win 100 pieces of gold.")
    exit(0)

def dead(reason):
    print(reason, "You Died.")
    exit(0)


start()