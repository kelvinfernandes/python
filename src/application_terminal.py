#python standart library modules
import os
import sys

from application import Application

class Terminal (Application): 
    project_name = "Python terminal"
    project_version = float(1.0)

    def __init__(self):
        #Instance attributes
        self.terminal_state = "LOADING"

        #Instance methods calling
        self.app_launch()
    
    def app_launch(self):
        self.terminal_clear_operation()
        print(f"Welcome to {Terminal.project_name}")

    def app_main_menu(self):
        print("Main menu \n 1) Start Game\n 2) Options\n 3) Quit")
    

    def app_quit(self):
        exit()

    # function to clear terminal
    def terminal_clear_operation(self):
        if (sys.platform == "win32"):
            os.system('cls')
        elif(sys.platform == "darwin"):
            os.system('clear')
        else:
            os.system('cls')