

#custom modules
from application_terminal import Terminal


# Main Function

def main(application_mode: str = "Terminal"):
    #app_instance.quit_app()
    terminal_instance  = Terminal()

    
    match application_mode:
        case "Terminal":
            pass
        case "Panda 3D":
            pass
        case "Custom Tkinter":
            pass
        case _:
            "This command is unavailable"
        


#Main Guard
if __name__ == "__main__":
    main("Terminal")