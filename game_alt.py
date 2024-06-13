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
        biblical_sources()
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

def biblical_sources():
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
    print("Welcome friend, I'm Paul.")
    print("I'm here to guide you through your journey.")
    print("You will first hear about the Acts of the Apostles.")
    print("Traditionally attributed to Luke the evangelist.")
    print("We're going to help you evaluate if they are historical evidence or not.")
    print("Luke will answer your questions, when you're done with him ask for me again.")

    dialogue = ["hello", "who are you", "sources", "how do we know you're not writing history?", "more examples"]

    while True:

        question = input("> ").lower()

        if question == "hello":
            print("Hello my friend.")
        elif "who are you" in question:
            print("I am Luke.")
        elif "sources" in question:
            print("My only historical source was Josephus, used for background context.")
            print("My other sources were literary. The old testament and Homer.")
        elif "how do we know you're not writing history?" in question:
            print("The contradictions. In his letters Paul says that his face was unknown to the churches in Judea until many years after his conversion.")
            print("And after his conversion he went to Arabia and then Damascus, only returning to Jerusalem after three years.")
            print("But in my story he interacts with the Jerusalem church from the very beginning, even before his conversion.")
            print("And he never visits Arabia after his conversion, he just goes to Damascus and back to Jerusalem after a few weeks.")
            print("Paul's story in the acts parallels Jesus story, but Paul does it in a much more bombastic way than Jesus.")
            print("He travels across the whole northeastern Mediterranean, Jesus only the Sea of Galilee.")
            print("His trials last years not a single night, armies plot to assassinate him and armies come to rescue him.")
            print("Both Paul and Jesus die and resurrect, but after his resurrection Paul goes back to his preaching.")
            print("Paul is then sent to meet the emperor of Rome, something that Jesus never accomplish.")
        elif "more examples" in question:
            print("I take elements from the book of Tobit.")
            print("You can figure it out from the language I use.")
            print("When Paul is cured from his blindness we are told that 'the blindness fell from his eyes like scales'.")
            print("In Tobit Rafael is told by God to 'scale away (lepisai)' Tobias's blindess. My use of language for Paul's only makes sense as an allusion to this.")
        elif question == "help":
            help(dialogue)
        elif question == "paul":
            talk_with_mark()
        else:
            print("I cannot help you with that.")

def talk_with_mark():
    print("'Hello friend, this is Paul again.'")
    print("'You are now gonna talk with Mark about his gospel.'")
    print("'Like before, ask for me again when you are done.'")
    print("Paul escorts you to a room, magic seems to bring you in front of another man.")
    print("'Welcome my friend.'")
    print("'What do you want to know?'")

    dialogue = ["hello", "who are you", "real or myth", "how do we know", "example", "go back"]
    dialogue_unlocked = ["barabbas", "what is it", "what does barabbas mean", "what were your purposes"]
    joined_dialogue = dialogue + dialogue_unlocked

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
        elif "what is it" in question and barabbas_on:
            print("It's an allegory for the Jewish ritual at Yom Kippur.")
            print("During the ritual two goats were chosen: ")
            print("one to be released in the wild containing the sins of Israel, the other to be slaughtered.")
        elif "what does barabbas mean" in question and barabbas_on:
            print("Son of the Father in Aramaic.")
        elif "what were your purposes" in question and barabbas_on:
            print("Depict one revolutionary against the other, Barabbas the murderous leader of a military revolution.")
            print("The messiah the people wanted.")
            print("Vs. Jesus, the spiritual saviour, the messiah as God wanted him to be.")
        elif "go back" in question:
            fuck_the_acts()
        elif question == "help" and not barabbas_on:
            help(dialogue)
        elif question == "help" and barabbas_on:
            help(joined_dialogue)
        elif question == "paul":
            talk_with_matthew()
        else:
            print("I don't know that.")

def talk_with_matthew():
    print("Paul grabs your hand, you feel a bit weird.")
    print("'It's time for you to meet Matthew traveler.'")
    print("You feel like you're floating to another destination guided by the apostle.")
    print("You settle in front of another man, looking like a greek statue.")
    print("'There you are, let me answer your questions.'")

    dialogue = ["hello", "who are you", "what sources did you use", "what were your intentions", "how do we know your source was mark", "sermon on the mount historical", "go back"]

    while True:

        question = input("> ").lower()

        if question == "hello":
            print("Hello friend.")
        elif "who are you" in question:
            print("I am Matthew, the author of the second gospel.")
        elif "what sources did you use" in question:
            print("My source was the gospel of Mark.")
        elif "what were your intentions" in question:
            print("I wanted a version of Christianity that was more torah friendly.")
        elif "how do we know your source was mark" in question:
            print("I rewrote his gospel to fit my agenda, sometimes I fixed his mistakes"
                  "and made things more ridiculous in the process."
                  "Like my interpretation of the donkey passage in Zechariah 9.9."
                  "I wanted it to be more faithful to scripture"
                  "So I made Jesus enter Jerusalem on two donkeys because I read it as:"
                  "See, your king comes to you," 
                  "righteous and victorious,"
                  "lowly and riding on a donkey,"
                  "AND on a colt, the foal of a donkey.")
        elif "sermon on the mount historical" in question:
            print("There is no reason to believe that.")
            print("I meticulously crafted it to have a literary structure.")
            print("It fits within rabbinical discourses on how could the jews fulfill the law without the temple.")
        elif "go back" in question:
            talk_with_mark()
        elif question == "help":
            help(dialogue)
        elif question == "paul":
            talk_with_luke()
        else:
            print("I can't answer that question.")

def talk_with_luke():
    print("'Follow me traveler' says the familiar voice of Paul.")
    print("You cannot clearly see him, but you feel a force guiding you to another area.")
    print("You're engulfed by the light, and a voice greets you.")
    print("You've reached Luke's abode.")
    print("I am him.")
    print("What's on your mind friend?")

    dialogue = ["hello","who are you", "you writing history", "sources", "example"]

    while True:

        question = input("> ").lower()
        
        if question == "hello":
            print("Hello friend.")
        elif question == "who are you":
            print("I am Luke, the author of the third gospel and the acts. We meet again.")
        elif "you writing history" in question:
            print("I was pretending to.")
            print("But I wasn't actually consulting sources.")
            print("I was just taking from Mark and Matthew and changing it to my liking.")
            print("What you see is the illusion of historical narration.")
        elif "sources" in question:
            print("Mark, Matthew and scripture.")
        elif "example" in question:
            print("My story of the healing of the widow's son at Naim.")
            print("It's a retelling of the same legend told of Elijah in the book of Kings.")
            print(' Some time later the son of the woman who owned the house became ill.\n' 
            'He grew worse and worse, and finally stopped breathing. She said to Elijah, “What do you have against me, man of God? \n'
            'Did you come to remind me of my sin and kill my son?”\n'
            '“Give me your son,” Elijah replied. He took him from her arms, carried him to the upper room where he was staying, \n'
            'and laid him on his bed. 20 Then he cried out to the Lord, “Lord my God, have you brought tragedy even on this widow I am staying with, \n' 
            'by causing her son to die?” 21 Then he stretched himself out on the boy three times and cried out to the Lord, \n'
            '“Lord my God, let this boy’s life return to him!” \n'
            'The Lord heard Elijah’s cry, and the boy’s life returned to him, and he lived. \n'
            'Elijah picked up the child and carried him down from the room into the house. \n'
            'He gave him to his mother and said, “Look, your son is alive!” \n'
            'Then the woman said to Elijah, “Now I know that you are a man of God and that the word of the Lord from your mouth is the truth.”\n')
        elif question == "help":
            help(dialogue)
        elif question == "go back":
            talk_with_matthew()
        elif question == "paul":
            talk_with_john()
        else:
            print("That's unknown to me.")

def talk_with_john():
    print("'You are getting close traveler, it's time for you to meet the author of the last gospel'.")
    print("Paul lifts you up with a force that takes your breath away for a moment, you find yourself in another area.")
    print("'Hello wanderer' says a polyphonic voice.")
    print("'I'm John, come witness my signs.'")

    dialogue = ["hello", "who are you", "is your gospel independent", "sources", "historical", "example", "go back"]

    while True:

        question = input("> ").lower()
        
        if question == "hello":
            print("Hello friend.")
        elif question == "who are you":
            print("I am John, or am I the many people that pretend to be John?")
        elif "is your gospel independent" in question:
            print("There's no reason to believe that.")
            print("I clearly know of Mark, I tell the same stories in the same order.")
            print("I insert the same character in the story as Luke, Martha, Mary's sister.")
            print("And me and Luke both claim Judas was possesed by Satan.")
            print("Mark's gospel theme was that Jesus would leave no signs to the jews.")
            print("Luke's and Matthew's have the resurrection as one sign.")
            print("My gospel has all the signs!!")
        elif "sources" in question:
            print("I also used the old testament to craft my miracle stories.")
            print("Jesus' first miracle at Cana is turning water into wine.")
            print("Just like Moses in exodus, where God has him turn water into blood as a sign.")
            print(" 'If they will not believe even after these two signs, nor listen to you,\nthen you shall take some of the water from the river, "
                  "and pour it on the dry ground, \nand the water that you took out of the river shall become blood upon the ground.'")
            print("I turned the last into the first.")
        elif "historical" in question or "example" in question:
            print("There is no reason to believe I'm writing history.")
            print("I'm the most fervent propagandist of them all.")
            print("I insert the most ridiculous storylines to fit my 'giving signs' purpose.")
            print("The Doubting Thomas episode for example.")
            print("Or Lazarus, the beloved disciple.")
            print("None of the other gospels have heard of him.")
            print("There's a Lazarus mentioned in Luke I decided to make a character of my story.")
            print("I made Lazarus very relevant in my gospel, he's the one that witnesses everything, and I cite as my source.")
            print("He's so important that I turned his resurrection as the reason the Jews killed Jesus.")
            print("None of this happens in the other gospels, because it is my invention, to fit my purpose.")
        elif question == "go back":
            talk_with_luke()
        elif question == "paul":
            talk_with_paul()
        elif question == "help":
            help(dialogue)
        else:
            print("That's unknown to me.")

def talk_with_paul():
    print("You made it")
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

    if "angel" in choice and not "man" in choice:
        gold_room()
    elif "man" in choice and not "angel" in choice:
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

def help(questions):
    list_lenght = len(questions)
    index = r.randint(0, list_lenght - 1)
    print(f"{questions[index]}")

def dead(reason):
    print(reason, "You Died.")
    exit(0)

start()