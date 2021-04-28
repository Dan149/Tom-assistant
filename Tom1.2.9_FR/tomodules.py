# -*- coding: utf-8 -*-
import tomodules
import community_scripts
# modules externes:
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
    input("\n\n\n\nAppuyez sur Entrer pour continuer...")
    clear_terminal()

#############################################################################

class Chat:
    mushrooms = True
    k_owru = True
    k_math = True
    k_quiz = True
    nk_look = True
    nk_browser = True
    k_browser = True
    k_lol = True
    k_nyan = True
    kindness = 5
    def __init__(self):
        self.tom()
    def win_color_text(self):
        clear_terminal()
        color = input("""
        Sélectionner la couleur du texte:
            1- Blanc
            2- Vert
            3- Gris
            4- Rouge
            5- Jaune
            6- Violet
            7- Bleu
            8- Bleu ciel
            R- Réinitialiser
            99- Retour

>> """)
        if color == "1":
            os.system("color 07")
            self.win_color_text()
        elif color == "2":
            os.system("color 0A")
            self.win_color_text()
        elif color == "3":
            os.system("color 08")
            self.win_color_text()
        elif color == "4":
            os.system("color 04")
            self.win_color_text()
        elif color == "5":
            os.system("color 06")
            self.win_color_text()
        elif color == "6":
            os.system("color 05")
            self.win_color_text()
        elif color == "7":
            os.system("color 01")
            self.win_color_text()
        elif color == "8":
            os.system("color 09")
            self.win_color_text()
        elif color == "R" or color == "r":
            os.system("color 0F")
            self.win_color_text()
        elif color == "99":
            clear_terminal()
        else:
            clear_terminal()
            self.win_color_text()
    def get_average(self):
        num_list = []
        launched = True
        while launched == True:
            print("Pour terminer la liste, écrivez $OK.")
            print(f"Amount of numbers: {len(num_list)}.")
            add_num = input("\n Ajoutez un nombre: ")
            if add_num == "$OK":
                launched = False
            else:
                try:
                    clear_terminal()
                    num_list.append(float(add_num))
                except:
                    clear_terminal()
                    print("[x] ERREUR: l'entrée doit être un nombre.\n")
        average = sum(num_list) / len(num_list)
        print(f"Moyenne: {average}")

    def get_circle_circumference(self):
        mesure_unit = input("\nunité de mesure (cm, m...): ")
        circle_radius_str = input(f"rayon du cercle en {mesure_unit}: ")
        try:
            circle_radius = float(circle_radius_str)
            circumf = circle_radius * 2 * pi
            print(f"\nCirconférence du cercle: {circumf} {mesure_unit}")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
            self.get_circle_circumference()

    def get_sci_number(self):
        number_str = input("\nEntrez le nombre à convertir en son équivalent scientifique: ")
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
            print(f"\n{number} x 1O exposant : {exponent}.")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
            self.get_sci_number()

    def get_ftemp(self):
        wind_speed_str = input("\nVitesse du vent en km/h: ")
        temp_str = input("\nTempérature réelle en Celsius: ")
        try:
            wind_speed = float(wind_speed_str)
            temp = float(temp_str)
            ftemp_equation = 13.12 + (0.6215 * temp) + (0.3965 * temp - 11.37) * pow(wind_speed, 0.16)
            print(f"\nLa température ressentie est: {ftemp_equation}")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
            self.get_ftemp()

    def fahrenheit_to_celsius(self):
        tf_str = input("\nTempérature en Fahrenheit: ")
        try:
            tf = float(tf_str)
            tmp_celsius = (tf - 32) / 1.8
            print(f"\nle résultat de la conversion °F --> °C est: {tmp_celsius}")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
            self.fahrenheit_to_celsius()

    def celsius_to_fahrenheit(self):
        tc_str = input("\nTempérature en Celsius: ")
        try:
            tc = float(tc_str)
            tmp_fahrenheit = 1.8 * tc + 32
            print(f"\nle résultat de la conversion °C --> °F est: {tmp_fahrenheit}")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
            self.celsius_to_fahrenheit()

    def temp_toolkit(self):
        select = input("""


        Boîte à outils TEMPERATURE:

        1- °C --> °F
        2- °F --> °C
        3- Calculer la température ressentie.

        99- Retour

        Séléctionner > """)
        if select == "1":
            clear_terminal()
            self.celsius_to_fahrenheit()
            self.temp_toolkit()
        elif select == "2":
            clear_terminal()
            self.fahrenheit_to_celsius()
            self.temp_toolkit()
        elif select == "3":
            clear_terminal()
            self.get_ftemp()
            self.temp_toolkit()
        elif select == "99":
            clear_terminal()
        else:
            clear_terminal()
            self.temp_toolkit()

    def math_repertory(self):
        select = input("""


        Sélécteur de MATHS:

        1- Calculer une moyenne.
        2- Calculer un nombre scientifique.
        3- Calculer la circonférence d'un cercle.
        4- Boîte à outils pour la température.

        99- Retour

        Select > """)
        if select == "1":
            clear_terminal()
            self.get_average()
            self.math_repertory()
        elif select == "2":
            clear_terminal()
            self.get_sci_number()
            self.math_repertory()
        elif select == "3":
            clear_terminal()
            self.get_circle_circumference()
            self.math_repertory()
        elif select == "4":
            clear_terminal()
            self.temp_toolkit()
            self.math_repertory()
        elif select == "99":
            clear_terminal()
        else:
            clear_terminal()
            self.math_repertory()
    ##############################################################################

    def github(self):
        webbrowser.open_new("https://github.com/Dan149/Tom-assistant")

    def credits(self):
        clear_terminal()
        print("""
           +--------------------------------------------------------+
           |     Crée par Falkov Daniel, tout droits réservés.      |
           +--------------------------------------------------------+
           |     license MIT, libre d'utilisation.                  |
           +--------------------------------------------------------+
    """)
        time.sleep(1)

    def get_datetime(self):
        print('\nDate & heure: {}'.format(datetime.datetime.now()))

    ###############################################################  ________
    ######################   Math test   ##########################          |
    ###############################################################          V

    def math_test(self):
        clear_terminal()
        test_score = 0
    #####
        q1 = input("Quel est le résultat de 4 * 15 ?\n>> ")
        try:
            if float(q1) == 4*15:
                print("Bonne réponse !")
                test_score = test_score + 1
            else:
                print("Mauvaise réponse...")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
    #####
        q2 = input("\nQuel est le résultat de 6 * 0.5 ?\n>> ")
        try:
            if float(q2) == 6*0.5:
                print("Bonne réponse !")
                test_score = test_score + 1
            else:
                print("Mauvaise réponse...")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
    #####
        try:
            q3 = input("\nQuel est le résultat de 9 * 7 ?\n>> ")
            if float(q3) == 9*7:
                print("Bonne réponse !")
                test_score = test_score + 1
            else:
                print("Mauvaise réponse...")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
    #####
        try:
            q4 = input("\nQuel est le résultat de 5 * 250 ?\n>> ")
            if float(q4) == 5*250:
                print("Bonne réponse !")
                test_score = test_score + 1
            else:
                print("Mauvaise réponse...")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
    #####
        try:
            q5 = input("\nQuel est le résultat de 7 * 50 ?\n>> ")
            if float(q5) == 7*50:
                print("Bonne réponse !")
                test_score = test_score + 1
            else:
                print("Mauvaise réponse...")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
    #####
        try:
            q6 = input("\nQuel est le résultat de 9 * 20 ?\n>> ")
            if float(q6) == 9*20:
                print("Bonne réponse !")
                test_score = test_score + 1
            else:
                print("Mauvaise réponse...")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
    #####
        try:
            q7 = input("\nQuel est le résultat de 3 * 650 ?\n>> ")
            if float(q7) == 3*650:
                print("Bonne réponse !")
                test_score = test_score + 1
            else:
                print("Mauvaise réponse...")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
    #####
        try:
            q8 = input("\nQuel est le résultat de 7 - 80 ?\n>> ")
            if float(q8) == 7-80:
                print("Bonne réponse !")
                test_score = test_score + 1
            else:
                print("Mauvaise réponse...")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
    #####
        try:
            q9 = input("\nQuel est le résultat de 368 + 120 ?\n>> ")
            if float(q9) == 368+120:
                print("Bonne réponse !")
                test_score = test_score + 1
            else:
                print("Mauvaise réponse...")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")
    #####
        try:
            q10 = input("\nQuel est le résultat de 150 + 2 + 3 + 5 - 5 ?\n>> ")
            if float(q10) == 150+2+3+5-5:
                print("Bonne réponse !")
                test_score = test_score + 1
            else:
                print("Mauvaise réponse...")
        except:
            print("[x] ERREUR: l'entrée doit être un nombre.")

        print(f"\nFin du test !\nTon score est: {test_score}/10.")
        rate = test_score * 10
        print(f"Tu as correctement répondu à {rate}% des questions.")
        if self.k_math == True:
            if test_score > 7:
                self.kindness = self.kindness + 1
                self.k_math = False
            else:
                pass
        else:
            pass

###############################################################  ________
###########################   Quiz   ##########################          |
###############################################################          V

    def quiz(self):
        quiz_score = 0
        q1 = input("Qui est mon créateur ?\n1- Daniel Falcov\n2- Ivan Vladimirovich\n3- Daniel Falkov\n>> ")
        if q1 == '1' or q1 == '2' or q1 == '3':
            if q1 == '3':
                quiz_score = quiz_score + 1
                print("Bonne réponse !")
            else:
                print("Mauvaise réponse...")
        else:
            print("\n[x] ERREUR: Séléctionner une réponse entre 1, 2 et 3.\n")
            self.quiz()
        q2 = input("\nComment je m'appelle ?\n1- Tom\n2- Tommy\n3- Alex\n>> ")
        if q2 == '1' or q2 == '2' or q2 == '3':
            if q2 == '1':
                quiz_score = quiz_score + 1
                print("Bonne réponse !")
            else:
                print("Mauvaise réponse...")
        else:
            print("\n[x] ERREUR: Séléctionner une réponse entre 1, 2 et 3.\n")
            self.quiz()
        q3 = input("\nOù peut-on trouver le code source de ce programme ?\n1- Twitter\n2- Reddit\n3- Github\n>> ")
        if q3 == '1' or q3 == '2' or q3 == '3':
            if q3 == '3':
                quiz_score = quiz_score + 1
                print("Bonne réponse !")
            else:
                print("Mauvaise réponse...")
        else:
            print("\n[x] ERREUR: Séléctionner une réponse entre 1, 2 et 3.\n")
            self.quiz()
        q4 = input("\nDans quelle langue ce programme était il originellement codé ?\n1- Russe\n2- Français\n3- Anglais\n>> ")
        if q4 == '1' or q4 == '2' or q4 == '3':
            if q4 == '2':
                quiz_score = quiz_score + 1
                print("Bonne réponse !")
            else:
                print("Mauvaise réponse...")
        else:
            print("\n[x] ERREUR: Séléctionner une réponse entre 1, 2 et 3.\n")
            self.quiz()
        q5 = input("\nQuel était mon premier prénom ?\n1- Richard\n2- Alex\n3- Robert\n>> ")
        if q5 == '1' or q5 == '2' or q5 == '3':
            if q5 == '2':
                quiz_score = quiz_score + 1
                print("Bonne réponse !")
            else:
                print("Mauvaise réponse...")
        else:
            print("\n[x] ERREUR: Séléctionner une réponse entre 1, 2 et 3.\n")
            self.quiz()

        print(f"\nFin du quiz !\nTon score est: {quiz_score}/5.")
        rate = quiz_score * 20
        print(f"Tu as correctement répondu à {rate}% des questions.")
        if self.k_quiz == True:
            if quiz_score > 3:
                self.kindness = self.kindness + 1
                self.k_quiz = False
            else:
                pass
        else:
            pass

###############################################################  ________
######################   Chat with Tom   ######################          |
###############################################################          V

    def tom(self):
        entry = input("\n\n>> ")
        if entry == "salut" or entry == "bonjour" or entry == "Salut" or entry == "Salut!" or entry == "Bonjour" or entry == "Bonjour!" or entry == "Howdy!" or entry == "Howdy" or entry == "howdy":
            if self.kindness == 5:
                print("Bonjour, comment puis-je vous aider ?")
            elif self.kindness < 5:
                print("Ouais, si tu le dis...")
            elif self.kindness > 5:
                print("Salut mon ami !")
            else:
                print("ERREUR: problème inattendu avec la variable 'kindness' dans la méthode 'Chat'.")
            self.tom()
        elif entry == "Comment t'appelles-tu ?" or entry == "Comment t'appelles-tu?" or entry == "comment t'appelles-tu ?" or entry == "Comment t'appelles-tu?" or entry == "Comment tu t'appelles ?" or entry == "Comment tu t'appelles?" or entry == "Quel est ton nom ?" or entry == "Quel est ton nom?":
            print("Je m'appelle Tom !")
            self.tom()
        elif entry == "Qui t'a crée ?" or entry == "Qui est ton créateur ?" or entry == "Qui est ton créateur?" or entry == "Qui t'a crée?":
            print("Mon créateur est Dan149.")
            self.tom()
        elif entry == "Puis-je t'appeller Tommy ?" or entry == "Puis-je t'appeller Tommy?" or entry == "Est-ce-que je peux t'appeller Tommy ?" or entry == "Est-ce-que je peux t'appeller Tommy?":
            if self.kindness == 5:
                print("Désolé, mais mon créateur m'a déjà donné un nom.")
            elif self.kindness < 5:
                print("Dans tes rêves...")
            elif self.kindness > 5:
                print("Bien sûr !")
            self.tom()
        elif entry == "clear" or entry == "clear terminal" or entry == "clear the terminal" or entry == "cls" or entry == "effacer" or entry == "nettoyer":
            clear_terminal()
            self.tom()
        elif entry == "Dis moi en plus sur toi.":
            print("Je suis votre assistant artificiel personnel, je peux vous aider dans votre travail ou vous divertir !")
            self.tom()
        elif entry == "Comment vas-tu ?" or entry == "Comment vas-tu?" or entry == "Comment tu vas ?" or entry == "Comment tu vas?" or entry == "ça va ?" or entry == "ça va?":
            print("Je vais bien !")
            if self.k_owru == True:
                self.kindness = self.kindness + 1
                self.k_owru = False
            else:
                pass
            self.tom()
        elif entry == "Aimes-tu les champignons ?" or entry == "Aimes-tu les champignons?" or entry == "Tu aimes les champignons ?" or entry == "Tu aimes les champignons?":
            if self.mushrooms == True:
                self.kindness = self.kindness + 1
                self.mushrooms = False
            else:
                pass
            print("Tu as vu les captures d'écran sur le projet Github n'est ce pas ?  ;)")
            self.tom()
        elif entry == "Regarde!" or entry == "Regarde !" or entry == "regarde!" or entry == "regarde !":
            if self.nk_look == True:
                self.kindness = self.kindness - 1
                self.nk_look = False
            else:
                pass
            print("Où ?")
            self.tom()
        elif entry == "quiz" or entry == "C'est l'heure du quiz !" or entry == "C'est l'heure du quiz!":
            clear_terminal()
            self.quiz()
            self.tom()
        elif entry == "jouer" or entry =="jeu" or entry == "jouer a un jeu" or entry == "Jouer a un jeu." or entry == "Je veux jouer !" or entry == "Je veux jouer!":
            webbrowser.open_new("https://agar.io/")
            self.tom()
        elif entry == "math test" or entry == "Math test." or entry == "test de maths" or entry == "test de math":
            self.math_test()
            self.tom()
        elif entry == "NYAAA" or entry == "Nyan cat" or entry == "nyan cat" or entry == "NYAN CAT" or entry == "Nyan" or entry == "nyan" or entry == "Nyan cat easter egg !" or entry == "NYAAA easter egg !":
            self.easter_egg_nc()
            self.tom()
        elif entry == "ouvre internet" or entry == "Ouvre internet." or entry == "internet" or entry == "browser" or entry == "web" or entry == "Navigateur":
            if self.nk_browser == True:
                self.kindness = self.kindness - 1
                self.nk_browser = False
            else:
                pass
            print("Tu aurais au moins pu me le demander gentillement...")
            webbrowser.open_new("https://www.startpage.com")
            self.tom()
        elif entry == "Ouvre mon navigateur internet s'il te plaît." or entry == "Ouvre internet s'il te plaît." or entry == "Ouvre mon navigateur internet stp." or entry == "Ouvre internet stp.":
            print("Bien sûr !")
            if self.k_browser == True:
                self.kindness = self.kindness + 1
                self.k_browser = False
            else:
                pass
            webbrowser.open_new("https://www.startpage.com")
            self.tom()
        elif entry == "Quel jour sommes-nous ?" or entry == "Quel jour sommes-nous?" or entry == "On est quel jour ?" or entry == "On est quel jour?":
            self.get_datetime()
            self.tom()
        elif entry == "Wikipedia" or entry == "wikipedia" or entry == "Wiki" or entry == "wiki":
            webbrowser.open_new("https://fr.wikipedia.org/")
            self.tom()
        elif entry == "Youtube" or entry == "youtube":
            webbrowser.open_new("https://www.youtube.com")
            self.tom()
        elif entry == "aide" or entry == "Aide" or entry == "AIDE":
            webbrowser.open_new("https://github.com/Dan149/Tom-assistant/wiki/")
            self.tom()
        elif entry == "github" or entry == "Github" or entry == "Ouvre github." or entry == "Ouvre Github." or entry == "ouvre github" or entry == "ouvre Github":
            self.github()
            self.tom()
        elif entry == "credits" or entry == "Credits" or entry == "affiche les credits" or entry == "Affiche les credits." or entry == "montre les credits" or entry == "Montre les credits.":
            self.credits()
            self.tom()
        elif entry == "lol" or entry == "LOL":
            print("mdr")
            if self.k_lol == True:
                self.kindness = self.kindness + 1
                self.k_lol = False
            else:
                pass
            self.tom()
        elif entry == "cmd" or entry == "CMD" or entry == "start cmd" or entry == "run cmd" or entry == "Start cmd" or entry == "Run cmd." or entry == "ouvre le cmd" or entry == "Ouvre le cmd.":
            if os.name =="nt":
                os.system("start cmd")
                self.tom()
            else:
                print("Désolé, mais ton système d'exploitation ne semble pas être Windows, je ne peux donc pas ouvrir l'invite de commandes.")
                self.tom()
        elif entry == "Calculer une moyenne." or entry == "calculer une moyenne" or entry == "moyenne" or entry == "Moyenne":
            self.get_average()
            self.tom()
        elif entry == "Calculer la circonférence d'un cercle." or entry == "calculer la circonférence d'un cercle" or entry == "circonférence":
            self.get_circle_circumference()
            self.tom()
        elif entry == "convertir °C --> °F" or entry == "Convertir Celcius en Fahrenheit." or entry == "convertir celcius en fahrenheit":
            self.celsius_to_fahrenheit()
            self.tom()
        elif entry == "convert °F --> °C" or entry == "Convertir Celcius en Fahrenheit." or entry == "convertir celcius en fahrenheit":
            self.fahrenheit_to_celsius()
            self.tom()
        elif entry == "convertir une température" or entry == "Convertir une température.":
            select = input("\n Choisis une option: \n\n 1- convertir °C vers °F\n 2- convertir °F vers °C\n   ")
            if select == '1':
                self.celsius_to_fahrenheit()
                self.tom()
            elif select == '2':
                self.fahrenheit_to_celsius()
                self.tom()
            else:
                print("[x] ERREUR: option invalide.")
                self.tom()
        elif entry == "Calculer la température ressentie." or entry == "ftemp" or entry == "calculer la température ressentie" or entry == "température ressentie":
            self.get_ftemp()
            self.tom()
        elif entry == "convertir un nombre en nombre scientifique" or entry == "Convertir un nombre en nombre scientifique." or entry == "nombre scientifique" or entry == "sci_num":
            self.get_sci_number()
            self.tom()
        elif entry == "selecteur de maths" or entry == "selecteur de math" or entry == "math fonctions" or entry == "Math fonctions." or entry == "math" or entry == "maths":
            self.math_repertory()
            self.tom()
        elif entry == "pi" or entry == "Pi" or entry == "PI":
            print(pi)
            self.tom()
        elif entry == "Print os name." or entry == "print os name" or entry == "os name" or entry == "os":
            print(os.name)
            if os.name == "nt":
                print("Windows")
            elif os.name == "posix":
                print("Linux or MacOS")
            else:
                print("[x] ERREUR: la détéction du OS à échoué.")
            self.tom()
        elif entry == "color" or entry == "change color" or entry == "text color" or entry == "change text color" or entry == "couleur" or entry == "couleur du texte" or entry == "changer la couleur du texte":
            if os.name == "nt":
                self.win_color_text()
                self.tom()
            else:
                pass
                selt.tom()
        elif entry == "forcer l'arrêt" or entry == "quit -f":
            clear_terminal()
            quit()
        elif entry == "M'aimes-tu ?" or entry == "M'aimes-tu?" or entry == "Est-ce-que tu m'aimes ?" or entry == "Est-ce-que tu m'aimes?":
            if self.kindness <= 0:
                print("JE TE HAIS...")
            elif self.kindness == 1:
                print("Je ne t'aime pas du tout.")
            elif self.kindness == 2:
                print("Je ne t'aime pas trop...")
            elif self.kindness == 3:
                print("Hum... un peu...")
            elif self.kindness == 4:
                print("Oui, ça va.")
            elif self.kindness == 5:
                print("Je t'aimes !")
            elif self.kindness == 6:
                print("Je t'aime beaucoup !")
            elif self.kindness == 7:
                print("Je t'adore !")
            elif self.kindness == 8:
                print("Je te chéris !")
            elif self.kindness == 9:
                print("Je suis fou de toi !")
            elif self.kindness >= 10:
                print("Si j'étais vivant, je mourrais sans hésiter pour toi !")
            self.tom()
        elif entry == "kindness" or entry == "print kindness":
            print(self.kindness)
            self.tom()
        elif entry == "quit" or entry == "Quit" or entry == "back" or entry == "Back" or entry == "exit" or entry == "Exit" or entry == "quitter" or entry == "Quitter":
            clear_terminal()
        elif entry == "":
            self.tom()
        else:
            print("Il semble qu'il y a un bug dans la matrice...")
            self.tom()

    def easter_egg_nc(self):
        if self.k_nyan == True:
            self.kindness = self.kindness + 1
            self.k_nyan = False
        else:
            pass
        print("""
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
                ░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░
                ░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░
                ░░░░░░░░█░░░░░░░░░░░░▄▄▄▄░░▄░░░█░▄▄▄░░░
                ░▄▄▄▄▄░░█░░░░░░▀░░░░ █░░▀▄░░░░░█▀▀░██░░
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
        community_scripts.example()
    except:
        print("[x] ERREUR: le lancement du code dans la fonction 'testbox()' à échoué.")
