from application import Application
import customtkinter

class GUIApplication (Application, customtkinter.CTk):
    # class attribute
    def __init__(self):
        
        self.app_launch()

    
    #Methods   
    def app_launch(self):
        super().__init__()

        #windows configuration
        self.geometry("1000x800")
        self.title("Python application")
        
        #Buttons
        self.button_options = customtkinter.CTkButton(self, text="Options", command=self.button_app_options)
        self.button_options.grid(row=0, column=0, padx=15, pady=15)

        self.button_quit = customtkinter.CTkButton(self, text="Quit application", command=self.button_app_quit)
        self.button_quit.grid(row=0, column=1, padx=10, pady=35)

        self.combo_box_characters = customtkinter.CTkComboBox(self, values=["Haven", "Jonesy", "Peely"], command=self.button_select_char)
        self.combo_box_characters.grid(row=0, column=2)

        self.option_window = None
    def app_main_menu(self):
        pass
    
    def button_select_char(self):
        pass

    def app_quit(self):
        exit()
    
    def button_app_quit(self):
       self.app_quit()
    
    def button_app_options(self):
       self.app_options()


    def app_options(self):
        if self.option_window is None or not self.option_window.winfo_exists():
            self.option_window = GUIOptionWindow()
            self.option_window.focus()
        else:
             self.option_window.focus()

class GUIOptionWindow(customtkinter.CTkToplevel):
    
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Python app - options")

        self.label = customtkinter.CTkLabel(self, text="Top level window")
        self.label.grid(row=0, column=0)

if __name__=="__main__":
    guiapp_test_instance = GUIApplication()
    guiapp_test_instance.mainloop()