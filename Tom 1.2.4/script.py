#Tom assistant for Windows, if you run this script on linux or mac, some color features wont work...
import tomodules
import datetime
import webbrowser
import os
import sys
import time
from math import pi

tomodules.clear_terminal()
version_name = "v1.2.4"
if os.name =="nt": 
    os.system("color 0A")
else:
    pass
    
print(f"{version_name} uploaded by the official github project owner.\n")
tomodules.banner()

print("\n       Welcome, I'm Tom, your artificial assistant !")

###############################################################

def callback():
    input("\nPress Enter to continue...\n")
    tomodules.clear_terminal()
    main()

def math_callback():
    input("\nPress Enter to continue...\n")
    tomodules.clear_terminal()
    math_selector()
    common_callback()

def common_callback():
    input("\nPress Enter to continue...\n")
    tomodules.clear_terminal()
    common_selector()

###############################################################  ________
###########################   Quiz   ##########################          |
###############################################################          V

def quiz():
    quiz_score = 0
    q1 = input("Who is my creator ?\n1- Daniel Falcov\n2- Jack Rayan\n3- Daniel Falkov\n>> ")
    if q1 == '1' or q1 == '2' or q1 == '3':
        if q1 == '3':
            quiz_score = quiz_score + 1
            print("Correct answer !")
        else:
            print("Wrong answer...")
    else:
        print("\n[x] ERROR: please select an answer between 1, 2 or 3.\n")
        quiz()
    q2 = input("\nWhat's my name ?\n1- Tom\n2- Tommy\n3- Alex\n>> ")
    if q2 == '1' or q2 == '2' or q2 == '3':
        if q2 == '1':
            quiz_score = quiz_score + 1
            print("Correct answer !")
        else:
            print("Wrong answer...")
    else:
        print("\n[x] ERROR: please select an answer between 1, 2 or 3.\n")
        quiz()
    q3 = input("\nWhere can you find the source code of this program ?\n1- Twitter\n2- Reddit\n3- Github\n>> ")
    if q3 == '1' or q3 == '2' or q3 == '3':
        if q3 == '3':
            quiz_score = quiz_score + 1
            print("Correct answer !")
        else:
            print("Wrong answer...")
    else:
        print("\n[x] ERROR: please select an answer between 1, 2 or 3.\n")
        quiz()
    q4 = input("\nIn witch language was I first coded ?\n1- Russian\n2- French\n3- English\n>> ")
    if q4 == '1' or q4 == '2' or q4 == '3':
        if q4 == '2':
            quiz_score = quiz_score + 1
            print("Correct answer !")
        else:
            print("Wrong answer...")
    else:
        print("\n[x] ERROR: please select an answer between 1, 2 or 3.\n")
        quiz()
    q5 = input("\nDo you know what was my first name ?\n1- Richard\n2- Alex\n3- Robert\n>> ")
    if q5 == '1' or q5 == '2' or q5 == '3':
        if q5 == '2':
            quiz_score = quiz_score + 1
            print("Correct answer !")
        else:
            print("Wrong answer...")
    else:
        print("\n[x] ERROR: please select an answer between 1, 2 or 3.\n")
        quiz()

    print(f"\nEnd of the quiz !\nYour score is: {quiz_score}/5.")
    rate = quiz_score * 20
    print(f"You successfully answered to {rate}% of the questions.")
    chat()

###############################################################  ________
######################   Math test   ##########################          |
###############################################################          V

def math_test():
    tomodules.clear_terminal()
    test_score = 0
#####
    q1 = input("What is the result of 4 * 15 ?\n>> ")
    if float(q1) == 4*15:
        print("Correct answer !")
        test_score = test_score + 1
    else:
        print("Wrong answer...")
#####
    q2 = input("\nWhat is the result of 6 * 0.5 ?\n>> ")
    if float(q2) == 6*0.5:
        print("Correct answer !")
        test_score = test_score + 1
    else:
        print("Wrong answer...")
#####        
    q3 = input("\nWhat is the result of 9 * 7 ?\n>> ")
    if float(q3) == 9*7:
        print("Correct answer !")
        test_score = test_score + 1
    else:
        print("Wrong answer...")
#####
    q4 = input("\nWhat is the result of 5 * 250 ?\n>> ")
    if float(q4) == 5*250:
        print("Correct answer !")
        test_score = test_score + 1
    else:
        print("Wrong answer...")
#####
    q5 = input("\nWhat is the result of 7 * 50 ?\n>> ")
    if float(q5) == 7*50:
        print("Correct answer !")
        test_score = test_score + 1
    else:
        print("Wrong answer...")
#####        
    q6 = input("\nWhat is the result of 9 * 20 ?\n>> ")
    if float(q6) == 9*20:
        print("Correct answer !")
        test_score = test_score + 1
    else:
        print("Wrong answer...")
#####
    q7 = input("\nWhat is the result of 3 * 650 ?\n>> ")
    if float(q7) == 3*650:
        print("Correct answer !")
        test_score = test_score + 1
    else:
        print("Wrong answer...")
#####    
    q8 = input("\nWhat is the result of 7 - 80 ?\n>> ")
    if float(q8) == 7-80:
        print("Correct answer !")
        test_score = test_score + 1
    else:
        print("Wrong answer...")
#####    
    q9 = input("\nWhat is the result of 368 + 120 ?\n>> ")
    if float(q9) == 368+120:
        print("Correct answer !")
        test_score = test_score + 1
    else:
        print("Wrong answer...")
#####
    q10 = input("\nWhat is the result of 150 + 2 + 3 + 5 - 5 ?\n>> ")
    if float(q10) == 150+2+3+5-5:
        print("Correct answer !")
        test_score = test_score + 1
    else:
        print("Wrong answer...")

    print(f"\nEnd of the test !\nYour score is: {test_score}/10.")
    rate = test_score * 10
    print(f"You successfully answered to {rate}% of the questions.")


###############################################################  ________
######################   Chat with Tom   ######################          |
###############################################################          V

def chat():
    entry = input("\n\n>> ")
    if entry == "hi" or entry == "hello" or entry == "Hi" or entry == "Hi!" or entry == "Hello" or entry == "Hello!":
        print("Hello, how can I help you ?")
        chat()
    elif entry == "What's your name ?" or entry == "What is your name ?" or entry == "what is your name ?" or entry == "what is your name?" or entry == "what is your name" or entry == "What's your name?" or entry == "What's your name" or entry == "What is your name?" or entry == "What is your name" or entry == "what's your name" or entry == "what's your name?" or entry == "what's your name ?":
        print("My name is Tom, and I'm your assistant !")
        chat()
    elif entry == "Who's your creator ?" or entry == "Who's your creator?" or entry == "Who is your creator ?" or entry == "Who is your creator" or entry == "who is your creator ?" or entry == "who is your creator?" or entry == "who is your creator":
        print("My creator is Daniel Falkov, you can find his Github in the main menu.")
        chat()
    elif entry == "Can I call you Tommy ?" or entry == "Can I call you Tommy?" or entry == "Can I call you Tommy" or entry == "can I call you Tommy ?" or entry == "can I call you Tommy?" or entry == "can I call you Tommy" or entry == "can I call you tommy ?" or entry == "can I call you tommy?" or entry == "can I call you tommy" or entry == "can i call you tommy ?" or entry == "can i call you tommy?" or entry == "can i call you tommy":
        print("Sorry, but my creator already gived me a name.")
        chat()
    elif entry == "clear" or entry == "clear terminal" or entry == "clear the terminal":
        tomodules.clear_terminal()
        chat()
    elif entry == "Tell me more about yourself." or entry == "tell me more about yourself":
        print("""Well, I'm just an artificial assistant with scientific purpose.
I'm quite young : I was born on the 14th december 2020...
            """)
        chat()
    elif entry == "When is your Birthday ?" or entry == "When is your Birthday?" or entry == "When is your Birthday" or entry == "when is your birthday ?" or entry == "when is your birthday?" or entry == "when is your birthday":
        print("I was born on the 14th december 2020.")
        chat()
    elif entry == "How are you ?" or entry == "How are you?" or entry == "How are you" or entry == "how are you ?" or entry == "how are you?" or entry == "how are you" or entry == "How are you going ?":
        print("I'm fine !")
        chat()
    elif entry == "Do you like mushrooms ?" or entry == "do you like mushrooms ?":
        print("You have seen the screenshots of the github ?  ;)")
        chat()
    elif entry == "quiz" or entry == "quiz time":
        tomodules.clear_terminal()
        quiz()
    elif entry == "play a game" or entry =="game" or entry == "Can I play with you ?" or entry == "Can I play a game ?" or entry == "I want to play !" or entry == "Can I play ?":
        webbrowser.open_new("https://agar.io/")
        chat()
    elif entry == "math test" or entry == "math":
        math_test()
        chat()
    elif entry == "quit" or entry == "exit" or entry == "back" or entry == "Quit" or entry == "Exit" or entry == "Back":
        tomodules.clear_terminal()
        common_selector()
    else:
        print("It looks like there is a bug in the Matrix...")
        chat()

###############################################################  ________
#####################   Module selector   #####################          |
###############################################################          V
def common_selector():
    start = input("""

                            > Common modules <

        +-------------------------------------------------------+ 
        |      1- display banner                                |
        +-------------------------------------------------------+
        |      2- display the date and the time                 |
        +-------------------------------------------------------+
        |      3- credits                                       |
        +-------------------------------------------------------+
        |      4- Github                                        |
        +-------------------------------------------------------+
        |      5- Chat with Tom (beta)                          |
        +-------------------------------------------------------+
        |      6- Help                                          |
        +-------------------------------------------------------+
        |      99- Back                                         |
        +-------------------------------------------------------+
\n      Select: 
        """)
    if start == '1':
        tomodules.clear_terminal()
        tomodules.banner()
        common_selector()
    elif start == '2':
        tomodules.clear_terminal()
        tomodules.get_datetime()
        common_callback()
    elif start == '3':
        tomodules.clear_terminal()
        tomodules.credits()
        common_callback()
    elif start == '4':
        tomodules.clear_terminal()
        tomodules.github()
        common_callback()
    elif start == '5':
        tomodules.clear_terminal()
        print("You are now chatting with Tom...")
        chat()
    elif start == '6':
        webbrowser.open_new("https://github.com/Dan149/Tom-assistant/wiki/")
        common_callback()
    elif start == '99':
        tomodules.clear_terminal()
        main()
    else:
        print("\n[x] ERROR: module or selector not found.")
        common_callback()

def math_selector():
    start = input("""

                            > Maths modules <

        +-------------------------------------------------------+
        |      1- convert a number in scientific number         |
        +-------------------------------------------------------+
        |      2- calculate feeled temperature                  |
        +-------------------------------------------------------+
        |      3- convert °F --> °C                             |
        +-------------------------------------------------------+
        |      4- convert °C --> °F                             |
        +-------------------------------------------------------+
        |      5- calculate a circle's circumference            |
        +-------------------------------------------------------+
        |      6- calculate an average                          |
        +-------------------------------------------------------+
        |      99- Back                                         |
        +-------------------------------------------------------+
\n      Select: 
        """)
    if start == '1':
        tomodules.clear_terminal()
        tomodules.get_sci_number()
        math_callback()
    elif start == '2':
        tomodules.clear_terminal()
        tomodules.get_ftemp()
        math_callback()
    elif start == '3':
        tomodules.clear_terminal()
        tomodules.fahrenheit_to_celsius()
        math_callback()
    elif start == '4':
        tomodules.clear_terminal()
        tomodules.celsius_to_fahrenheit()
        math_callback()
    elif start == '5':
        tomodules.clear_terminal()
        tomodules.get_circle_circumference()
        math_callback()
    elif start == '6':
        tomodules.clear_terminal()
        tomodules.get_average()
        math_callback()
    elif start == '99':
        tomodules.clear_terminal()
        main()
    else:
        print("\n[x] ERROR: module or selector not found.")
        math_callback()

def main():
    start = input("""
                    > MENU <

        +-----------------------------+
        |      1- Math modules        |
        +-----------------------------+
        |      2- Common modules      |
        +-----------------------------+
        |      99- Quit               |
        +-----------------------------+
\n      Select: 
    """)
    if start == '1':
        tomodules.clear_terminal()
        math_selector()
    elif start == '2':
        tomodules.clear_terminal()
        common_selector()
    elif start == '99':
        tomodules.clear_terminal()
        print("         \nQUITTING...")
        time.sleep(1.5)
        quit()

    else:
        print("\n[x] ERROR: module or option not found.")
        callback()
        main()
main()