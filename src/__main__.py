

#custom modules
from application_terminal import Terminal
from application_panda3d import Panda3DApplication
from application_tkinter import GUIApplication


# Main Function

def main(application_mode):
    
    match application_mode:
        case "Terminal":
            terminal_instance  = Terminal()
            pass
        case "Panda 3D":
            panda3d_instance = Panda3DApplication()
            panda3d_instance.run()
        case "GUI":
            customtkinter_instance = GUIApplication()
            customtkinter_instance.mainloop()
        case _:
            "This command is unavailable"
        


#Main Guard
if __name__ == "__main__":
    application_mode = input("Tapez le mode que vous voulez ouvrir (Terminal, Panda 3D, GUI): ")
    main(application_mode)