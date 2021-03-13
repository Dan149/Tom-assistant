#Tom assistant for Windows, if you run this script on linux or mac, some color features wont work...
import tomodules
import datetime
import webbrowser
import os
import sys
import time
from math import pi

tomodules.clear_terminal()
version_name = "v1.2.5"
if os.name =="nt": 
    os.system("color 0A")
else:
    pass
    
print(f"{version_name} uploaded by the official github project owner.\n")
tomodules.banner()

print("\n       Welcome, I'm Tom !")

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
        tomodules.chat()
        common_selector()
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
        time.sleep(1)
        quit()

    else:
        print("\n[x] ERROR: module or option not found.")
        callback()
        main()
main()