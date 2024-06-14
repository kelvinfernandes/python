

#custom modules
from application_terminal import Terminal
from application_panda3d import Panda3DApplication
from application_tkinter import TerminalAppGUI
from application_ctk import GUIApplication

# global variables
python_app_instance = None


# Main Function

def main(application_mode):
    
    match application_mode:
        case 1:
            python_app_instance  = Terminal()
        case 2:
            python_app_instance = Panda3DApplication()
            python_app_instance.run()
        case 3:
            python_app_instance = TerminalAppGUI()
            python_app_instance.mainloop()
        case 4:
            python_app_instance = GUIApplication()
            python_app_instance.mainloop()
        case _:
            "This command is unavailable"
        

#Main Guard
if __name__ == "__main__":
    menu_items = [
        "Main menu",
        "1) Terminal",
        "2) Panda 3D",
        "3) Tkinter",
        "4) Custom Tkinter"
        ]
    
    # Calcul de la longueur maximale pour l'encadrement
    max_len = max(len(item) for item in menu_items)
    border = "+" + "-" * (max_len + 2) + "+"

    # Impression de la bordure supérieure
    print(border)
    
    # Impression des éléments du menu entourés de bordures
    for item in menu_items:
        line = f"| {item}" + " " * (max_len - len(item)) + " |"
        print(line)
    
    # Impression de la bordure inférieure
    print(border)

    application_mode = int(input("Quel mode voulez-vous ouvrir\n "))
    main(application_mode)