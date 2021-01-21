#!usr/bin/python3
#version optimized for debian linux
import datetime
from math import pi
#Release No.3, version alpha 0.02 full, no-IA, uploaded by the official github project owner. for more info, check https://github.com/Dan149/Tom-assistant
name = input("Enter your name: ")
print(f"\nWelcome {name}, I'm Tom, your artificial assistant !")

def help():

    print(f"{prenom}, those are the avalaible fonctionalities:\n")
    print("version() : display the assistant's version")
    print("get_datetime() : display the date and the time")
    print("get_sci_number : convert a simple number into scientific number")
    print("get_ftemp() : calculate the feeled temperature")
    print("fahrenheit_to_celsius() : convert °F into °C")
    print("celsius_to_fahrenheit() : convert les °C into °F")
    print("get_circle_circumference() : calculate the circumference of a circle")
    print("get_average() : calculate an average")
    print("credits() : see credits")
    print("github() : link to the creator's Github")
    print("main() : module launch repertory")
    print("get_name() : display your name")

def version():
    version_name = "alpha 0.04"
    print("\n         ______________________________________")
    print("")
    print(f"         Version : {version_name}")
    print("         ______________________________________")
   
def get_name():
    print(f"\nVotre prénom est {prenom}.")
    
def get_datetime():
    print ('\nDate & time: {}'.format(datetime.datetime.now()))
    
def get_sci_number():
    number_str = input("\nEnter the number you want to convert in scientific number: ")
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
    
def get_circle_circumference():
    mesure_unit = input("\nmesuring unit (cm, m...): ")
    circle_radius_str = input(f"circle radius in {mesure_unit}: ")
    circle_radius = float(circle_radius_str)
    circonf = pi * 2 * circle_radius
    print(f"\ncircumference of the circle: {circonf} {mesure_unit}")
    
def get_average():
    num_list = []
    enter_num_str = input("\nenter a number: ")
    enter_num = float(enter_num_str)
    num_list.append(enter_num)
    another = input("\nadd another one ? [yes/no] ")
    while (another == "yes" or another == "y" or another == "Y"):
        enter_num_str = input("\nEntrer un nombre: ")
        enter_num = float(enter_num_str)
        num_list.append(enter_num)
        another = input("\nadd another one ? [yes/no] ")
    average = sum(num_list) / len(num_list)
    print(f"\naverage: {average}")

def credits():
    print("\n__________________________")
    print("")
    print("Created by: Falkov Daniel.")
    print("MIT license, free to use.")
    print("__________________________")

def github():
    print("\nThe Github of my creator: https://github.com/Dan149")

def main():
    print("\nWARNING: the fourth option 'get_sci_number()' may not work.\n")
    start = input("""\nModules : \n
    1- display the informations about the modules (dev) \r 
    2- display the program version \r
    3- display the date and the time \r
    4- convert a number in scientific number \r
    5- calculate feeled temperature \r
    6- convert °F --> °C \r
    7- convert °C --> °F \r
    8- calculate a circle's circumference
    9- calculate an average
    10- credits
    11- Github
    12- Exit
    \nSelect: \n
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
