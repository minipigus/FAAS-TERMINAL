import math
import time
import os
import hashlib
from cryptography.fernet import Fernet
import winsound
import random
from threading import Timer
import threading


global pas

def main_hello():
    print("""
    This app is by sattyrnus. It is based on the fuffydoesnothing project. 

This project contains:
- DMR control
- Fuel system
- Reactor structure system
- Menu with basic information
- Registration 
- Stop system 
- Rector stop system using a code
- Explosion system if the code is not entered

    """)
    time.sleep(9)
    clear()
    print("""    
░██████╗░██╗░░░██╗░█████╗░███╗░░██╗████████╗██╗░░░██╗███╗░░░███╗  ░██████╗░█████╗░██╗███████╗███╗░░██╗░█████╗░███████╗
██╔═══██╗██║░░░██║██╔══██╗████╗░██║╚══██╔══╝██║░░░██║████╗░████║  ██╔════╝██╔══██╗██║██╔════╝████╗░██║██╔══██╗██╔════╝
██║██╗██║██║░░░██║███████║██╔██╗██║░░░██║░░░██║░░░██║██╔████╔██║  ╚█████╗░██║░░╚═╝██║█████╗░░██╔██╗██║██║░░╚═╝█████╗░░
╚██████╔╝██║░░░██║██╔══██║██║╚████║░░░██║░░░██║░░░██║██║╚██╔╝██║  ░╚═══██╗██║░░██╗██║██╔══╝░░██║╚████║██║░░██╗██╔══╝░░
░╚═██╔═╝░╚██████╔╝██║░░██║██║░╚███║░░░██║░░░╚██████╔╝██║░╚═╝░██║  ██████╔╝╚█████╔╝██║███████╗██║░╚███║╚█████╔╝███████╗
░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝  ╚═════╝░░╚════╝░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░╚══════╝

██╗███╗░░██╗░█████╗░
██║████╗░██║██╔══██╗
██║██╔██╗██║██║░░╚═╝
██║██║╚████║██║░░██╗
██║██║░╚███║╚█████╔╝
╚═╝╚═╝░░╚══╝░╚════╝░
""")
    time.sleep(3)
    clear()
    faas()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def clear():
    print("\033[H\033[J", end="")

def faas():
    print("""


███████╗░█████╗░░█████╗░░██████╗  ████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░
██╔════╝██╔══██╗██╔══██╗██╔════╝  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░
█████╗░░███████║███████║╚█████╗░  ░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░
██╔══╝░░██╔══██║██╔══██║░╚═══██╗  ░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░
██║░░░░░██║░░██║██║░░██║██████╔╝  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝ 
          
""")
    time.sleep(3)
    login()
    

key = b'PYynEu5z5eJtTohErGY_MdpEe6zmnGJ2KmOJelSPRh0='
cipher = Fernet(key)

encrypted_username = b'gAAAAABnk5SuMr9JgeZ5VnkrlT5z4vjEN58nI4VL5yAID4dMBemgT082CIqJXEz32yAFkqNvqybUnZHV3QUTzV7d-6mO0Jk59w=='
encrypted_password = b'gAAAAABnk5SuEihr0FZKKvwSVhg4glQ8MCLscdzjlU9jRnmn6SWzQlCH-Rs6F_7RbBEletG81vke-kvm-Jsb3uQ2kwuLZXPFlw=='

def decrypt_data(encrypted_data):
    return cipher.decrypt(encrypted_data).decode()

def play_beep():
    winsound.Beep(1000, 300)

def login():

    saved_username = decrypt_data(encrypted_username)
    saved_password = decrypt_data(encrypted_password)

    print("=== Login ===")
    while True:
        username = input("Username: ")
        play_beep()
        password = input("Password: ")
        play_beep()
        if username == saved_username and password == saved_password:
            time.sleep(2)
            print("Access granted.")
            time.sleep(3)
            clear()
            main_menu()
            return True
        else:
            print("Incorrect username or password. Please try again.")


temperature = 70  
fuel_level = 100  
reactor_structure = 100  
psa_enabled = False  
heating_level = 0  
cooling_level = 0  
reactor_running = False  



def play_beep():
     winsound.Beep(1000, 200)

def play_beep():
    winsound.Beep(1000, 200)  

def start_reactor():
    global temperature, heating_level, cooling_level, psa_enabled, reactor_running
    
    print("[INFO] Reactor is starting...")
    play_beep()
    
    
    while True:
        try:
            heating_level = int(input("Enter initial heating level (1-5): "))
            play_beep()
            if 1 <= heating_level <= 5:
                break
            else:
                print("[ERROR] Heating level must be between 1 and 5.")
                play_beep()
        except ValueError:
            print("[ERROR] Invalid input. Please enter a number.")
            play_beep()

    
    while True:
        try:
            cooling_level = int(input("Enter initial cooling level (1-5): "))
            play_beep()
            if 1 <= cooling_level <= 5:
                break
            else:
                print("[ERROR] Cooling level must be between 1 and 5.")
                play_beep()
        except ValueError:
            print("[ERROR] Invalid input. Please enter a number.")
            play_beep()

    
    while True:
        psa_choice = input("Enable PSA (cooling)? Y/N: ").strip().upper()
        play_beep()
        if psa_choice in ("Y", "N"):
            psa_enabled = psa_choice == "Y"
            break
        else:
            print("[ERROR] Invalid input. Please enter Y or N.")
            play_beep()

    reactor_running = True
    print(f"[INFO] Starting reactor with heating level {heating_level} and cooling level {cooling_level}.")
    play_beep()
    time.sleep(2)
    temperature += heating_level * 20  
    run_reactor()

def run_reactor():
    global temperature, fuel_level, reactor_structure, reactor_running

    while reactor_running:
        clear()
       
        if psa_enabled:
            temperature += heating_level * 10 - cooling_level * 10
        else:
            temperature += heating_level * 10
        
        
        fuel_level -= 2
        if fuel_level < 0:
            fuel_level = 0

       
        if temperature < 100:
            print("[STALL] Reactor temperature too low! Reactor shutting down.")
            play_beep()
            time.sleep(3)
            reactor_running = False
            return

        
        if temperature >= 3500:
            reactor_structure -= 5
            if reactor_structure <= 0:
                reactor_structure = 0
                activate_red_code()
                return

        
        psa_status = "YES" if psa_enabled else "NO"
        print(f"| Structure: {reactor_structure}% | Temperature: {temperature}°F | Fuel Level: {fuel_level}% | PSA: {psa_status} |")
        play_beep()

        
        if fuel_level == 0:
            print("[ALERT] Fuel depleted! Ordering fuel...")
            play_beep()
            order_fuel()

        time.sleep(1)

def order_fuel():
    
    global fuel_level
    while True:
        try:
            amount = int(input("Enter the amount of fuel to order (1-100): "))
            play_beep()
            if 1 <= amount <= 100:
                if fuel_level + amount > 100:
                    print("[ERROR] Cannot exceed 100% fuel level.")
                    play_beep()
                else:
                    fuel_level += amount
                    print(f"[INFO] Fuel level increased to {fuel_level}%.")
                    play_beep()
                    return
            else:
                print("[ERROR] Fuel amount must be between 1 and 100.")
                play_beep()
        except ValueError:
            print("[ERROR] Invalid input. Please enter a number.")
            play_beep()

def activate_red_code():
    global reactor_running
    print("[ALERT] Reactor is overheating! Code RED activated!")
    play_beep()
    print("Enter shutdown code within 1 minute to prevent disaster.")
    play_beep()
    reactor_running = False  

    shutdown_code = "1234"  
    start_time = time.time()  

    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > 60: 
            activate_black_code()
            return

        user_code = input("Enter shutdown code: ")
        play_beep()
        if user_code == shutdown_code:
            print("[INFO] Reactor successfully shut down. Disaster averted.")
            play_beep()
            time.sleep(4)
            return  

        print(f"[ERROR] Incorrect code. Time left: {int(60 - elapsed_time)} seconds.")
        play_beep()

def activate_black_code():
    
    print("[ALERT] Code BLACK activated! Reactor will explode in 1 minute!")
    play_beep()
    time.sleep(60)  
    print("[ALERT] BOOM! Reactor exploded.")
    play_beep()
    exit() 

def company_info_menu():
    
    while True:
        print("\n=== COMPANY INFO ===")
        print("1. Company Overview")
        print("2. Employee List")
        print("3. Go Back to Main Menu")

        choice = input("Enter your choice: ")
        play_beep()
        clear()

        if choice == "1":
            print("\n[INFO] This app, developed by Quantum Science Inc, manages the DMR reactor in a more innovative and simplified way.")
        elif choice == "2":
            print("\n[INFO] Employees:")
            for _ in range(5):  
                print(generate_employee())
        elif choice == "3":
            break
        else:
            print("\n[ERROR] Invalid choice. Please try again.")


def main_menu():
    while True:
        clear()
        print("=== MAIN MENU ===")
        print("1. Start Reactor")
        print("2. Company Info")
        print("3. Exit")

        choice = input("Enter your choice: ")
        play_beep()
        if choice == "1":
            clear()
            start_reactor()
        elif choice == "2":
            company_info_menu()
        elif choice == "3":
            print("[INFO] Exiting program...")
            play_beep()
            break
        else:
            print("[ERROR] Invalid choice. Please try again.")
            play_beep()

def generate_employee():
    first_names = ["John", "Jane", "Mark", "Sarah", "Michael", "Laura", "James", "Emily"]
    last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Davis", "Miller", "Wilson"]
    roles = ["Supervisor", "Physicist", "Engineer", "Corporate", "Employee"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    role = random.choice(roles)

    return f"{first_name} {last_name} - {role}"



main_hello()
