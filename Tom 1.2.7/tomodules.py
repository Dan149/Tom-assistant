# -*- coding: utf-8 -*-
import tomodules
import community_mods
# external modules:
import datetime
import webbrowser
import os
import time
from math import pi

time_pause = 0.05

def clear_terminal():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")

def banner():
    time.sleep(2.3)
    clear_terminal()
    if os.name =="nt":
        os.system("color 01")
    else:
        pass
    print("\n\n          TTTTTTTTTTTTTTTTTTTTTTT                                      ")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 02")
    else:
        pass
    print("          T:::::::::::::::::::::T                                      ")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 03")
    else:
        pass
    print("          T:::::::::::::::::::::T                                      ")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 04")
    else:
        pass
    print("          T:::::TT:::::::TT:::::T                                      ")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 05")
    else:
        pass
    print("          TTTTTT  T:::::T  TTTTTTooooooooooo      mmmmmmm    mmmmmmm   ")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 06")
    else:
        pass
    print("                  T:::::T      oo:::::::::::oo  mm:::::::m  m:::::::mm ")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 07")
    else:
        pass
    print("                  T:::::T     o:::::::::::::::om::::::::::mm::::::::::m")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 08")
    else:
        pass
    print("                  T:::::T     o:::::ooooo:::::om::::::::::::::::::::::m")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 09")
    else:
        pass
    print("                  T:::::T     o::::o     o::::om:::::mmm::::::mmm:::::m")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 0B")
    else:
        pass
    print("                  T:::::T     o::::o     o::::om::::m   m::::m   m::::m")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 0C")
    else:
        pass
    print("                  T:::::T     o::::o     o::::om::::m   m::::m   m::::m")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 0D")
    else:
        pass
    print("                  T:::::T     o::::o     o::::om::::m   m::::m   m::::m")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 0E")
    else:
        pass
    print("                TT:::::::TT   o:::::ooooo:::::om::::m   m::::m   m::::m")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 01")
    else:
        pass
    print("                T:::::::::T   o:::::::::::::::om::::m   m::::m   m::::m")
    time.sleep(time_pause)
    if os.name =="nt":
        os.system("color 02")
    else:
        pass
    print("                T:::::::::T    oo:::::::::::oo m::::m   m::::m   m::::m")
    time.sleep(time_pause)
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
    launched = True
    while launched == True:
        print("To stop, type $OK.")
        print(f"Amount of numbers: {len(num_list)}.")
        add_num = input("\n Add a number: ")
        if add_num == "$OK":
            launched = False
        else:
            try:
                clear_terminal()
                num_list.append(float(add_num))
            except:
                clear_terminal()
                print("[x] ERROR: Input must be a number.\n")
    average = sum(num_list) / len(num_list)
    print(f"Your average is: {average}.")

def get_circle_circumference():
    mesure_unit = input("\nmesuring unit (cm, m...): ")
    circle_radius_str = input(f"circle radius in {mesure_unit}: ")
    try:
        circle_radius = float(circle_radius_str)
        circumf = circle_radius * 2 * pi
        print(f"\ncircumference of the circle: {circumf} {mesure_unit}")
    except:
        print("[x] ERROR: Input must be a number.")
        get_circle_circumference()

def get_sci_number():
    number_str = input("\nEnter the number you want to convert in scientific number: ")
    try:
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
    except:
        print("[x] ERROR: Input must be a number.")
        get_sci_number()

def get_ftemp():
    wind_speed_str = input("\nwind speed in km/h: ")
    temp_str = input("\nreal temperature Celsius: ")
    try:
        wind_speed = float(wind_speed_str)
        temp = float(temp_str)
        ftemp_equation = 13.12 + 0.6215 * temp + (0.3965 * temp - 11.37) * pow(wind_speed, 0.16)
        print(f"\nThe feeled temperature is: {ftemp_equation}")
    except:
        print("[x] ERROR: Input must be a number.")
        get_ftemp()

def fahrenheit_to_celsius():
    tf_str = input("\nTemperature in Fahrenheit: ")
    try:
        tf = float(tf_str)
        tmp_celsius = (tf - 32) / 1.8
        print(f"\nthe result of the conversion °F --> °C is: {tmp_celsius}")
    except:
        print("[x] ERROR: Input must be a number.")
        fahrenheit_to_celsius()

def celsius_to_fahrenheit():
    tc_str = input("\nTemperature in Celsius: ")
    try:
        tc = float(tc_str)
        tmp_fahrenheit = 1.8 * tc + 32
        print(f"\nthe result of the conversion °C --> °F is: {tmp_fahrenheit}")
    except:
        print("[x] ERROR: Input must be a number.")
        celsius_to_fahrenheit()

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
    time.sleep(1)
    print("""
             +-----------------------------------------+
             |   Thanks to the Excomptix team:         |
             |                                         |
             |   http://www.excomptix.byethost24.com   |
             +-----------------------------------------+

""")
    time.sleep(1.75)

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
    try:
        if float(q1) == 4*15:
            print("Correct answer !")
            test_score = test_score + 1
        else:
            print("Wrong answer...")
    except:
        print("[x] ERROR: Input must be a number.")
#####
    q2 = input("\nWhat is the result of 6 * 0.5 ?\n>> ")
    try:
        if float(q2) == 6*0.5:
            print("Correct answer !")
            test_score = test_score + 1
        else:
            print("Wrong answer...")
    except:
        print("[x] ERROR: Input must be a number.")
#####
    try:
        q3 = input("\nWhat is the result of 9 * 7 ?\n>> ")
        if float(q3) == 9*7:
            print("Correct answer !")
            test_score = test_score + 1
        else:
            print("Wrong answer...")
    except:
        print("[x] ERROR: Input must be a number.")
#####
    try:
        q4 = input("\nWhat is the result of 5 * 250 ?\n>> ")
        if float(q4) == 5*250:
            print("Correct answer !")
            test_score = test_score + 1
        else:
            print("Wrong answer...")
    except:
        print("[x] ERROR: Input must be a number.")
#####
    try:
        q5 = input("\nWhat is the result of 7 * 50 ?\n>> ")
        if float(q5) == 7*50:
            print("Correct answer !")
            test_score = test_score + 1
        else:
            print("Wrong answer...")
    except:
        print("[x] ERROR: Input must be a number.")
#####
    try:
        q6 = input("\nWhat is the result of 9 * 20 ?\n>> ")
        if float(q6) == 9*20:
            print("Correct answer !")
            test_score = test_score + 1
        else:
            print("Wrong answer...")
    except:
        print("[x] ERROR: Input must be a number.")
#####
    try:
        q7 = input("\nWhat is the result of 3 * 650 ?\n>> ")
        if float(q7) == 3*650:
            print("Correct answer !")
            test_score = test_score + 1
        else:
            print("Wrong answer...")
    except:
        print("[x] ERROR: Input must be a number.")
#####
    try:
        q8 = input("\nWhat is the result of 7 - 80 ?\n>> ")
        if float(q8) == 7-80:
            print("Correct answer !")
            test_score = test_score + 1
        else:
            print("Wrong answer...")
    except:
        print("[x] ERROR: Input must be a number.")
#####
    try:
        q9 = input("\nWhat is the result of 368 + 120 ?\n>> ")
        if float(q9) == 368+120:
            print("Correct answer !")
            test_score = test_score + 1
        else:
            print("Wrong answer...")
    except:
        print("[x] ERROR: Input must be a number.")
#####
    try:
        q10 = input("\nWhat is the result of 150 + 2 + 3 + 5 - 5 ?\n>> ")
        if float(q10) == 150+2+3+5-5:
            print("Correct answer !")
            test_score = test_score + 1
        else:
            print("Wrong answer...")
    except:
        print("[x] ERROR: Input must be a number.")

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
    elif entry == "clear" or entry == "clear terminal" or entry == "clear the terminal" or entry == "cls":
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
    elif entry == "Can you bring me some water please ?" or entry == "Can you bring me some water please?" or entry == "can you bring me some water please ?"or entry == "can you bring me some water please?" or entry == "Can you bring me water please ?" or entry == "Can you bring me water please?" or entry == "can you bring me water please ?" or entry == "can you bring me water please?" or entry == "Can you bring me some water ?" or entry == "Can you bring me some water?" or entry == "Bring me some water." or entry == "bring me some water" or entry == "Bring me water." or entry == "bring me water":
        print("You are kidding me right ?")
        chat()
    elif entry == "open my internet browser" or entry == "Open my internet browser." or entry == "internet" or entry == "browser" or entry == "web":
        webbrowser.open_new("https://www.startpage.com")
        print("You could at least ask it nicely...")
        chat()
    elif entry == "open my internet browser please" or entry == "Open my internet browser please.":
        webbrowser.open_new("https://www.startpage.com")
        print("Of course !")
        chat()
    elif entry == "What's the date of today ?" or entry == "What's the date of today?" or entry == "what's the date of today ?" or entry == "what's the date of today?" or entry == "What is the date of today ?" or entry == "What is the date of today?" or entry == "what is the date of today ?" or entry == "what is the date of today?":
        get_datetime()
        chat()
    elif entry == "Wikipedia" or entry == "wikipedia" or entry == "Wiki" or entry == "wiki":
        webbrowser.open_new("https://en.wikipedia.org/")
        chat()
    elif entry == "Youtube" or entry == "youtube":
        webbrowser.open_new("https://www.youtube.com")
        chat()
    elif entry == "help" or entry == "Help" or entry == "HELP":
        webbrowser.open_new("https://github.com/Dan149/Tom-assistant/wiki/")
        chat()
    elif entry == "github" or entry == "Github" or entry == "Open github." or entry == "Open Github." or entry == "open github" or entry == "open Github" or entry == "Dan149's Github" or entry == "Dan149's github":
        github()
        chat()
    elif entry == "credits" or entry == "Credits" or entry == "display credits" or entry == "Display credits." or entry == "show credits" or entry == "Show credits.":
        credits()
        chat()
    elif entry == "Display banner." or entry == "display banner" or entry == "banner" or entry == "Banner" or entry == "Show banner." or entry == "show banner":
        banner()
        chat()
    elif entry == "MDR" or entry == "mdr":
        print("lol")
        chat()
    elif entry == "cmd" or entry == "CMD" or entry == "start cmd" or entry == "run cmd" or entry == "Start cmd" or entry == "Run cmd.":
        if os.name =="nt":
            os.system("start cmd")
            chat()
        else:
            print("Sorry, but you aren't on Windows, this command can't work.")
            chat()
    elif entry == "Calculate an average." or entry == "calculate an average" or entry == "average" or entry == "Average" or entry == "Can you calculate an average ?" or entry == "Can you calculate an average?":
        get_average()
        chat()
    elif entry == "Calculate a circle's circumference." or entry == "calculate a circle's circumference" or entry == "Circle's circumference." or entry == "Circle circumference." or entry == "circle's circumference" or entry == "circle circumference":
        get_circle_circumference()
        chat()
    elif entry == "convert °C --> °F" or entry == "Convert Celcius to Fahrenheit." or entry == "convert celcius to fahrenheit":
        celsius_to_fahrenheit()
        chat()
    elif entry == "convert °F --> °C" or entry == "Convert Celcius to Fahrenheit." or entry == "convert celcius to fahrenheit":
        fahrenheit_to_celsius()
        chat()
    elif entry == "convert temperature" or entry == "convert temp" or entry == "Convert temperature.":
        select = input("\n Chose an option: \n\n 1- convert °C --> °F\n 2- convert °F --> °C\n   ")
        if select == '1':
            celsius_to_fahrenheit()
            chat()
        elif select == '2':
            fahrenheit_to_celsius()
            chat()
        else:
            print("ERROR: option not found.")
            chat()
    elif entry == "calculate feeled temperature" or entry == "ftemp" or entry == "Calculate feeled temperature." or entry == "calculate ftemp" or entry == "Calculate ftemp." or entry == "Ftemp":
        get_ftemp()
        chat()
    elif entry == "convert a number in scientific number" or entry == "Convert a number in scientific number." or entry == "sci_number" or entry == "sci_num" or entry == "scientific number" or entry == "Scientific number.":
        get_sci_number()
        chat()
    elif entry == "quit" or entry == "Quit" or entry == "back" or entry == "Back" or entry == "exit" or entry == "Exit":
        clear_terminal()
    elif entry == "" or entry == " " or entry == "   " or entry == "    " or entry == "     " or entry == "      ":
        chat()
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

def testbox():
    #This function is related to the community_mods.py file.
    try:
        community_mods.exemple()
    except:
        print("ERROR: no code inside the 'testbox()' function.")
