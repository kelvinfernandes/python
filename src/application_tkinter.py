import os
import sys
import tkinter as tk
from tkinter import messagebox, simpledialog

# Personal modules
from application import Application
from etudiant import Etudiant
from enseignant import Enseignant
from personnel import Personnel
from base import Planning
from universite import Universite
from data import Data

class TerminalAppGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion d'Université")
        self.geometry("600x400")
        
        # Instance attributes
        data = Data()
        self.universite_instance = data.create_universite_instance()


        # Initialize main menu
        self.create_main_menu()

    
    def create_main_menu(self):
        self.clear_frame()
        
        tk.Label(self, text="Gestion d'Université", font=("Helvetica", 16)).pack(pady=20)

        tk.Button(self, text="Personnel", command=self.personnel_menu, width=30).pack(pady=10)
        tk.Button(self, text="Étudiant", command=self.etudiant_menu, width=30).pack(pady=10)
        tk.Button(self, text="Enseignant", command=self.enseignant_menu, width=30).pack(pady=10)
        tk.Button(self, text="Quitter", command=self.quit, width=30).pack(pady=10)

    def personnel_menu(self):
        self.clear_frame()
        
        tk.Label(self, text="Menu Personnel", font=("Helvetica", 16)).pack(pady=20)

        tk.Button(self, text="Lister Personnel", command=self.list_personnel, width=30).pack(pady=10)
        tk.Button(self, text="Licencier Personnel", command=self.fire_personnel, width=30).pack(pady=10)
        tk.Button(self, text="Retour", command=self.create_main_menu, width=30).pack(pady=10)

    def etudiant_menu(self):
        self.clear_frame()
        
        tk.Label(self, text="Menu Étudiant", font=("Helvetica", 16)).pack(pady=20)

        tk.Button(self, text="Lister Étudiants", command=self.list_etudiants, width=30).pack(pady=10)
        tk.Button(self, text="Changer Formation", command=self.change_formation, width=30).pack(pady=10)
        tk.Button(self, text="Afficher Notes", command=self.display_notes, width=30).pack(pady=10)  # New button
        tk.Button(self, text="Retour", command=self.create_main_menu, width=30).pack(pady=10)

    def enseignant_menu(self):
        self.clear_frame()
        
        tk.Label(self, text="Menu Enseignant", font=("Helvetica", 16)).pack(pady=20)

        tk.Button(self, text="Lister Enseignants", command=self.list_enseignants, width=30).pack(pady=10)
        tk.Button(self, text="Changer Planning", command=self.change_planning, width=30).pack(pady=10)
        tk.Button(self, text="Retour", command=self.create_main_menu, width=30).pack(pady=10)

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def list_personnel(self):
        personnel_names = "\n".join(self.universite_instance.list_personnel.keys())
        messagebox.showinfo("Liste du Personnel", f"Liste des personnels:\n{personnel_names}")

    def list_etudiants(self):
        etudiant_names = "\n".join(self.universite_instance.list_etudiant.keys())
        messagebox.showinfo("Liste des Étudiants", f"Liste des étudiants:\n{etudiant_names}")

    def list_enseignants(self):
        enseignant_names = "\n".join(self.universite_instance.list_enseignant.keys())
        messagebox.showinfo("Liste des Enseignants", f"Liste des enseignants:\n{enseignant_names}")

    def fire_personnel(self):
        personnel_name = simpledialog.askstring("Licencier Personnel", "Entrez le nom du personnel à licencier :").capitalize()
        if personnel_name and personnel_name in self.universite_instance.list_personnel:
            self.universite_instance.licencier_personnel(personnel_name)
            messagebox.showinfo("Licenciement Réussi", f"{personnel_name} a été licencié.")
        else:
            messagebox.showerror("Erreur", "Personnel non trouvé.")

    def change_formation(self):
        etudiant_name = simpledialog.askstring("Changer Formation Étudiant", "Entrez le nom de l'étudiant :").capitalize()
        if etudiant_name and etudiant_name in self.universite_instance.list_etudiant:
            formation = simpledialog.askstring("Nouvelle Formation", f"Formation actuelle:  {self.universite_instance.list_etudiant.get(etudiant_name).formation} \nEntrez la nouvelle formation :").capitalize()
            self.universite_instance.list_etudiant[etudiant_name].formation = formation
            messagebox.showinfo("Modification Réussie", f"La formation de {etudiant_name} a été modifiée.\nNouvelle formation:  {self.universite_instance.list_etudiant.get(etudiant_name).formation} \n")
        else:
            messagebox.showerror("Erreur", "Étudiant non trouvé.")

    def change_planning(self):
        etudiant_name = simpledialog.askstring("Changer Planning Étudiant", "Entrez le nom de l'étudiant :").capitalize()
        if etudiant_name and etudiant_name in self.universite_instance.list_etudiant:
            action = simpledialog.askinteger("Action", "1) Augmenter Horaire Entrée\n2) Diminuer Horaire Entrée\n3) Augmenter Horaire Sortie\n4) Diminuer Horaire Sortie")
            if action in [1, 2, 3, 4]:
                hours = simpledialog.askinteger("Heures", "Entrez le nombre d'heures :")
                etudiant = self.universite_instance.list_etudiant[etudiant_name]
                if action == 1:
                    etudiant.recuperer_planning().aug_hor_ent(hours)
                elif action == 2:
                    etudiant.recuperer_planning().dim_hor_ent(hours)
                elif action == 3:
                    etudiant.recuperer_planning().aug_hor_sort(hours)
                elif action == 4:
                    etudiant.recuperer_planning().dim_hor_sort(hours)
                messagebox.showinfo("Modification Réussie", f"Le planning de {etudiant_name} a été modifié.")
            else:
                messagebox.showerror("Erreur", "Action invalide.")
        else:
            messagebox.showerror("Erreur", "Étudiant non trouvé.")

    def display_notes(self):
        etudiant_name = simpledialog.askstring("Afficher Notes Étudiant", "Entrez le nom de l'étudiant :").capitalize()
        if etudiant_name and etudiant_name in self.universite_instance.list_etudiant:
            notes = self.universite_instance.list_etudiant[etudiant_name].notes
            notes_str = "\n".join([f"{subject}: {grade}" for subject, grade in notes.items()])
            messagebox.showinfo("Notes de l'Étudiant", f"Notes de {etudiant_name}:\n{notes_str}")
        else:
            messagebox.showerror("Erreur", "Étudiant non trouvé.")

    def quit(self):
        self.destroy()


if __name__ == "__main__":
    app = TerminalAppGUI()
    app.mainloop()
