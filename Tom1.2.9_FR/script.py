# -*- coding: utf-8 -*-
import tomodules
import community_scripts
# modules externes:
import datetime
import webbrowser
import os
import time
import pathlib
from math import pi

tomodules.clear_terminal()
version_name = "v1.2.9"
if os.name =="nt":
    os.system("color 0A")
else:
    pass

print(f"{version_name} mis en ligne par le détenteur du projet github officiel, DAN149.\n")
tomodules.banner()

print("\n       Bienvenue, je suis Tom !")


def main():
    entry = input("""
                    > MENU <

        +--------------------------------+
        |   1- Parler avec Tom (stable)  |
        +--------------------------------+
        |   Q- Quitter                   |
        +--------------------------------+
\n      Selectionner:
>> """)
    if entry == '1':
        tomodules.clear_terminal()
        tomodules.Chat()
        main()
    elif entry == 'testbox':            # This function is located at the end of the 'tomodules.py' file.
        further = input("\nCette fonction est conçue pour les développeurs, voulez vous continuer ? [y/n]\n > ")
        if further == "y" or further == "Y" or further == "yes" or further == "Yes" or further == "YES":
            tomodules.clear_terminal()
            tomodules.testbox()
            input("Appuyez sur Entrer pour continuer...")
            tomodules.clear_terminal()
            main()
        else:
            tomodules.clear_terminal()
            main()
    elif entry == 'Q':
        tomodules.clear_terminal()
        print("         \nArrêt de l'assistant en cours, veuillez ne pas fermer cette fenêtre.")
        [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]
        [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]
        time.sleep(1)
        print("\nVous pouvez à présent fermer cette fenêtre.")
        quit()

    else:
        tomodules.clear_terminal()
        main()
main()
