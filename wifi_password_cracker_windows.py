import os
import time
import subprocess
from colorama import Fore
from colorama.initialise import init

init()

try:
    os.system("cls")
    print(f"{Fore.LIGHTMAGENTA_EX}Loading Wifi SSIDs . . .")
    time.sleep(3)
    os.system("cls")
    print(f"{Fore.GREEN}Wifi SSIDs Here")
    command_1 = subprocess.check_output("netsh wlan show profiles" , shell = True).decode()
    time.sleep(1)
    print(f"{Fore.CYAN}{command_1}\n")
    user_input = input(f"{Fore.GREEN}[+]{Fore.WHITE} Which Do You Want To Hack??? {Fore.LIGHTGREEN_EX}=>{Fore.WHITE} ")

    command_2 = os.system(f"netsh wlan show profile name = {user_input} key=clear")
    time.sleep(1)
    print(f"{Fore.GREEN}The Password Hacked Successfully\n")
    time.sleep(1)
    print(f"{Fore.LIGHTMAGENTA_EX} The Password is Available on Key Content")

except Exception as error:
    print(f"{Fore.RED}The Wifi SSID is not Available Please Reload The App")

finally:
    pass