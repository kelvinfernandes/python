

#custom modules
from application_terminal import Terminal
from application_panda3d import Panda3DApplication
from application_tkinter import GUIApplication

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
            python_app_instance = GUIApplication()
            python_app_instance.mainloop()
        case _:
            "This command is unavailable"
        


#Main Guard
if __name__ == "__main__":
    application_mode = int(input("Quel mode voulez-vous ouvrir\n 1) Terminal\n 2) Panda 3D\n 3) Custom Tkinter)\n "))
    main(application_mode)