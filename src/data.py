from base import Planning
from etudiant import Etudiant
from enseignant import Enseignant
from personnel import Personnel
from universite import Universite

class Data:
    TYPE_DATA = "Universite"

    def __init__(self):...

    def create_universite_instance(self):
            # Initialize students
            notes_kelvin = {"reseaux": "12", "developpement": "17", "systeme": "12", "Anglais": "14", "Droit": "12"}
            planning_kelvin = Planning(8, 16)
            kelvin = Etudiant("Kelvin", 25, "Etudiant", planning_kelvin, "IRS", 2020, 5, notes_kelvin)

            notes_john = {"reseaux": "14", "developpement": "15", "systeme": "13", "Anglais": "15", "Droit": "13"}
            planning_john = Planning(8, 16)
            john = Etudiant("John", 25, "Etudiant", planning_john, "Developpement web", 2020, 3, notes_john)

            notes_ponnappa = {"reseaux": "14", "developpement": "15", "systeme": "13", "Anglais": "15", "Droit": "13"}
            planning_ponnappa = Planning(8, 16)
            ponnappa = Etudiant("Ponnappa", 25, "Etudiant", planning_ponnappa, "IRS", 2020, 5, notes_ponnappa)

            # Initialize teachers
            planning_trevor = Planning(8, 16)
            trevor = Enseignant("Trevor", 35, "Enseignant", planning_trevor)

            planning_tarryn = Planning(8, 16)
            tarryn = Enseignant("Tarryn", 35, "Enseignant", planning_tarryn)

            planning_eugenia = Planning(8, 16)
            eugenia = Enseignant("Eugenia", 35, "Enseignant", planning_eugenia)

            # Initialize staff
            planning_yasmine = Planning(8, 16)
            jasmine = Personnel("Jasmine", 35, "Personnel", planning_yasmine)

            planning_taylor = Planning(8, 16)
            taylor = Personnel("Taylor", 35, "Personnel", planning_taylor)

            planning_allison = Planning(8, 16)
            allison = Personnel("Allison", 35, "Personnel", planning_allison)

            # Create lists
            list_etudiant = {"Kelvin": kelvin, "John": john, "Ponnappa": ponnappa}
            list_enseignant = {"Trevor": trevor, "Tarryn": tarryn, "Eugenia": eugenia}
            list_personnel = {"Jasmine": jasmine, "Taylor": taylor, "Allison": allison}

            # Create university instance
            universite_instance = Universite(list_etudiant, list_enseignant, list_personnel)
            
            return universite_instance
