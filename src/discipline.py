from personne import Personne
from formation import Formation

class Planning: 
    number_instances = 0
    UNIVERSITE_NAME = "Universite PS"

    def __init__(self, list_etudiant, 
                 list_enseigant, 
                 list_personnel,
                 nom,
                 lieu,
                 anne_creation):
        self._list_etudiant = ["Kelvin","John", "Ponnappa", "Mia", "Peter", "Natalie", "Ang", "Nguta", "Tamzyn", "Salome"]
        self._list_enseigant = ["Trevor","Tarryn", "Eugenia", "Verona", "Jackie", "Maureen", "Desiree", "Daly", "Hayman", "Ruveni"]
        self._list_personnel = ["Jasmine","Taylor", "Allison", "Morgan", "Richard", "Morgan", "Cierra", "Ciara", "Paul", "Ericka"]
        self._nom = "Universite Paris Saclay"
        self._lieu = "Orsay"
        self._annee_creation = 2020
    
    def ajouter_formation(): ...
    def fermer_formation(): ...
    def licencier_personnel(): ...

    #getter
    #setter

