# -*- coding: utf-8 -*-
import tomodules
import community_mods
#external modules:
import datetime
import webbrowser
import os
import time
from math import pi

tomodules.clear_terminal()
version_name = "v1.2.7"
if os.name =="nt":
    os.system("color 0A")
else:
    pass

print(f"{version_name} uploaded by the official github project owner, DAN149.\n")
tomodules.banner()

print("\n       Welcome, I'm Tom !")

###############################################################  ________
#####################   Module selector   #####################          |
###############################################################          V

def math_selector():
    entry = input("""

                            > Maths modules <

    WARNING: The math modules moved into the 'Chat with Tom' function.

        +-------------------------------------------------------+
        |      99- Back                                         |
        +-------------------------------------------------------+
\n      Select:
        """)

    if entry == '99':
        tomodules.clear_terminal()
        main()
    else:
        tomodules.clear_terminal()
        math_selector()

def main():
    entry = input("""
                    > MENU <

        +--------------------------------+
        |    1- Math functions           |
        +--------------------------------+
        |    2- Chat with Tom (stable)   |
        +--------------------------------+
        |    Q- Quit                     |
        +--------------------------------+
\n      Select:
    """)
    if entry == '1':
        tomodules.clear_terminal()
        math_selector()
    elif entry == '2':
        tomodules.clear_terminal()
        tomodules.chat()
        main()
    elif entry == 'testbox':
        further = input("\nThis function is made for developers, do you want to continue ? [y/n]\n > ")
        if further == "y" or further == "Y" or further == "yes" or further == "Yes" or further == "YES":
            tomodules.clear_terminal()
            tomodules.testbox()
            input("Press Enter to continue...")
            tomodules.clear_terminal()
            main()
        else:
            tomodules.clear_terminal()
            main()
    elif entry == 'Q' or entry == "q":
        tomodules.clear_terminal()
        print("         \nQUITTING...")
        time.sleep(1)
        quit()

    else:
        tomodules.clear_terminal()
        main()
main()
