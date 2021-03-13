import tomodules
import datetime
import webbrowser
import os
import sys
import time
from math import pi

def clear_terminal():
    if os.name =="nt": 
        os.system("cls")
    else:
        os.system("clear")

def banner():
    time.sleep(3)
    clear_terminal()
    if os.name =="nt": 
        os.system("color 01")
    else:
        pass
    print("\n\n          TTTTTTTTTTTTTTTTTTTTTTT                                      ")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 02")
    else:
        pass
    print("          T:::::::::::::::::::::T                                      ")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 03")
    else:
        pass
    print("          T:::::::::::::::::::::T                                      ")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 04")
    else:
        pass
    print("          T:::::TT:::::::TT:::::T                                      ")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 05")
    else:
        pass
    print("          TTTTTT  T:::::T  TTTTTTooooooooooo      mmmmmmm    mmmmmmm   ")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 06")
    else:
        pass
    print("                  T:::::T      oo:::::::::::oo  mm:::::::m  m:::::::mm ")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 07")
    else:
        pass
    print("                  T:::::T     o:::::::::::::::om::::::::::mm::::::::::m")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 08")
    else:
        pass
    print("                  T:::::T     o:::::ooooo:::::om::::::::::::::::::::::m")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 09")
    else:
        pass
    print("                  T:::::T     o::::o     o::::om:::::mmm::::::mmm:::::m")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 0B")
    else:
        pass
    print("                  T:::::T     o::::o     o::::om::::m   m::::m   m::::m")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 0C")
    else:
        pass
    print("                  T:::::T     o::::o     o::::om::::m   m::::m   m::::m")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 0D")
    else:
        pass
    print("                  T:::::T     o::::o     o::::om::::m   m::::m   m::::m")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 0E")
    else:
        pass
    print("                TT:::::::TT   o:::::ooooo:::::om::::m   m::::m   m::::m")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 01")
    else:
        pass
    print("                T:::::::::T   o:::::::::::::::om::::m   m::::m   m::::m")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 02")
    else:
        pass
    print("                T:::::::::T    oo:::::::::::oo m::::m   m::::m   m::::m")
    time.sleep(0.1)
    if os.name =="nt": 
        os.system("color 03")
    else:
        pass
    print("                TTTTTTTTTTT      ooooooooooo   mmmmmm   mmmmmm   mmmmmm")
    time.sleep(0.2)
    if os.name =="nt": 
        os.system("color 0F")
    else:
        pass
    input("\n\n\n\nPress Enter to continue...")
    clear_terminal()

#############################################################################

def get_average():
    num_list = []
    enter_num_str = input("\nenter a number: ")
    enter_num = float(enter_num_str)
    num_list.append(enter_num)
    another = input("\nadd another one ? [yes/no] ")
    if another == "yes" or another == "y" or another == "Y" or another == "Yes" or another == "no" or another == "n" or another == "N" or another == "No":   
        while (another == "yes" or another == "y" or another == "Y" or another == "Yes"):
            enter_num_str = input("\nenter a number: ")
            enter_num = float(enter_num_str)
            num_list.append(enter_num)
            another = input("\nadd another one ? [yes/no] ")
    else:
        print("[x] ERROR: Wrong option")
        get_average()
    average = sum(num_list) / len(num_list)
    print(f"\naverage: {average}")
    
def get_circle_circumference():
    mesure_unit = input("\nmesuring unit (cm, m...): ")
    circle_radius_str = input(f"circle radius in {mesure_unit}: ")
    circle_radius = float(circle_radius_str)
    circumf = 2 * pi * circle_radius
    print(f"\ncircumference of the circle: {circumf} {mesure_unit}")

def get_sci_number():
    number_str = input("\nEnter the number you want to convert in scientific number: ")
    number = float(number_str)
    exponent = 0
    if (number < 1):
        while (number < 1): 
            number = number * 10 
            exponent = exponent - 1
    if (number > 1):
        while (number > 10):
            number = number / 10
            exponent = exponent + 1
    print(f"\n{number} x 1O exponent : {exponent}.")
    
def get_ftemp():
    wind_speed_str = input("\nwind speed in km/h: ")
    temp_str = input("\nreal temperature Celsius: ")
    wind_speed = float(wind_speed_str)
    temp = float(temp_str)
    ftemp_equation = 13.12 + 0.6215 * temp + (0.3965 * temp - 11.37) * pow(wind_speed, 0.16)
    print(f"\nThe feeled temperature is: {ftemp_equation}")
    
def fahrenheit_to_celsius():
    tf_str = input("\nTemperature in Fahrenheit: ")
    tf = float(tf_str)
    tmp_celsius = (tf - 32) / 1.8
    print(f"\nthe result of the conversion °F --> °C is: {tmp_celsius}")

def celsius_to_fahrenheit():
    tc_str = input("\nTemperature in Celsius: ")
    tc = float(tc_str)
    tmp_fahrenheit = 1.8 * tc + 32
    print(f"\nthe result of the conversion °C --> °F is: {tmp_fahrenheit}")

##############################################################################

def github():
    webbrowser.open_new("https://github.com/Dan149/Tom-assistant")

def credits():
    clear_terminal()
    print("""
                +-----------------------------------+
                |     Created by: Falkov Daniel     |
                +-----------------------------------+
                |     MIT license, free to use.     |
                +-----------------------------------+
""")  
    time.sleep(2)
    print("""   
             +-----------------------------------------+
             |   Thanks to the Excomptix team:         |
             |                                         |
             |   http://www.excomptix.byethost24.com   |
             +-----------------------------------------+

""")      
    time.sleep(2)

def get_datetime():
    print('\nDate & time: {}'.format(datetime.datetime.now()))


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
    clear_terminal()
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
    if entry == "hi" or entry == "hello" or entry == "Hi" or entry == "Hi!" or entry == "Hello" or entry == "Hello!" or entry == "Howdy!" or entry == "Howdy" or entry == "howdy":
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
        clear_terminal()
        chat()
    elif entry == "Tell me more about yourself." or entry == "tell me more about yourself":
        print("Well, I'm just an artificial assistant...")
        chat()
    elif entry == "How are you ?" or entry == "How are you?" or entry == "How are you" or entry == "how are you ?" or entry == "how are you?" or entry == "how are you" or entry == "How are you going ?":
        print("I'm fine !")
        chat()
    elif entry == "Do you like mushrooms ?" or entry == "do you like mushrooms ?":
        print("You have seen the screenshots of the github ?  ;)")
        chat()
    elif entry == "quiz" or entry == "quiz time":
        clear_terminal()
        quiz()
    elif entry == "play a game" or entry =="game" or entry == "Can I play with you ?" or entry == "Can I play a game ?" or entry == "I want to play !" or entry == "Can I play ?":
        webbrowser.open_new("https://agar.io/")
        chat()
    elif entry == "math test" or entry == "math":
        math_test()
        chat()
    elif entry == "NYAAA" or entry == "Nyan cat" or entry == "nyan cat" or entry == "NYAN CAT" or entry == "Nyan" or entry == "nyan" or entry == "Nyan cat easter egg !" or entry == "NYAAA easter egg !":
        easter_egg_nc()
        chat()
    elif entry == "Can you bring me some water please ?" or entry == "Can you bring me some water please?" or entry == "can you bring me some water please ?"or entry == "can you bring me some water please?" or entry == "Can you bring me water please ?" or entry == "Can you bring me water please?" or entry == "can you bring me water please ?" or entry == "can you bring me water please?" or entry == "Can you bring me some water ?" or entry == "Can you bring me some water?":
        print("You are kidding me right ?")
        chat()
    elif entry == "open my internet browser" or entry == "Open my internet browser.":
        webbrowser.open_new("https://www.startpage.com")
        print("You could at least ask it nicely...")
        chat()
    elif entry == "open my internet browser please" or entry == "Open my internet browser please.":
        webbrowser.open_new("https://www.startpage.com")
        print("Of course !")
        chat()
    elif entry == "affection":
        print(affection)
    elif entry == "quit" or entry == "exit" or entry == "back" or entry == "Quit" or entry == "Exit" or entry == "Back":
        clear_terminal()
    else:
        print("It looks like there is a bug in the Matrix...")
        chat()

def easter_egg_nc():
    print("""
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
            ░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░
            ░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░
            ░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░
            ░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░
            ░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░
            ░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░
            ░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░
            ░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░
            ░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░
            ░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░
            ░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

        """)
    webbrowser.open_new("https://www.youtube.com/watch?v=Cqv8j_x7qm8")