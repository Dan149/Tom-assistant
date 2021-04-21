# -*- coding: utf-8 -*-
import tomodules
import community_scripts
# external modules:
import datetime
import webbrowser
import os
import time
import pathlib
from math import pi

tomodules.clear_terminal()
version_name = "v1.2.8"
if os.name =="nt":
    os.system("color 0A")
else:
    pass

print(f"{version_name} uploaded by the official github project owner, DAN149.\n")
tomodules.banner()

print("\n       Welcome, I'm Tom !")


def main():
    entry = input("""
                    > MENU <

        +--------------------------------+
        |    1- Chat with Tom (stable)   |
        +--------------------------------+
        |    Q- Quit                     |
        +--------------------------------+
\n      Select:
    """)
    if entry == '1':
        tomodules.clear_terminal()
        tomodules.Chat()
        main()
    elif entry == 'testbox':            # This function is located at the end of the 'tomodules.py' file.
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
        [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]
        [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]
        time.sleep(1)
        quit()

    else:
        tomodules.clear_terminal()
        main()
main()
