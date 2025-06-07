import time
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