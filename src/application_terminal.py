#python standart library modules
import os
import sys
#personnal modules
from application import Application




class Terminal (Application): 
    project_name = "Python terminal - Gestion d'Université"
    project_version = float(1.0)

    def __init__(self):
        #Instance attributes
        self.terminal_state = "LOADING"

        #Instance methods calling
        self.app_main_menu()
    
    def app_launch(self):
        self.terminal_operation_clear()
        print(f"Welcome to {Terminal.project_name}")

        

    def app_main_menu(self):
        user_choice = int(input("Main menu \n 1) Start Application\n 2) Options\n 3) Quit\n"))

        match user_choice:
            case 1:
                self.app_launch()
            case 2:
                self.app_options()
            case 3:
                self.app_quit()
            case _:
                pass
    
    def app_options(self):
        pass

    def app_quit(self):
        exit()

    # function to clear terminal
    def terminal_operation_clear(self):
        if (sys.platform == "win32"):
            os.system('cls')
        elif(sys.platform == "darwin"):
            os.system('clear')
        else:
            os.system('cls')