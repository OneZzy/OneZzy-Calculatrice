import os
import sys
from time import sleep   

os.system('cls')

# --------ANSI COLORS---------
#     BLACK = "\033[0;30m"
#     RED = "\033[0;31m"
#     GREEN = "\033[0;32m"
#     BROWN = "\033[0;33m"
#     BLUE = "\033[0;34m"
#     PURPLE = "\033[0;35m"
#     CYAN = "\033[0;36m"
#     LIGHT_GRAY = "\033[0;37m"
#     DARK_GRAY = "\033[1;30m"
#     LIGHT_RED = "\033[1;31m"
#     LIGHT_GREEN = "\033[1;32m"
#     YELLOW = "\033[1;33m"
#     LIGHT_BLUE = "\033[1;34m"
#     LIGHT_PURPLE = "\033[1;35m"
#     LIGHT_CYAN = "\033[1;36m"
#     LIGHT_WHITE = "\033[1;37m"
#     BOLD = "\033[1m"
#     FAINT = "\033[2m"
#     ITALIC = "\033[3m"
#     UNDERLINE = "\033[4m"
#     BLINK = "\033[5m"
#     NEGATIVE = "\033[7m"
#     CROSSED = "\033[9m"
#     END = "\033[0m"
# -------------------------

while(1):
    os.system('cls') 
    words = """\n
    \033[0;35m ██████\033[0;34m╗ \033[0;35m███\033[0;34m╗   \033[0;35m██\033[0;34m╗\033[0;35m███████\033[0;34m╗\033[0;35m███████\033[0;34m╗\033[0;35m███████\033[0;34m╗\033[0;35m██\033[0;34m╗   \033[0;35m██\033[0;34m╗
    \033[0;35m██\033[0;34m╔═══\033[0;35m██\033[0;34m╗\033[0;35m████\033[0;34m╗  \033[0;35m██\033[0;34m║\033[0;35m██\033[0;34m╔════╝╚══\033[0;35m███\033[0;34m╔╝╚══\033[0;35m███\033[0;34m╔╝╚\033[0;35m██\033[0;34m╗ \033[0;35m██\033[0;34m╔╝
    \033[0;35m██\033[0;34m║   \033[0;35m██\033[0;34m║\033[0;35m██\033[0;34m╔\033[0;35m██\033[0;34m╗ \033[0;35m██\033[0;34m║\033[0;35m█████\033[0;34m╗    \033[0;35m███\033[0;34m╝    \033[0;35m███\033[0;34m╔╝  ╚\033[0;35m█\033[0;35m███\033[0;34m╔╝ 
    \033[0;35m██\033[0;34m║   \033[0;35m██\033[0;34m║\033[0;35m██\033[0;34m║╚\033[0;35m██\033[0;34m╗\033[0;35m██\033[0;34m║\033[0;35m██\033[0;34m╔══╝   \033[0;35m███\033[0;34m╔╝   \033[0;35m███\033[0;34m╔╝    ╚\033[0;35m██\033[0;34m╔╝  
    ╚\033[0;35m██████\033[0;34m╔╝\033[0;35m██\033[0;34m║ ╚\033[0;35m████\033[0;34m║\033[0;35m███████\033[0;34m╗\033[0;35m███████\033[0;34m╗\033[0;35m███████\033[0;34m╗   \033[0;35m██\033[0;34m║   
     \033[0;34m╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝   ╚═╝   

        [1] Adition
        [2] Multiplication
        [3] Soustraction
        [4] Division
        \n"""
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()

    choix = input('Que voulez vous faire: ')

    if choix == "1":
        an1 = input("First Number: ")
        an2 = input("Second Number: ")
        an3 = int(an1)+int(an2)
        print("\033[0;32m Réponse: ",an3)
        input('\033[0;31mAppuyer sur "ENTER" pour revenir au programm\033[0m')


    if choix == "2":
        an1 = input("First Number: ")
        an2 = input("Second Number: ")
        an3 = int(an1)*int(an2)
        print("\033[0;32m Réponse: ",an3)
        input('\033[0;31mAppuyer sur "ENTER" pour revenir au programm\033[0m') 

    if choix == "3":
        an1 = input("First Number: ")
        an2 = input("Second Number: ")
        an3 = int(an1)-int(an2)
        print("\033[0;32m Réponse: ",an3)
        input('\033[0;31mAppuyer sur "ENTER" pour revenir au programm\033[0m')  

    if choix == "4":
        an1 = input("First Number: ")
        an2 = input("Second Number: ")
        an3 = int(an1)/int(an2)
        print("\033[0;32m Réponse: ",an3)
        input('\033[0;31mAppuyer sur "ENTER" pour revenir au programm\033[0m') 