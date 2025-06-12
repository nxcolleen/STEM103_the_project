import time
# I had to import the time here, it was giving errors without.
# I haven't figured out another way to fix such badness without importing the time.

# chicken

# This is my typing function, isn't it just the most fun thing in here?
def typing_function(statement1, statement2, type_to_go):
    stuck = True
    while stuck:
        print(statement1)
        time.sleep(3)
        print(statement2)
        time.sleep(5)
        typing_action = input("Type '" + (type_to_go) + "' to execute the action. ")
        time.sleep(5)
        if typing_action == (type_to_go):
            print("The action has been completed successfully,")
            time.sleep(3)
            stuck = False
            return
        else:
            print("Failure to execute the action, incorrect typing.")
            time.sleep(3)

# The battling function, which is like a quiz!
def quiz_function(statement1, options, win_option, statement_win, statement_lose):
    quizzing = True
    print(statement1)
    time.sleep(2)
    print("It's time for you to get ready,")
    while quizzing:
        time.sleep(5)
        print("Pick an option!")
        print(options)
        option_pick = input("Type 1 for the first one, 2 for the second, or 3 for the third! ")
        time.sleep(2)
        if option_pick == win_option:
            print("The decision was successful!")
            time.sleep(2)
            print(statement_win)
            quizzing = False
            time.sleep(3)
        else:
            print("Failure! Unsuccessful choice,")
            time.sleep(2)
            print(statement_lose)

# This function runs the whole game. Isn't that incredible?
# Input 'skip' in the first input to access Skipping Terminal
def the_game():
    startup = True
    chapter1 = True
    chapter2 = True
    number_picking1 = True
    number_picking2 = True
    subtracting = False
    multiplying = False
    chapter3 = True
    check_skip = input("Type something to start the program. ")
    if check_skip == "skip":
        skipping = True
        print("--- Skipping Terminal ---")
        while skipping:
            print("Input the value associated with the section to skip it,")
            print("or input anything else to exit the terminal.")
            skip_pick = input("startup: 0, chapter1: 1, chapter2: 2, chapter3: 3 ")
            if skip_pick == "0":
                startup = False
            elif skip_pick == "1":
                chapter1 = False
            elif skip_pick == "2":
                chapter2 = False
            elif skip_pick == "3":
                chapter3 = False
            else:
                skipping = False

# First Chunk of Code, startup
    while startup:
        print()
        print("It's time for some fun! Hehehheheh,")
        time.sleep(2)
        print("Did you know this thing's name is the Annoying Game?")
        time.sleep(5)
        print("That's right,")
        input("Ready to begin? ")
        begin = input("Type 'Oh yes, I am indeed ready to begin the fun!' to start ")
        if begin == "Oh yes, I am indeed ready to begin the fun!":
            print("Great to hear! Let's begin.")
            startup = False
        else:
            print("How dare you deny the fun. I can't allow you not to have it,")
            time.sleep(6)

# Chapter 1
    while chapter1:
        print()
        time.sleep(5)
        print("It's time for an adventure!")
        print("Pick where you want to go,")
        location = input("Pothole Feilds, Desert of Slime, or the Lands of No No. ")
        typing_function("Yay! Time to go to " + location + "!",
         "You're going to have to walk there,", "Walky walky walky, I'm walking!")
        print("Yay! You walked quite a long way, but you haven't quite made it there yet!")
        time.sleep(5)
        quiz_function("Wall blocks the way!", "Punch, Kick, Jump", "3", "Wall was defeated!",
         "Wall laughs at your patheticness,")
        print("You've finally made it! That's amazing!")
        time.sleep(5)
        typing_function("Yay! We need to clap to celebrate your greatness,",
         "It's time to clap!", "Clap clap clap clap clap! Clappy clap clap.")
        time.sleep(2)
        print("Incredible.")
        time.sleep(3)
        input("What might it be that you wish to do now? ")
        certainty = input("Type 'Yes! That's exactly what I want to do!' to be certain about it. ")
        if certainty == "Yes! That's exactly what I want to do!":
            print("Great to hear! Let's continue.")
            chapter1 = False
        else:
            print("That's quite enough! Why can't you just be sure about something?")
            time.sleep(3)
            print("So very annoying, in fact, you're going to have to make your way all the way back here now!")

# Chapter 2
    while chapter2:
        print()
        while number_picking1:
            time.sleep(3)
            print("I think we should do some math together.")
            try:
                number_pick1 = int(input("Pick a number so we can play with it. "))
                print(f"Ah yes, {number_pick1}, that's a great number for us to enjoy!")
                number_picking1 = False
            except ValueError:
                print("No no no! I said to put in a number! Go again, fatty.")
        while number_picking2:
            time.sleep(3)
            print("Hm, we need another number.")
            try:
                number_pick2 = int(input("Pick another number. "))
                time.sleep(2)
                print("That's amazing!")
                time.sleep(3)
                print(f"{number_pick2}, very nice decisions from you today!")
                number_picking2 = False
            except ValueError:
                print("What is going on with you today? Put in a number!")
            time.sleep(3)
            print("Pick what we should do with the two numbers.")
            math_pick1 = input("'subtract' or 'multiply' ")
            if math_pick1 == "subtract":
                subtracting = True
            elif math_pick1 == "multiply":
                multiplying = True
            time.sleep(3)
            input("Do you also want to do the other option? ")
            math_pick2 = input("Input 'Y' for Yes. ")
            if math_pick2 == "Y":
                subtracting = True
                multiplying = True
            if subtracting:
                print(number_pick1 - number_pick2)
                print(number_pick2 - number_pick1)
            if multiplying:
                print(number_pick1 * number_pick2)
            time.sleep(5)
            print("There you go! Your numbers, and look what they became! Very nice, and fun!")
            time.sleep(5)
            chapter2 = False

# Chapter 3
    while chapter3:
        print(); time.sleep(3)
        input("Having fun today? ")
        print("Well I certainly hope you are!"); time.sleep(3)
        input("I think we should visit the Pothole Fields, don't you? ")
        print("Heheheheh! Let's get going!"); time.sleep(5)
        print("Uh oh, there's a little weirdo coming over here!")
        quiz_function("Little Weirdo attacks!", "Slap, Sniff, Gobble", "1", "Little Weirdo ran away!",
         "Little Weirdo touches you with its scary looking carrot fingers, and makes you feel quite uncomfortable!")
        time.sleep(3)
        print("Excellent work, the way you handled that little freak,"); time.sleep(2)
        print("That's amazing!"); time.sleep(3)
        print("More little weirdos incoming!"); time.sleep(3)
        print("You'd better jump over that hole, I don't think you're going to be able to defeat that many of them.")
        typing_function("Get ready to jump!", "",
         "I can jump, and this jump will be the biggest jump I have ever done in all of the jumps I have done.")
        time.sleep(3); print("That's amazing!"); time.sleep(3)
        print("Pick which way to escape fom the freaks, type exactly which option,")
        escape_pick1 = input("'Left', 'Straight', 'Right' ")
        if escape_pick1 == "Left":
            print("No! There's an army of them!"); time.sleep(3)
            print("They're turning you into a weirdo,"); time.sleep(3)
            print("The only way to be saved, is to restart back to when we finished doing our math!")
            time.sleep(3); print("I apologize, but this is the only way."); time.sleep(3)
        elif escape_pick1 == "Straight":
            typing_function("Ahhhh! Fallen into a pot hole!", "You're going to have to dig your way out, quickly!",
             "Dig dig dig, oh, I'm digging my way out of here!")
            chapter3 = False
        else:
            print("Let's go right!"); time.sleep(3)
            quiz_function("Another little weirdo, It's in the way!", "Poke, Kick In The Mouth, Snort", "2",
             "The freak fell into a pot hole!", "The freak bites you in the ankle, ouch!")
            chapter3 = False

# ending
    print(); time.sleep(3); print("Excellent work, those little weirdos are gone!"); time.sleep(3)
    print("I guess we'd better get out of the Pothole Fields, I hadn't known of these dangers.")
    typing_function("Let's get out of here.",
     "Time for walking again,", "Walky walky walky, I'm walking!")
    print("Well, we're finally out of there."); time.sleep(2)
    print("I guess that's it for now,"); time.sleep(3)
    print("Goodbye, my favorite enjoyer of fun."); time.sleep(3)
    print("I am unsure if we'll be seeing each other again."); time.sleep(3)
    input("Type something to end my program. ")