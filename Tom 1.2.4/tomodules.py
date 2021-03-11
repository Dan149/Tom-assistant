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
                +-----------------------------------+-------------------------------------+
                |     Created by: Falkov Daniel     |     Thanks to Excomptix Team        |
                +-----------------------------------+                                     |
                |     MIT license, free to use.     | http://www.excomptix.byethost24.com |
                +-----------------------------------+-------------------------------------+
""")        

def get_datetime():
    print('\nDate & time: {}'.format(datetime.datetime.now()))
