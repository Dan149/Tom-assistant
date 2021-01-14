import datetime
from math import pi

prenom = input("Entrez votre prénom: ")
tutoyer = input("Voulez vous être tutoyé ? Si oui, marquez 'oui': ")
if (tutoyer == "oui"):
    print(f"Bienvenue {prenom}, je suis Tom, ton assistant artificiel !")
    print("Pour afficher mes fonctionnalités, entre la commande help()")
else:
    print("Bienvenue Monsieur, je suis Tom, votre assistant artificiel !")
    print("Pour afficher mes fonctionnalités, entrez la commande help()")
    
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
    print("credits() : Voir les crédits du logiciel (en anglais)")
    print("github() : Lien vers le Github du créateur")
    if (tutoyer == "oui"):
        print("get_name() : affiche ton prenom")
    else:
        print("get_name() : affiche votre prenom")

def version():
    version_name = "alpha 0.01"
    print("         ______________________________________")
    print("   ")
    print(f"         Version de l'assistant : {version_name}")
    print("   ")
    print("         ______________________________________")
   
def get_name():
    print(f"Votre prénom est {prenom}.")
    
def get_datetime():
    print ('Date & heure actuelle: {}'.format(datetime.datetime.now()))
    
def get_sci_number():
    if (tutoyer == "oui"):
        number_str = input("Entre le nombre qui sera converti en nombre scientifique: ")
    else:
        number_str = input("Entrez le nombre qui sera converti en nombre scientifique: ")
    number = float(number_str)
    exposant = 0
    if (number > 1):
        while (number > 10):
            number = number / 10
            exposant = exposant + 1
    if (number < 1):
        while (number < 1): 
            number = number * 10 
            exposant = exposant - 1
    print(f"{number} x 1O Exposant : {exposant}.")
    
def get_ftemp():
    wind_speed_str = input("Vitesse du vent en km/h: ")
    temp_str = input("Température réelle en Celsius: ")
    wind_speed = float(wind_speed_str)
    temp = float(temp_str)
    ftemp_equation = 13.12 + 0.6215 * temp + (0.3965 * temp - 11.37) * pow(wind_speed, 0.16)
    print(f"La température ressentie est: {ftemp_equation}")
    
def fahrenheit_to_celsius():
    tf_str = input("Température en Fahrenheit: ")
    tf = float(tf_str)
    tmp_celsius = (tf - 32) / 1.8
    print(f"Le résultat de la conversion °F --> °C est: {tmp_celsius}")

def celsius_to_fahrenheit():
    tc_str = input("Température en Celsius: ")
    tc = float(tc_str)
    tmp_fahrenheit = 1.8 * tc + 32
    print(f"Le résultat de la conversion °C --> °F est: {tmp_fahrenheit}")
    
def get_circle_circumference():
    mesure_unit = input("Unité de mesure (cm, m...): ")
    circle_radius_str = input(f"Rayon du cercle en {mesure_unit}: ")
    circle_radius = float(circle_radius_str)
    circonf = pi * 2 * circle_radius
    print(f"Circonférence du cercle: {circonf} {mesure_unit}")

def credits():
    print("Created by: Falkov Daniel.")
    print("MIT license, free to use.")
    print("__________________________")

def github():
    print("Le Github de mon créateur: https://github.com/Dan149")
