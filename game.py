from sys import exit
from time import sleep
import random as r
import time

def start():
    fancy_print("You're on the quest for the historical jesus.")
    fancy_print("You are in a cave with three paths.")
    fancy_print("From what path do you start? North, east or west?")
    
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
        "I don't know him personally, but I've been told he spoke thus: \n"
        "“Be merciful, that ye may obtain mercy.\nForgive, that ye may be forgiven.\nAs ye do, so shall it be done unto you.",
        "How was he manifested to the world?\n"
        "A star shone forth in heaven above all the other stars, \n"
        "the light of which was inexpressible,\nwhile its novelty struck men with astonishment.\nAnd all the rest of the stars,\n"
        "with the sun and moon,\nformed a chorus to this star,\nand its light was exceedingly great above them all.",
        "Well, a very stupid man called Papias told Iraneus, that told me, that the Lord used to teach about the end of times:\n"
        "'The days will come when vines will grow,\n"
        "each having ten thousand shoots,\n"
        "and on each shoot ten thousand branches, \n"
        "and on each branch ten thousand twigs, \n"
        "and on each twig ten thousand clusters,\n"
        "and in each cluster ten thousand grapes, \n"
        "and each grape when crushed will yield twenty-five measures of wine.'\n"
        "Do with that what you will my friend!\n",
        "I know of the brother of the Lord James, he was holy from his mother's womb;\n"
        "and he drank no wine nor strong drink, nor did he eat flesh.\n"
        "No razor came upon his head; he did not anoint himself with oil,\n"
        "and he did not use the bath. He alone was permitted to enter into the holy place;\n" 
        "for he wore not woolen but linen garments.\n"
        "The sects before mentioned did not believe, \n"
        "either in a resurrection or in the coming of one to requite every man according to his works;\n"
        "but those who did believe, believed because of James.\n"
        "The aforesaid scribes and Pharisees accordingly set James on the summit of the temple,\n"
        "and cried aloud to him, and said:\n"
        "'O just one, whom we are all bound to obey, forasmuch as the people are in error,\n"
        "and follow Jesus the crucified, do tell us what is the door of Jesus the crucified'.\n"
        "And he answered: 'Why ask me concerning Jesus the Son of Man?\n"
        "He Himself sits in heaven, at the right hand of the Great Power,\n"
        "and shall come on the clouds of heaven.' \n"
        "And, when many were fully convinced by these words, and said, \n"
        "'Hosanna to the son of David',\n"
        "the Pharisees and scribes said to one another:\n"
        "'We have not done well in procuring this testimony to Jesus.\n"
        "But let us go up and throw him down'.\n"
        "Thus they fulfilled the Scripture written in Isaiah: \n"
        "'Let us away with the just man, because he is troublesome to us:\n"
        "therefore shall they eat the fruit of their doings'.\n" 
        "So they went up and threw down the just man, and said to one another:\n"
        "'Let us stone James the Just'.\n"
        "And they began to stone him: for he was not killed by the fall;\n"
        "but he turned, and kneeled down, and said:\n"
        "'I beseech Thee, Lord God our Father, forgive them;\n" 
        "for they know not what they do'\n"
        "And so he suffered martyrdom; and they buried him on the spot.",
        "I'm afraid, my friend, that they are making me say words I've never written down.\n"
        "I was listing the known crimes of the Roman man known as Pontius Pilate,\n"
        "and a brief passage about this man Jesus appears there.\n"
        "But if you know of my character, my friend, you will believe it to be fake.\n"
        "I explain things in great detail, and this passage is too brief and vague.\n"
        "And the funny part is that, the sentence after it says:\n"
        "'About the same time also another sad calamity put the Jews into disorder.'",
        "I know this Christ was a god worshipped by some cultists. \n"
        "They were in the habit of meeting on a certain fixed day before it was light,\n" 
        "when they sang in alternate verses a hymn to Christ, as to a god,\n"
        "and bound themselves by a solemn oath, not to any wicked deeds,\n"
        "but never to commit any fraud, theft or adultery, never to falsify their word,\n"
        "nor deny a trust when they should be called upon to deliver it up;\n"
        "after which it was their custom to separate, and then reassemble to partake of food, \n"
        "but food of an ordinary and innocent kind.",
        "Ah! I talk about 'ChrEstianus' being accused and tortured by Nero during the fire of Rome,\n"
        "Chrestus is also mentioned by our friend Suetonius here in his history,\n"
        "I'm being told something was added to it! About Pontius Pilate crucifying their leader Christ!\n"
        "But their leader was Chrestus! Filthy superstitious cultists!",
        "I know nothing of the man Christ, only a bit about the Jew Chrestus, and I know of Christians being persecuted!",
        "I read in a Sextus Julius Africanus work, that was quoting another lost work of the historian Thallus,\n"
        "that he reported the eclipse and earthquake that happened on the day of the death of Jesus.\n"
        "But my friend Eusebius here says I'm lying! Thallus never said anything relating the eclipse to the death of Jesus!\n"
        "He was just mentioning an eclipse and earthquake in Bythinia!"
        ]
    dates = ["95 CE or 60 CE, depending on who you ask.", "110 CE", "130 and 150 CE but I wrote in the 4th century", "180 CE", "93 CE", "112 CE", "116 CE", "121 CE", "50 CE (allegedly) but I wrote in the 9th century"]

    index = r.randint(0, 8)

    fancy_print("The path leads you to a dining hall.")
    fancy_print("Nine men are sitting around a table.")
    fancy_print("""They don't really bother to invite you to sit down, 
    but you can see there's an empty chair and plate for you.""")
    fancy_print(f"""You sit next to one of them, and he presents himself.
    'Hello friend, my name is {sources[index]}'""")

    while True:
        dialogue = input("> ").lower()

        if "hello" in dialogue:
            fancy_print("Greetings! What do you want to know my friend?")
        elif "jesus" and "exist" in dialogue:
            fancy_print(f"{phrases[index]}")
        elif "change seat" in dialogue:
            index = r.randint(0, 8)
            fancy_print(f"Hello friend, I'm {sources[index]}.")
        elif "when" and "written" in dialogue:
            fancy_print(f"Around the year {dates[index]}.")
        elif "go back" in dialogue:
            start()
        elif "made" and "choice" in dialogue:
            pick_your_jesus()
        else:
            fancy_print("I don't know that.")

def biblical_sources():
    fancy_print("The path you chose brings you to a tall door.")
    fancy_print("What do you do?")

    door_open = False

    while True:

        action = input("> ").lower()

        if 'knock' in action:
            fancy_print("You hear someone screaming, 'Come on in, the door is open!'")
        elif action == 'jesus christ':
            fancy_print("The door opens with a loud creeking sound.")
            door_open = True
        elif 'door' in action:
            fancy_print("It's a very sturdy door. There's some writing on it.")
        elif 'writing' in action:
            fancy_print("The writing says 'λόγος'")
        elif action == 'enter' and door_open:
            fancy_print("You enter the library.")
            fuck_the_acts()
        else:
            fancy_print("I cannot do that.")

def fuck_the_acts():
    fancy_print("'Welcome friend, I'm Paul.'")
    fancy_print("'I'm here to guide you through your journey.'")
    fancy_print("'You will first hear about the Acts of the Apostles.'")
    fancy_print("'Traditionally attributed to Luke the evangelist.'")
    fancy_print("'We're going to help you evaluate if they are historical evidence or not.'")
    fancy_print("'Luke will answer your questions, when you're done with him ask for me again.'")

    dialogue = ["hello", "who are you", "sources", "how do we know you're not writing history?", "more examples"]

    while True:

        question = input("> ").lower()

        if question == "hello":
            fancy_print("Hello my friend.")
        elif "who are you" in question:
            fancy_print("I am Luke.")
        elif "sources" in question:
            fancy_print("My only historical source was Josephus, used for background context.")
            fancy_print("My other sources were literary. The old testament and Homer.")
        elif "how do we know you're not writing history" in question:
            fancy_print("The contradictions. In his letters Paul says that his face was unknown to the churches in Judea until many years after his conversion.")
            fancy_print("And after his conversion he went to Arabia and then Damascus, only returning to Jerusalem after three years.")
            fancy_print("But in my story he interacts with the Jerusalem church from the very beginning, even before his conversion.")
            fancy_print("And he never visits Arabia after his conversion, he just goes to Damascus and back to Jerusalem after a few weeks.")
            fancy_print("Paul's story in the acts parallels Jesus story, but Paul does it in a much more bombastic way than Jesus.")
            fancy_print("He travels across the whole northeastern Mediterranean, Jesus only the Sea of Galilee.")
            fancy_print("His trials last years not a single night, armies plot to assassinate him and armies come to rescue him.")
            fancy_print("Both Paul and Jesus die and resurrect, but after his resurrection Paul goes back to his preaching.")
            fancy_print("Paul is then sent to meet the emperor of Rome, something that Jesus never accomplish.")
        elif "more examples" in question:
            fancy_print("I take elements from the book of Tobit.")
            fancy_print("You can figure it out from the language I use.")
            fancy_print("When Paul is cured from his blindness we are told that 'the blindness fell from his eyes like scales'.")
            fancy_print("In Tobit Rafael is told by God to 'scale away (lepisai)' Tobias's blindess. My use of language for Paul's only makes sense as an allusion to this.")
        elif question == "help":
            help(dialogue)
        elif question == "paul":
            talk_with_mark()
        else:
            fancy_print("I cannot help you with that.")

def talk_with_mark():
    fancy_print("'Hello friend, this is Paul again.'")
    fancy_print("'You are now gonna talk with Mark about his gospel.'")
    fancy_print("'Like before, ask for me again when you are done.'")
    fancy_print("Paul escorts you to a room, magic seems to bring you in front of another man.")
    fancy_print("'Welcome my friend.'")
    fancy_print("'What do you want to know?'")

    dialogue = ["hello", "who are you", "real or myth", "how do we know", "example", "go back"]
    dialogue_unlocked = ["barabbas story", "what is it", "what does barabbas mean", "what were your purposes"]
    joined_dialogue = dialogue + dialogue_unlocked

    barabbas_on = False

    while True:

        question = input("> ").lower()

        if question == "hello":
            fancy_print("Hello my friend.")
        elif "who are you" in question:
            fancy_print("I am Mark, the author of the first gospel.")
        elif "real or myth" in question:
            fancy_print("I was writing a myth for my own purposes.")
        elif "how do we know" in question:
            fancy_print("By analyizing my text, I can give you an example if you wish.")
        elif "example" in question:
            fancy_print("You are surely familiar with the episode at the crucifixion,")
            fancy_print("where Pilate makes the people chose between Jesus and Barabbas")
            fancy_print("At first glance it might seem like some historical truth under the myth.")
            fancy_print("But that's not what it is.")
            barabbas_on = True
        elif barabbas_on and "barabbas story" in question:
            fancy_print("This is the story as I've told it in my gospel.")
            fancy_print("At the feast, Pilate used to release to them one prisoner of their choice. \n"
                  "And there was one called Barabbas, chained up with those who'd engaged in rebellion, \n" 
                  "who in the insurrection had committed murder. \n"
                  "The mob went up and began to ask him to do what he usually did for them. \n"
                  "And Pilate answered them, saying, 'Do you want me to release to you the King of the Jews?' \n" 
                  "For he realized the chief priests had seized [Jesus] out of jealousy. \n"
                  "But the chief priests stirred up the mob, so he would release Barabbas to them instead. \n"
                  "And Pilate again answered and said to them, 'So what should I do about the one you call the King of the Jews?' \n" 
                  "And they cried out again, 'Crucify him!' And Pilate said, 'What evil has he done?' But they cried out more, \n" 
                  "'Crucify him!' And Pilate, wishing to satisfy the mob, released to them Barabbas, \n"
                  "and sent Jesus to be whipped and crucified (Mk 15.6-15)")
        elif "what is it" in question and barabbas_on:
            fancy_print("It's an allegory for the Jewish ritual at Yom Kippur.")
            fancy_print("During the ritual two goats were chosen: ")
            fancy_print("one to be released in the wild containing the sins of Israel, the other to be slaughtered.")
        elif "what does barabbas mean" in question and barabbas_on:
            fancy_print("Son of the Father in Aramaic.")
        elif "what were your purposes" in question and barabbas_on:
            fancy_print("Depict one revolutionary against the other, Barabbas the murderous leader of a military revolution.")
            fancy_print("The messiah the people wanted.")
            fancy_print("Vs. Jesus, the spiritual saviour, the messiah as God wanted him to be.")
        elif "go back" in question:
            fuck_the_acts()
        elif question == "help" and not barabbas_on:
            help(dialogue)
        elif question == "help" and barabbas_on:
            help(joined_dialogue)
        elif question == "paul":
            talk_with_matthew()
        else:
            fancy_print("I don't know that.")

def talk_with_matthew():
    fancy_print("Paul grabs your hand, you feel a bit weird.")
    fancy_print("'It's time for you to meet Matthew, traveler.'")
    fancy_print("You feel like you're floating to another destination guided by the apostle.")
    fancy_print("You settle in front of another man, he looks like a greek statue.")
    fancy_print("'There you are, let me answer your questions' he says.")

    dialogue = ["hello", "who are you", "what sources did you use", "what were your intentions", "how do we know your source was mark", "sermon on the mount historical", "go back"]

    while True:

        question = input("> ").lower()

        if question == "hello":
            fancy_print("Hello friend.")
        elif "who are you" in question:
            fancy_print("I am Matthew, the author of the second gospel.")
        elif "what sources did you use" in question:
            fancy_print("My source was the gospel of Mark and scripture.")
        elif "what were your intentions" in question:
            fancy_print("I wanted a version of Christianity that was more torah friendly.")
        elif "how do we know your source was mark" in question:
            fancy_print("I rewrote his gospel to fit my agenda, sometimes I fixed his mistakes\n"
                  "and made things more ridiculous in the process.\n"
                  "Like my interpretation of the donkey passage in Zechariah 9.9.\n"
                  "I wanted it to be more faithful to scripture\n"
                  "So I made Jesus enter Jerusalem on two donkeys because I read it as:\n"
                  "See, your king comes to you,\n" 
                  "righteous and victorious,\n"
                  "lowly and riding on a donkey,\n"
                  "AND on a colt, the foal of a donkey.")
        elif "sermon on the mount historical" in question:
            fancy_print("There is no reason to believe that.")
            fancy_print("I meticulously crafted it to have a literary structure.")
            fancy_print("It fits within rabbinical discourses on how could the jews fulfill the law without the temple.")
        elif "go back" in question:
            talk_with_mark()
        elif question == "help":
            help(dialogue)
        elif question == "paul":
            talk_with_luke()
        else:
            fancy_print("I can't answer that question.")

def talk_with_luke():
    fancy_print("'Follow me traveler' says the familiar voice of Paul.")
    fancy_print("You cannot clearly see him, but you feel a force guiding you to another area.")
    fancy_print("You're engulfed by the light, a voice greets you.")
    fancy_print("'You've reached Luke's abode.'")
    fancy_print("'I am him.'")
    fancy_print("'What's on your mind friend?'")

    dialogue = ["hello", "who are you", "you writing history", "sources", "example"]

    while True:

        question = input("> ").lower()
        
        if question == "hello":
            fancy_print("Hello friend.")
        elif question == "who are you":
            fancy_print("I am Luke, the author of the third gospel and the acts. We meet again.")
        elif "you writing history" in question:
            fancy_print("I was pretending to.")
            fancy_print("But I wasn't actually consulting sources.")
            fancy_print("I was just taking from Mark and Matthew and changing it to my liking.")
            fancy_print("What you see is the illusion of historical narration.")
        elif "sources" in question:
            fancy_print("Mark, Matthew and scripture.")
        elif "example" in question:
            fancy_print("My story of the healing of the widow's son at Naim.")
            fancy_print("It's a retelling of the same legend told of Elijah in the book of Kings.")
            fancy_print(' Some time later the son of the woman who owned the house became ill.\n' 
            'He grew worse and worse, and finally stopped breathing. She said to Elijah, “What do you have against me, man of God? \n'
            'Did you come to remind me of my sin and kill my son?”\n'
            '“Give me your son,” Elijah replied. He took him from her arms, carried him to the upper room where he was staying, \n'
            'and laid him on his bed. 20 Then he cried out to the Lord, “Lord my God, have you brought tragedy even on this widow I am staying with, \n' 
            'by causing her son to die?” 21 Then he stretched himself out on the boy three times and cried out to the Lord, \n'
            '“Lord my God, let this boy’s life return to him!” \n'
            'The Lord heard Elijah’s cry, and the boy’s life returned to him, and he lived. \n'
            'Elijah picked up the child and carried him down from the room into the house. \n'
            'He gave him to his mother and said, “Look, your son is alive!” \n'
            'Then the woman said to Elijah, “Now I know that you are a man of God and that the word of the Lord from your mouth is the truth.”')
        elif question == "help":
            help(dialogue)
        elif question == "go back":
            talk_with_matthew()
        elif question == "paul":
            talk_with_john()
        else:
            fancy_print("That's unknown to me.")

def talk_with_john():
    fancy_print("'You are getting close traveler, it's time for you to meet the author of the last gospel'.")
    fancy_print("Paul lifts you up with a force that takes your breath away for a moment, you find yourself in another area.")
    fancy_print("'Hello wanderer' says a polyphonic voice.")
    fancy_print("'I'm John, come witness my signs.'")

    dialogue = ["hello", "who are you", "is your gospel independent", "sources", "historical", "example", "go back"]

    while True:

        question = input("> ").lower()
        
        if question == "hello":
            fancy_print("Hello friend.")
        elif question == "who are you":
            fancy_print("I am John, or am I the many people that pretend to be John?")
        elif "is your gospel independent" in question:
            fancy_print("There's no reason to believe that.")
            fancy_print("I clearly know of Mark, I tell the same stories in the same order.")
            fancy_print("I insert the same character in the story as Luke, Martha, Mary's sister.")
            fancy_print("And me and Luke both claim Judas was possesed by Satan.")
            fancy_print("Mark's gospel theme was that Jesus would leave no signs to the jews.")
            fancy_print("Luke's and Matthew's have the resurrection as one sign.")
            fancy_print("My gospel has all the signs!!")
        elif "sources" in question:
            fancy_print("I also used the old testament to craft my miracle stories.")
            fancy_print("Jesus' first miracle at Cana is turning water into wine.")
            fancy_print("Just like Moses in exodus, where God has him turn water into blood as a sign.")
            fancy_print(" 'If they will not believe even after these two signs, nor listen to you,\nthen you shall take some of the water from the river, "
                  "and pour it on the dry ground, \nand the water that you took out of the river shall become blood upon the ground.'")
            fancy_print("I turned the last into the first.")
        elif "historical" in question or "example" in question:
            fancy_print("There is no reason to believe I'm writing history.")
            fancy_print("I'm the most fervent propagandist of them all.")
            fancy_print("I insert the most ridiculous storylines to fit my 'giving signs' purpose.")
            fancy_print("The Doubting Thomas episode for example.")
            fancy_print("Or Lazarus, the beloved disciple.")
            fancy_print("None of the other gospels have heard of him.")
            fancy_print("There's a Lazarus mentioned in Luke I decided to make a character of my story.")
            fancy_print("I made Lazarus very relevant in my gospel, he's the one that witnesses everything, and I cite as my source.")
            fancy_print("He's so important that I turned his resurrection as the reason the Jews killed Jesus.")
            fancy_print("None of this happens in the other gospels, because it is my invention, to fit my purpose.")
        elif question == "go back":
            talk_with_luke()
        elif question == "paul":
            talk_with_paul()
        elif question == "help":
            help(dialogue)
        else:
            fancy_print("That's unknown to me.")

def talk_with_paul():
    fancy_print("You see Paul's familiar face again in the most well lit room you've ever seen, he starts talking to you:")
    fancy_print("You made it.")
    fancy_print("From the authors of the gospels you get to know a certain literary version of Jesus.")
    fancy_print("From me you'll get to know another one.")
    fancy_print("He doesn't ride donkeys and is not crucified by Pontius Pilate.")
    fancy_print("He doesn't have beloved disciples called Lazarus.")
    fancy_print("He doesn't perform miraculous healings.")
    fancy_print("No Mary, no Joseph, no Galilee, no Nazareth.")
    fancy_print("My Jesus story comes from private revelations and hidden messages in scripture.")
    fancy_print("From which of these topics do you want to start our conversation?")
    fancy_print("""
          - Hebrews;
          - Things Jesus said;
          - The Eucharist;
          - Rulers of this age;
          - Women;
          - Sperm;
          - Brothers of the lord;
    """)

    dialogue = ["hello", "Hebrews", " Things Jesus said", "The Eucharist", "Rulers of this age", "Women", "Sperm", "Brothers of the lord", "made my choice", "start (goes back to the start of the game to pick the other paths if you didn't already)"]
    answers = []

    while True:

        question = input("> ").lower()

        if question == "help":
            help(dialogue)
        elif question == "hello":
            fancy_print("Hello traveler.")
        elif "hebrews" in question:
            hebrews()
        elif "things jesus said" in question:
            things_jesus_said()
        elif "eucharist" in question:
            the_eucharist()
        elif "rulers of this age" in question:
            rulers_of_this_age()
        elif "women" in question:
            women()
        elif "sperm" in question:
            sperm()
        elif "brothers of the lord" in question:
            brothers_of_the_lord()
        elif question == "start":
            start()
        elif "made my choice" in question:
            pick_your_jesus()
        else:
            fancy_print("I have no knowledge of that.")

def hebrews():
    fancy_print("""
            For if He were on earth, He would not be a priest, since there are already priests who
        offer gifts according to the law, and who only give service to the copy and shadow of heavenly things. 
    """)

    dialogue = ["What is Hebrews?", "Who is Jesus?"]

    info_on = False

    while not info_on:
        
        question = input("> ").lower()

        if "what is hebrews" in question:
            fancy_print("It is a gospel, written before the canonical ones. The author of Hebrews assumes the temple is still operating.")
            fancy_print("""
                    The law is only a shadow of the good things that are coming—not the realities themselves. 
                For this reason it can never, by the same sacrifices repeated endlessly year after year, make perfect those who draw near to worship. 
                Otherwise, would they not have stopped being offered? For the worshipers would have been cleansed once for all, 
                and would no longer have felt guilty for their sins. But those sacrifices are an annual reminder of sins.
                It is impossible for the blood of bulls and goats to take away sins.
            """)
        elif "who is jesus" in question:
            fancy_print("Jesus the Son of God is the great high priest who has passed through the heavens.")
            fancy_print("He had to die in heaven for the blood magic of his sacrifice to work.")
            fancy_print("The sacrifices made by the priests on earth are less effective than the celestial ones, because they only serve the copies of the things in heaven.")
            fancy_print("""
                    Christ, arriving as a High Priest of the good things to come, through a greater and more perfect temple, 
                the one not made with hands (that is to say, not of [human] construction), and neither through the blood of goats
                and calves, but through his own blood, he entered into the holy place once and for all, finding eternal redemption.

                    According to the law, all things are cleansed with blood and without bloodshed no forgiveness occurs.
                And so it was necessary that the copies of the things in the heavens should be cleansed with these, 
                but the heavenly things themselves with better sacrifices than these.

                For Christ did not go into the holy place made with hands, the antitype of the true one, but into heaven itself, now to appear before the face of God on our behalf. 
                Nor does he need to present himself time and again, like the high priest does who goes into the holy place year by year with the blood of another.

                 By this testament we have been made holy through the offering of the body of Jesus Christ once and for all.
            """)

            info_on = True
        elif question == "help":
            help(dialogue)
        else:
            fancy_print("I have no knowledge of that.")

def things_jesus_said():
    fancy_print("""
            How then shall they call on him in whom they have not believed? And how shall they believe in him whom
        they have not heard? And how shall they hear without a preacher? And how shall they preach, except [a preacher] be sent?
    """)

    dialogue = ["What did Jesus say?", "What's an example?"]

    info_on = False

    while not info_on:
        
        question = input("> ").lower()

        if "what did jesus say" in question:
            fancy_print("Some might say that some things I said were the words of Jesus. Because they've been made to be that in the gospels.")
            fancy_print("But those were my own words.")
            fancy_print("And the apostles only know of the message of Jesus through scripture and revelation.")
            fancy_print("""
                    Now to him who is able to establish you in accordance with my gospel, the message I proclaim about Jesus Christ, 
                in keeping with the revelation of the mystery hidden for long ages past, but now revealed and made known through the prophetic writings by the command of the eternal God, 
                so that all the Gentiles might come to the obedience that comes from faith to the only wise God be glory forever through Jesus Christ!
            """)
        elif "example" in question:
            fancy_print("I teach the concept of the Golden Rule many times in my letters.")
            fancy_print("Declaring to love your neighbor as yourself.")
            fancy_print("But I never show any knowledge of Jesus having said this.")
            fancy_print("My only source on that is the leviticus.")
            fancy_print("""
                  Do not seek revenge or bear a grudge against anyone among your people, but love your neighbour as yourself. I am the Lord.
            """)

            info_on = True
        elif question == "help":
            help(dialogue)
        else:
            fancy_print("I have no knowledge of that.")

def the_eucharist():
    fancy_print("""
            For I received from the Lord that which I also delivered to you, that the Lord Jesus in the night in which he was delivered up took bread, 
            and having given thanks, he broke it and said, ‘This is my body, which is for your sake. Do this in remembrance of me.’ 
            Likewise also the cup after the eating, saying, ‘This cup is the new testament in my blood. Do this, as often as you drink, in remembrance of me.’ 
            For as often as you eat this bread, and drink the cup, you proclaim the Lord’s death until he comes.
    """)

    dialogue = ["How did Mark change this?"]

    info_on = False

    while not info_on:
        
        question = input("> ").lower()

        if "how did mark change this" in question:
            fancy_print("He used this text as a base in which he inserted his characters.")
            fancy_print("""
                     While they were eating, Jesus took bread, and when he had given thanks, he broke it and gave it to his disciples, saying, “Take it; this is my body.”
                     Then he took a cup, and when he had given thanks, he gave it to them, and they all drank from it.
                     “This is my blood of the covenant, which is poured out for many,” he said to them. 
            """)
            fancy_print("I didn't speak of this as if I was present or as if someone who was told me about it.")
            fancy_print("I explicitly say this I received from the Lord (in revelation).")
            
            info_on = True
        elif question == "help":
            help(dialogue)
        else:
            fancy_print("I have no knowledge of that.")

def rulers_of_this_age():
    fancy_print("""
            We speak a wisdom among the mature (the fully initiated), a wisdom not of this age, nor of the rulers of this age (archontōn tou aiōnos toutou), 
        who are being abolished, but we speak God’s wisdom, in a mystery, that has been hidden, which God foreordained before the ages (aiōnōn) for our glory, 
        which none of the rulers of this age (archontōn tou aiōnos toutou) had known. For if they had known it, they would not have crucified the Lord of Glory. 
        But as it is written, ‘Things which eye saw not, and ear heard not, and which entered not into the heart of a man, those things God prepared for those who love him’. 
    """)

    dialogue = ["Who are the rulers of this age?", "Words Paul didn't say"]

    info_on = False

    while not info_on:
        
        question = input("> ").lower()

        if "who are the rulers of this age" in question:
            fancy_print("In the passage above it is mentioned that they are the ones that killed Jesus.")
            fancy_print("The passage says that if they knew the plan of God, they wouldn't have killed him.")
            fancy_print("How can the archons of this age be the Romans or the Jewish elite?")
            fancy_print("Am I wprried about them not wanting to cleanse the sins of all humanity? They either wouldn't have cared if they knew, or went on with it to see if it would have saved all.")
            fancy_print("The archons of this age are Satan and his demons, if they knew that their killing Jesus would save all in God's plan, they wouldn't have done it.")
            fancy_print("He also says that these rulers are being abolished, the Romans and the Jewish elite were not abolished, and could still be saved by joining Christ.")
            
            info_on = True
        elif "words paul didn't say" in question:
            fancy_print("""
                    For you, brethren, became imitators of the churches of God which are in Judaea in Jesus Christ, 
                for you also suffered the same things from your own countrymen as they did from the Jews who both killed the Lord Jesus and the prophets, 
                and drove us out, and pleased not God, and are contrary to all men, forbidding us to speak to the Gentiles that they may be saved, 
                to fill up their sins for evermore—but the wrath has come upon them to the uttermost.
            """)
            fancy_print("Here someone tried to make me say that Jesus was killed by the Jews, but it is a clear fabrication.")
            fancy_print("What makes it clear is that I imply here my knowledge of the calamity that befell the jews (the destruction of the temple).")
            fancy_print("But I was probably already dead and gone when that happened.")
            fancy_print("I speak of myself as a Jew, and I consider them part of my own church. I would never damn them this way")
            fancy_print("""
                    ‘Did God cast off his people? God forbid! For I also am a Jew, of the seed of Abraham, of the tribe of Benjamin’

                    ‘Are they Hebrews? So am I. Are they Israelites? So am I. Are they the seed of Abraham? So am I’
            """)
        elif question == "help":
            help(dialogue)
        else:
            fancy_print("I have no knowledge of that.")

def women():
    fancy_print("""
            If you are Christ’s, then you [like him] are the sperm of Abraham, heirs according to the promise.
        And I say that as long as the heir is a child, he’s no different from a slave. Even though he is lord of all, he is under guardians and stewards until [the day] the father has foreordained.
        And we, too, were enslaved under the elements of the universe when we were children. 
        But when the fullness of time came, God sent his son, made from a woman, made under the law, in order to rescue those under the law, in order that we might receive adoption as sons. 
        And because you are sons, God has sent the spirit of his Son into our hearts, crying ‘Abba, father!’ As a result, you are no longer a slave, but a son; and if a son, then also an heir by God.
    """)

    dialogue = ["What does made from a woman mean?"]

    info_on = False

    while not info_on:
        
        question = input("> ").lower()

        if "made from a woman" in question:
            fancy_print("""
                    For it is written, Abraham had two sons, one from a slave woman and one from a free woman,
                but the one from the slave woman was born according to the flesh, and the one from the free woman by the promise.
                Which things are said allegorically, for these [women] are the two testaments, the first being the one from Mount Sinai, which gives birth to slavery. 
                That’s Hagar—Hagar meaning Mount Sinai in Arabia, which corresponds to Jerusalem now, for she is enslaved with her children. 
                But the Jerusalem above is free, and she is our mother.
            """)
            fancy_print("I'm talking here about allegorical women. There's two Jerusalems, one is on earth, and it's enslaved, the other is in Heaven, and it's free.")
            fancy_print("Jesus was momentarily born of Hagar, the Torah law that has power on earthly Jerusalem.")
            fancy_print("With his death he killed that law, making it possible for us to be born of the free woman: God's heavenly kingdom.")
            fancy_print("""
                    So now, [my] brothers, we are the children of the promise, like Isaac [the son of the free woman, Sarah].
                But as in those days the one born according to the flesh [Ishmael] persecuted the one according to the spirit [Isaac], so it is now. 
                But what does the scripture say? Cast out the slave girl and her son, for the son of the slave girl will not be heir with the son of the free woman. 
                Accordingly, [my] brothers, we are not children of the slave woman, but of the free one. For freedom did Christ set us free.
            """)
            
            info_on = True
        elif question == "help":
            help(dialogue)
        else:
            fancy_print("I have no knowledge of that.")

def sperm():
    fancy_print("""
            Paul, a servant of Jesus Christ, called to be an apostle, separated unto the gospel of God,
        Concerning his Son Jesus Christ our Lord, which was made of the seed of David according to the flesh;
        And declared to be the Son of God with power, according to the spirit of holiness, by the resurrection from the dead:
        By whom we have received grace and apostleship, for obedience to the faith among all nations[...]
    """)

    dialogue = ["What does it mean that he was made from the seed of David?", "Cosmic sperm bank?"]

    info_on = False

    while not info_on:
        
        question = input("> ").lower()

        if "seed of david" in question:
            fancy_print("In the passage above I use the word 'genomenos' to describe how Jesus came into being.")
            fancy_print("It's the same word I use to describe Adam's creation by God.")
            fancy_print("And it's the same word I use to describe our future resurrection body.")
            fancy_print("My preferred word used for natural birth is 'gennao'.")
            fancy_print("So how did God get the seed of David to manifacture Jesus's body?")
            fancy_print("He got it from the cosmic sperm bank of course!")
        elif 'cosmic sperm bank' in question:
            fancy_print("""
                    When your days are done, and you sleep with your fathers, I will raise up your sperm after you, 
                which shall come from your belly, and I will establish his kingdom. He will build for me a house in my name, 
                and I will establish his throne forever. I will be his father, and he will be my son.
            """)
            fancy_print("This passage's original poetic intent is probably to describe an unending royal line.")
            fancy_print("But read literally with pesher logic it could be interpreted as God saving up David's sperm until the time to keep his promise of an eternal line came.")
            fancy_print("All sorts of things could be stored in heaven, even our own future bodies, even sperm.")

            info_on = True
        elif question == "help":
            help(dialogue)
        else:
            fancy_print("I have no knowledge of that.")

def brothers_of_the_lord():
    fancy_print("""
            Am I not free? Am I not an apostle? Have I not seen Jesus our Lord? Are you not my work in the Lord? 
        If I am not an apostle to others, at least I am to you. For you are my seal of apostleship in the Lord. My defense to those who are putting me on trial is this: 
        Do we not have the right to eat and drink? Do we not have the right to take along with us a sister as a wife, as also the other apostles and the brothers of the Lord and Cephas do? 
        Or is it only Barnabas and I who have no right to give up working for our keep? 
    """)

    dialogue = ["Who are the brothers of the lord?", "James"]

    info_on = False

    while not info_on:
        
        question = input("> ").lower()

        if "brothers of the lord" in question:
            fancy_print("In the passage above I mention them in contrast to the apostles and Cephas.")
            fancy_print("I'm talking about me and Barnabas being singled out and having to work for our meals.")
            fancy_print("Also not being able to bring a 'sister of the lord' with us for said meals without us or them having to work.")
            fancy_print("So I clearly refer to 'brothers of the Lord' not as a privileged category that is the family of Jesus, but as all other Christians.")
            fancy_print("It's a cultic title.")
        elif "james" in question:
            fancy_print("""
                    When it was the good pleasure of the God who separated me from my mother’s womb, and called me through his grace, to reveal his Son in me, 
                    that I might preach him among the Gentiles, I did not confer with flesh and blood right away, nor did I go to Jerusalem to those that were apostles before me, 
                    but I went to Arabia and again I returned to Damascus. Then after three years I went to Jerusalem, to consult with Cephas, and I stayed with him for fifteen days, 
                    but I did not see any other of the apostles, except James the brother of the Lord. And look, these things I’m writing to you, by God, I’m not lying! 
                    Then I went into the regions of Syria and Cilicia. And I was still unknown by face to the congregations of Judea that were in Christ.
            """)
            fancy_print("Here I'm talking about how after I had my first revelation I didn't talk to any other apostle in person for years.")
            fancy_print("Finally I decided to go to Jerusalem to consult Cephas, but I didn't see any other apostles.")
            fancy_print("The James I met was 'the brother of the Lord' in the sense that he was just a regular 'Christian' (a name I never use).")
            fancy_print("I phrased it as 'other than the apostles I saw only James' (heteron tōn apostolōn)")

            info_on = True
        elif question == "help":
            help(dialogue)
        else:
            fancy_print("I have no knowledge of that.")

def jesus_not_here_room():
    fancy_print("Jesus is not here!!")
    fancy_print("But you do find the credits for this game.")
    fancy_print("Credits to 'On the historicity of Jesus' by Richard Carrier.")
    fancy_print("""And all those little rascal authors of ancient Christianity,
    that made all of this possible.""")

    choice = input("Do you want to go back to the start?\n> ").lower()

    if choice == "yes":
        start()
    elif choice == "no":
        fancy_print("Hope to see you again friend.")
        exit(0)
    else:
        dead("Mythical Jesus spears you from outer space with the sword of justice.")

def pick_your_jesus():
    fancy_print("You find yourself in a room with two statues")
    fancy_print("In one Jesus is portrayed like an angel")
    fancy_print("In the other he is portrayed like a man.")
    fancy_print("Which one do you pick?")

    choice = input("> ").lower()

    if "angel" in choice and not "man" in choice:
        gold_room()
    elif "man" in choice and not "angel" in choice:
        silver_room()
    else:
        dead("Jesus urged you to make a choice with his angel sword.")

def gold_room():
    fancy_print("You believe that Jesus was a mythical entity.")
    fancy_print("Crucified in a level of heaven by demons.")
    fancy_print("You win 1000 pieces of gold.")
    exit(0)

def silver_room():
    fancy_print("You believe that Jesus was a historical man.")
    fancy_print("Crucified by Romans on earth.")
    fancy_print("You win 100 pieces of gold.")
    exit(0)

def help(questions):
    fancy_print(f"{questions}")

def dead(reason):
    fancy_print(reason)
    fancy_print("You died.")
    exit(0)

def fancy_print(string):
    for char in string:
        print(char, end="", flush = True)
        sleep(.03)
    print(end = "\n")

start()