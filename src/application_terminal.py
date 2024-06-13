#python standart library modules
import os
import sys
#personnal modules
from application import Application
from etudiant import Etudiant
from enseignant import Enseignant
from personnel import Personnel
from base import Planning
from universite import Universite



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
        actor = int(input("Qui êtes vous?\n 1) Personnel\n 2) Etudiant\n 3) Enseignant\n"))

        # données standart de l'universite creation de l'universite
        #Attributs qui seront utilisés pour initiliser université

        notes_kelvin = {"reseaux":"12", "developpement":"17", "systeme":"12", "Anglais":"14", "Droit":"12" }
        planning_kelvin = Planning(8, 16)
        kelvin = Etudiant("Kelvin", 25, "Etudiant", planning_kelvin, 2020, 5, notes_kelvin)

        planning_trevor = Planning(8, 16)
        trevor = Enseignant("Trevor", 35, "Enseigant", planning_trevor)

        planning_yasmine = Planning(8, 16)
        jasmine = Personnel("Jasmine", 35, "Personnel", planning_yasmine)

        list_etudiant = {"Kelvin":kelvin,"John":"", "Ponnappa":"", "Mia":"", "Peter":"", "Natalie":"", "Ang":"", "Nguta":"", "Tamzyn":"", "Salome":""}
        list_enseignant = {"Trevor":trevor,"Tarryn":"", "Eugenia":"", "Verona":"", "Jackie":"", "Maureen":"", "Desiree":"", "Daly":"", "Hayman":"", "Ruveni":""}
        list_personnel = {"Jasmine":jasmine,"Taylor":"", "Allison":"", "Morgan":"", "Richard":"", "Morgan":"", "Cierra":"", "Ciara":"", "Paul":"", "Ericka":""}

        #Une seule instance de l'universite sera crée
        universite_instance = Universite(list_etudiant, list_enseignant, list_personnel)

        match actor:
            #dans le cas où l'acteur est un personnel de l'université
            case 1:
                print(f"Liste des Personnels de l'{universite_instance.nom} - qui êtes vous parmi cette liste?\n")
                
                #afficher la liste des etudiants dans le dictionnaire 
                for key in universite_instance.list_personnel:
                    print(key)
                
                print(f"Saissisez votre prenom tel que dans la liste\n")
                #recuperation du prenom
                login = input().capitalize()
                
                if universite_instance.list_personnel.get(login):
                    print(f"Bonjour, {login} vous êtes un personnel de l'{universite_instance.nom}\n")
                    uc = int(input(f"1) Pour manager si vous etes le directeur \n2) Pour administrer si vous êtes une secretaire\n3) Pour nettoyer si vous êtes une femme de menage\n4) Pour Cuisiner si vous êtes un cuisinier\n"))

                    #actions personnel
                    match uc:
                        #si le personnel est le directeur
                        case 1:
                            ucDirecteur = int(input(f"\n1) Licencier personnel\n2) Ajouter formation\n3) Renomer formation\n"))
                            match ucDirecteur:
                                case 1:
                                    print(f"Liste de personnel\n")
                
                                    #afficher la liste des personnels dans le dictionnaire 
                                    for key in universite_instance.list_personnel:
                                        print(key)
                                    
                                    personne_a_demissioner = input(f"Saissisez le prenom du personnel que vous voulez demissioner\n").capitalize()
                                
                                    universite_instance.licencier_personnel(personne_a_demissioner)
                                    print(universite_instance.list_personnel.get(personne_a_demissioner).fonction)
                                    menu = int(input(f"\nTapez 0 pour retourner au menu principal\n"))

                                    if(menu == 0):
                                        self.app_main_menu()
                                    
                        #si le personnel est une secretaire
                        case 2:
                            ucSecretaire = int(input(f"\n1) Changer le planning"))
                            if ucSecretaire == 1:
                                #afficher la liste des etudiants pour changer le planning
                                for key in universite_instance.list_etudiant:
                                    print(key)
                                
                                etudiant = input(f"Saissisez le prenom de l'étudiant que vous voulez changer le planning\n").capitalize()

                                if universite_instance.list_etudiant.get(etudiant):
                                    ucPlanning = int(input(f"\n1) Augmenter horaire entrée\n2) Diminuer horaire entrée\n3) Augmenter horaire sortie\n4) Diminuer horaire sortie\n"))
                                    
                                    match ucPlanning:
                                        case 1:
                                            aug = int(input("\nCombien d'heures voulez vous augmenter?\n"))
                                            print(f"Horaire entrée avant l'augmentation {universite_instance.list_etudiant.get(etudiant).recuperer_planning().horaire_entree}\n")
                                            universite_instance.list_etudiant.get(etudiant).recuperer_planning().aug_hor_ent(aug)
                                            print(f"Horaire entrée après l'augmentation {universite_instance.list_etudiant.get(etudiant).recuperer_planning().horaire_entree}\n")
                                            
                                            menu = int(input(f"\nTapez 0 pour retourner au menu principal\n"))
                                            if(menu == 0):
                                                self.app_main_menu()
                                        case 2:...

                        case _:...
           
            #dans le cas où l'acteur est un étudiant
            case 2:
                print(f"Liste des Etudiants de l'{universite_instance.nom} - qui êtes vous parmi cette liste?\n")
                
                #afficher la liste des etudiants dans le dictionnaire 
                for key in universite_instance.list_etudiant:
                    print(key)
                
                print(f"Saissisez votre prenom tel que dans la liste\n")
                #recuperation du prenom
                login = input().capitalize()
                
                if universite_instance.list_etudiant.get(login):
                    print(f"Bonjour, {login} vous êtes un étudiant de l'{universite_instance.nom}\n")
                    uc = int(input(f"1) Consulter les notes\n2) Demissioner\n"))

                    #actions etudiant
                    match uc:
                        case 1:
                            etudiant = universite_instance.list_etudiant.get(login)
                            print(etudiant.consulter_notes())
                            menu = int(input(f"\nTapez 0 pour retourner au menu principal\n"))
                            if(menu == 0):
                                self.app_main_menu()

                        case 2:
                            etudiant = universite_instance.list_etudiant.get(login)
                            etudiant.demissioner("Demissioner")
                            print(etudiant.fonction)
                            menu = int(input(f"\nTapez 0 pour retourner au menu principal\n"))
                            if(menu == 0):
                                self.app_main_menu()
                        case _:...

            #dans le cas où l'acteur est un enseignant
            case 3:
                print(f"Liste des Enseignants de l'{universite_instance.nom} - qui êtes vous parmi cette liste?\n")
                
                #afficher la liste des etudiants dans le dictionnaire 
                for key in universite_instance.list_enseignant:
                    print(key)
                
                print(f"Saissisez votre prenom tel que dans la liste\n")
                #recuperation du prenom
                login = input().capitalize()
                
                if universite_instance.list_enseignant.get(login):
                    print(f"Bonjour, {login} vous êtes un enseignant de l'{universite_instance.nom}\n")
                    ucEnseignant = int(input(f"1) Pour valider année d'un étudiant \n2) Pour redoubler un étudiant \n"))

                    #actions personnel
                    match ucEnseignant:
                        #Valider l'année d'un etudiant
                        case 1:
                            #selection de l'etudiant
                            print(f"Liste de vos étudiants\n")
        
                            #afficher la liste des etudiants dans le dictionnaire 
                            for key in universite_instance.list_etudiant:
                                print(key)

                            etudiant = input(f"\nSaissisez le prenom d'un de vos etudiants\n").capitalize()

                            
                            if universite_instance.list_etudiant.get(etudiant):
                                print(f"Année de {etudiant} avant la validation: {universite_instance.list_etudiant.get(etudiant).annee_scolaire}")
                                universite_instance.list_etudiant.get(etudiant).valider_annee(True)
                                print(f"Année de {etudiant} après la validation: {universite_instance.list_etudiant.get(etudiant).annee_scolaire}")
                                
                                menu = int(input(f"\nTapez 0 pour retourner au menu principal\n"))
                                if(menu == 0):
                                    self.app_main_menu()
                        #Redoubler un etudiant     
                        case 2:
                            #selection de l'etudiant
                            print(f"Liste de vos étudiants\n")
        
                            #afficher la liste des etudiants dans le dictionnaire 
                            for key in universite_instance.list_etudiant:
                                print(key)

                            etudiant = input(f"\nSaissisez le prenom de un de vos etudiants\n").capitalize()

                            
                            if universite_instance.list_etudiant.get(etudiant):
                                print(f"Année de {etudiant} avant la redoublement: {universite_instance.list_etudiant.get(etudiant).annee_scolaire}")
                                universite_instance.list_etudiant.get(etudiant).redoubler(True)
                                print(f"Année de {etudiant} après la redoublement: {universite_instance.list_etudiant.get(etudiant).annee_scolaire}")
                                
                                menu = int(input(f"\nTapez 0 pour retourner au menu principal\n"))
                                if(menu == 0):
                                    self.app_main_menu()
                        case _:...
                
            case _:
                pass

        

    def app_main_menu(self):
        user_choice = int(input(f"Main menu \n 1) Start Application\n 2) Options\n 3) Quit\n"))

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