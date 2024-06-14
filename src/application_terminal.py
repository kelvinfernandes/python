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
        menu_items = [
                    "1) Personnel",
                    "2) Etudiant",
                    "3) Enseignant"
                    ]
                            
        self.menu(menu_items)
        actor = int(input("Qui êtes vous?\n"))

        # données standart de l'universite creation de l'universite
        #Attributs qui seront utilisés pour initiliser université

        #--------------------------------------------------------------------------------------------------------------------
        #CREATION DES ETUDIANTS
        #--------------------------------------------------------------------------------------------------------------------


        notes_kelvin = {"reseaux":"12", "developpement":"17", "systeme":"12", "Anglais":"14", "Droit":"12" }
        planning_kelvin = Planning(8, 16)
        kelvin = Etudiant("Kelvin", 25, "Etudiant", planning_kelvin, "IRS", 2020, 5, notes_kelvin)

        notes_john = {"reseaux":"14", "developpement":"15", "systeme":"13", "Anglais":"15", "Droit":"13" }
        planning_john = Planning(8, 16)
        john = Etudiant("John", 25, "Etudiant", planning_john, "Developpement web", 2020, 3, notes_john)

        notes_ponnappa = {"reseaux":"14", "developpement":"15", "systeme":"13", "Anglais":"15", "Droit":"13" }
        planning_ponnappa = Planning(8, 16)
        ponnappa = Etudiant("Ponnappa", 25, "Etudiant", planning_ponnappa, "IRS", 2020, 5, notes_ponnappa)

        #--------------------------------------------------------------------------------------------------------------------
        #CREATION DES ENSEIGNANTS
        #--------------------------------------------------------------------------------------------------------------------

        planning_trevor = Planning(8, 16)
        trevor = Enseignant("Trevor", 35, "Enseigant", planning_trevor)

        planning_tarryn = Planning(8, 16)
        tarryn = Enseignant("Tarryn", 35, "Enseigant", planning_tarryn)

        planning_eugenia = Planning(8, 16)
        eugenia = Enseignant("Eugenia", 35, "Enseigant", planning_eugenia)
        
        #--------------------------------------------------------------------------------------------------------------------
        #CREATION DES PERSONNELS
        #--------------------------------------------------------------------------------------------------------------------

        planning_yasmine = Planning(8, 16)
        jasmine = Personnel("Jasmine", 35, "Personnel", planning_yasmine)

        planning_taylor = Planning(8, 16)
        taylor = Personnel("Taylor", 35, "Personnel", planning_taylor)

        planning_allison = Planning(8, 16)
        allison = Personnel("Jasmine", 35, "Personnel", planning_allison)

        #--------------------------------------------------------------------------------------------------------------------
        #CREATION DES LISTS qui vont contenir les etudiants , enseigants, personnels
        #--------------------------------------------------------------------------------------------------------------------
        list_etudiant = {"Kelvin":kelvin,"John":john, "Ponnappa":ponnappa}
        list_enseignant = {"Trevor":trevor,"Tarryn":tarryn, "Eugenia":eugenia}
        list_personnel = {"Jasmine":jasmine,"Taylor":taylor, "Allison":allison}

        #Une seule instance de l'universite sera crée
        universite_instance = Universite(list_etudiant, list_enseignant, list_personnel)

        match actor:
            #dans le cas où l'acteur est un personnel de l'université
            case 1:
                print(f"Liste des Personnels de l'{universite_instance.nom} - qui êtes vous parmi cette liste?\n")
                
                #afficher la liste des etudiants dans le dictionnaire 
                for key in universite_instance.list_personnel:
                    print(key)
                
                print(f"\nSaissisez votre prenom tel que dans la liste\n")
                #recuperation du prenom
                login = input().capitalize()
                
                if universite_instance.list_personnel.get(login):
                    print(f"Bonjour, {login} vous êtes un personnel de l'{universite_instance.nom}\n")
                    menu_items = [
                        "1) Pour manager si vous etes le directeur",
                        "2) Pour administrer si vous êtes une secretaire"
                        ]
                    self.menu(menu_items)
                    uc = int(input())

                    #actions personnel
                    match uc:
                        #si le personnel est le directeur
                        case 1:
                            menu_items = [
                                "1) Licencier personnel",
                                "2) Changer la formation d'un étudiant"
                                ]
                            
                            self.menu(menu_items)
                            ucDirecteur = int(input())

                            match ucDirecteur:
                                case 1:
                                    print(f"Liste de personnel\n")
                
                                    #afficher la liste des personnels dans le dictionnaire 
                                    for key in universite_instance.list_personnel:
                                        print(key)
                                    
                                    personne_a_demissioner = input(f"\nSaissisez le prenom du personnel que vous voulez demissioner\n").capitalize()
                                
                                    universite_instance.licencier_personnel(personne_a_demissioner)
                                    print(universite_instance.list_personnel.get(personne_a_demissioner).fonction)
                                    menu = int(input(f"\nTapez 0 pour retourner au menu principal\n"))

                                    if(menu == 0):
                                        self.app_main_menu()
                                case 2:
                                    print(f"Liste des étudiants de l'{universite_instance.nom}\n")
                
                                    #afficher la liste des personnels dans le dictionnaire 
                                    for key in universite_instance.list_etudiant:
                                        print(key)
                                    
                                    etudiant = input(f"Saissisez le prenom de l'étudiant que vous voulez modifier de formation\n").capitalize()
                                    
                                    if universite_instance.list_etudiant.get(etudiant):
                                        print(f"Formation de {etudiant} avant la modification: {universite_instance.list_etudiant.get(etudiant).formation}\n")
                                        formation = input("Saissisez le nom de la formation\n").capitalize()
                                        universite_instance.list_etudiant.get(etudiant).formation = formation
                                        print(f"Formation de {etudiant} après la modification: {universite_instance.list_etudiant.get(etudiant).formation}\n")                                      
                                    else:
                                        print(f"Cet étudiant n'est pas dans la liste\n")

                                    menu = int(input(f"\nTapez 0 pour retourner au menu principal\n"))
                                    if(menu == 0):
                                            self.app_main_menu()
                                    
                        #si le personnel est une secretaire
                        case 2:
                            ucSecretaire = int(input(f"\n1) Changer le planning\n"))
                            if ucSecretaire == 1:
                                #afficher la liste des etudiants pour changer le planning
                                for key in universite_instance.list_etudiant:
                                    print(key)
                                
                                etudiant = input(f"\nSaissisez le prenom de l'étudiant que vous voulez changer le planning\n").capitalize()

                                if universite_instance.list_etudiant.get(etudiant):
                                    menu_items = [
                                        "1) Augmenter horaire entrée",
                                        "2) Diminuer horaire entrée",
                                        "3) Augmenter horaire sortie",
                                        "4) Diminuer horaire sortie"
                                        ]
                                    
                                    self.menu(menu_items)
                                    ucPlanning = int(input())
                                    
                                    match ucPlanning:
                                        case 1:
                                            aug = int(input("\nCombien d'heures voulez vous augmenter?\n"))
                                            print(f"Horaire entrée avant l'augmentation {universite_instance.list_etudiant.get(etudiant).recuperer_planning().horaire_entree}\n")
                                            universite_instance.list_etudiant.get(etudiant).recuperer_planning().aug_hor_ent(aug)
                                            print(f"Horaire entrée après l'augmentation {universite_instance.list_etudiant.get(etudiant).recuperer_planning().horaire_entree}\n")
                                            
                                            menu = int(input(f"\nTapez 0 pour retourner au menu principal\n"))
                                            if(menu == 0):
                                                self.app_main_menu()
                                        case 2:
                                            dim = int(input("\nHoraire Entrée: Combien d'heures voulez vous diminuer?\n"))
                                            print(f"Horaire entrée avant la diminution {universite_instance.list_etudiant.get(etudiant).recuperer_planning().horaire_entree}\n")
                                            universite_instance.list_etudiant.get(etudiant).recuperer_planning().dim_hor_ent(dim)
                                            print(f"Horaire entrée après la diminution {universite_instance.list_etudiant.get(etudiant).recuperer_planning().horaire_entree}\n")
                                            
                                            menu = int(input(f"\nTapez 0 pour retourner au menu principal\n"))
                                            if(menu == 0):
                                                self.app_main_menu()
                                        case 1:
                                            aug = int(input("\nHoraire Entrée: Combien d'heures voulez vous augmenter?\n"))
                                            print(f"Horaire entrée avant l'augmentation {universite_instance.list_etudiant.get(etudiant).recuperer_planning().horaire_entree}\n")
                                            universite_instance.list_etudiant.get(etudiant).recuperer_planning().aug_hor_ent(aug)
                                            print(f"Horaire entrée après l'augmentation {universite_instance.list_etudiant.get(etudiant).recuperer_planning().horaire_entree}\n")
                                            
                                            menu = int(input(f"\nTapez 0 pour retourner au menu principal\n"))
                                            if(menu == 0):
                                                self.app_main_menu()
                                        case 3:
                                            aug = int(input("\nHoraire Sortie: Combien d'heures voulez vous augmenter?\n"))
                                            print(f"Horaire sortie avant l'augmentation {universite_instance.list_etudiant.get(etudiant).recuperer_planning().horaire_sortie}\n")
                                            universite_instance.list_etudiant.get(etudiant).recuperer_planning().aug_hor_sort(aug)
                                            print(f"Horaire sortie après l'augmentation {universite_instance.list_etudiant.get(etudiant).recuperer_planning().horaire_sortie}\n")
                                            
                                            menu = int(input(f"\nTapez 0 pour retourner au menu principal\n"))
                                            if(menu == 0):
                                                self.app_main_menu()
                                        case 4:
                                            aug = int(input("\nHoraire Sortie: Combien d'heures voulez vous Diminuer?\n"))
                                            print(f"Horaire sortie avant la diminution {universite_instance.list_etudiant.get(etudiant).recuperer_planning().horaire_sortie}\n")
                                            universite_instance.list_etudiant.get(etudiant).recuperer_planning().dim_hor_sort(aug)
                                            print(f"Horaire sortie après la diminution {universite_instance.list_etudiant.get(etudiant).recuperer_planning().horaire_sortie}\n")
                                            
                                else:
                                    print(f"Cet étudiant n'est pas dans la liste\n")

                                    menu = int(input(f"\nTapez 0 pour retourner au menu principal\n"))
                                    if(menu == 0):
                                            self.app_main_menu()
                        case _:...
           
            #dans le cas où l'acteur est un étudiant
            case 2:
                print(f"Liste des Etudiants de l'{universite_instance.nom} - qui êtes vous parmi cette liste?\n")
                
                #afficher la liste des etudiants dans le dictionnaire 
                for key in universite_instance.list_etudiant:
                    print(key)
                
                print(f"\nSaissisez votre prenom tel que dans la liste\n")
                #recuperation du prenom
                login = input().capitalize()
                
                if universite_instance.list_etudiant.get(login):
                    print(f"Bonjour, {login} vous êtes un étudiant de l'{universite_instance.nom}\n")
                    menu_items = [
                                "1) Consulter les notes",
                                "2) Demissioner"
                               ]
                                    
                    self.menu(menu_items)
                    uc = int(input())

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
                
                print(f"\nSaissisez votre prenom tel que dans la liste\n")
                #recuperation du prenom
                login = input().capitalize()
                
                if universite_instance.list_enseignant.get(login):
                    print(f"Bonjour, {login} vous êtes un enseignant de l'{universite_instance.nom}\n")
                    menu_items = [
                                "1) Pour valider année d'un étudiant",
                                "2) Pour redoubler un étudiant"
                               ]
                                    
                    self.menu(menu_items)
                    ucEnseignant = int(input())

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
    
    #permet d'afficher un carré dans chaque menu de l'application
    def menu(self, menu_items):
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


    def app_main_menu(self):
        menu_items = [
        "1) Start Application",
        "2) Options",
        "3) Quit"]

        self.menu(menu_items)
    
        user_choice = int(input("\n"))

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