#!usr/bin/python3
import datetime
from math import pi
#Release No.3, version alpha 0.02 full, no-IA, uploaded by the official github project owner. for more info, check https://github.com/Dan149/Tom-assistant
prenom = input("Entrez votre prénom: ")
tutoyer = input("Voulez vous être tutoyé ? Si oui, marquez 'oui': ")
if (tutoyer == 'oui'):
    print(f"\nBienvenue {prenom}, je suis Tom, ton assistant artificiel !")

else:
    print("\nBienvenue Monsieur, je suis Tom, votre assistant artificiel !")

def help():
    if (tutoyer == "oui"):
        print(f"{prenom}, voici les fonctionnalités disponibles:")
    else:
        print("Monsieur, voici les fonctionnalités disponibles:")
    print("   ")
    print("version() : affiche la version de l'assistant")
    print("get_datetime() : affiche la date et l'heure précise actuelle")
    print("get_sci_number : permet de convertir un nombre quelquonque en nombre scientifique")
    print("get_ftemp() : permet de calculer la température ressentie")
    print("fahrenheit_to_celsius() : permet de convertir les °F en °C")
    print("celsius_to_fahrenheit() : permet de convertir les °C en °F")
    print("get_circle_circumference() : permet de calculer la circonférence d'un cercle")
    print("get_average() : permet de calculer la moyenne de plusieurs nombres")
    print("credits() : Voir les crédits du logiciel (en anglais)")
    print("github() : Lien vers le Github du créateur")
    print("main() : répertoire de lancemant des modules")
    if (tutoyer == "oui"):
        print("get_name() : affiche ton prenom")
    else:
        print("get_name() : affiche votre prenom")

def version():
    version_name = "alpha 0.03"
    print("\n         ______________________________________")
    print("")
    print(f"         Version de l'assistant : {version_name}")
    print("         ______________________________________")
   
def get_name():
    print(f"\nVotre prénom est {prenom}.")
    
def get_datetime():
    print ('\nDate & heure actuelle: {}'.format(datetime.datetime.now()))
    
def get_sci_number():
    if (tutoyer == "oui"):
        number_str = input("\nEntre le nombre qui sera converti en nombre scientifique: ")
    else:
        number_str = input("\nEntrez le nombre qui sera converti en nombre scientifique: ")
    number = float(number_str)
    exposant = 0
    if (number < 1):
        while (number < 1): 
            number = number * 10 
            exposant = exposant - 1
    if (number > 1):
        while (number > 10):
            number = number / 10
            exposant = exposant + 1
    print(f"\n{number} x 1O Exposant : {exposant}.")
    
def get_ftemp():
    wind_speed_str = input("\nVitesse du vent en km/h: ")
    temp_str = input("\nTempérature réelle en Celsius: ")
    wind_speed = float(wind_speed_str)
    temp = float(temp_str)
    ftemp_equation = 13.12 + 0.6215 * temp + (0.3965 * temp - 11.37) * pow(wind_speed, 0.16)
    print(f"\nLa température ressentie est: {ftemp_equation}")
    
def fahrenheit_to_celsius():
    tf_str = input("\nTempérature en Fahrenheit: ")
    tf = float(tf_str)
    tmp_celsius = (tf - 32) / 1.8
    print(f"\nLe résultat de la conversion °F --> °C est: {tmp_celsius}")

def celsius_to_fahrenheit():
    tc_str = input("\nTempérature en Celsius: ")
    tc = float(tc_str)
    tmp_fahrenheit = 1.8 * tc + 32
    print(f"\nLe résultat de la conversion °C --> °F est: {tmp_fahrenheit}")
    
def get_circle_circumference():
    mesure_unit = input("\nUnité de mesure (cm, m...): ")
    circle_radius_str = input(f"Rayon du cercle en {mesure_unit}: ")
    circle_radius = float(circle_radius_str)
    circonf = pi * 2 * circle_radius
    print(f"\nCirconférence du cercle: {circonf} {mesure_unit}")
    
def get_average():
    num_list = []
    enter_num_str = input("\nEntrer un nombre: ")
    enter_num = float(enter_num_str)
    num_list.append(enter_num)
    another = input("\nEn entrer un autre ? 'oui'/'non' ")
    while (another == "oui"):
        enter_num_str = input("\nEntrer un nombre: ")
        enter_num = float(enter_num_str)
        num_list.append(enter_num)
        another = input("\nEn entrer un autre ? 'oui'/'non' ")
    average = sum(num_list) / len(num_list)
    print(f"\nMoyenne: {average}")

def credits():
    print("\n__________________________")
    print("")
    print("Created by: Falkov Daniel.")
    print("MIT license, free to use.")
    print("__________________________")

def github():
    print("\nLe Github de mon créateur: https://github.com/Dan149")

def main():
    print("\nWARNING: the fourth option 'get_sci_number()' may not work.\n")
    start = input("""\nModules : \n
    1- afficher les informations concernant les modules (dev) \r 
    2- afficher la version du logiciel \r
    3- afficher la date et l'heure \r
    4- convertir un nombre en son équivalent scientifique \r
    5- calculer la temperature ressentie \r
    6- °F --> °C \r
    7- °C --> °F \r
    8- calculer la circonference d'un cercle
    9- calculer une moyenne
    10- crédits
    11- Github
    12- éteindre l'assistant
    \nEntrer un nombre: \n
    """)
    if start == '1':
        help()
    elif start == '2':
        version()
        main()
    elif start == '3':
        get_datetime()
        main()
    elif start == '4':
        get_sci_number()
        main()
    elif start == '5':
        get_ftemp()
        main()
    elif start == '6':
        fahrenheit_to_celsius()
        main()
    elif start == '7':
        celsius_to_fahrenheit()
        main()
    elif start == '8':
        get_circle_circumference()
        main()
    elif start == '9':
        get_average()
        main()
    elif start == '10':
        credits()
        main()
    elif start == '11':
        github()
        main()
    elif start == '12':
        quit()
    else:
        print("\nERROR: module not found.")
        main()
    
main()

