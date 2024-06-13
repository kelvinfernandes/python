from etudiant import Etudiant
from enseignant import Enseignant
from personnel import Personnel

class Universite: 
    # Class attributes
    number_instances = 0
    UNIVERSITE_NAME = "Universite PS"

    #Constructeur
    def __init__(self, list_etudiant, 
                 list_enseigant, 
                 list_personnel,
                 nom:str = "Universite Paris Saclay",
                 lieu:str = "Orsay",
                 annee_creation:int = 2020):
        
        self._list_etudiant = list_etudiant
        self._list_enseignant = list_enseigant
        self._list_personnel = list_personnel
        
        self._nom = nom
        self._lieu = lieu
        self._annee_creation = annee_creation


    # Methods
    def ajouter_formation(): ...
    def fermer_formation(): ...
    def licencier_personnel(self, personnel_a_demissioner): 
        self._list_personnel.get(personnel_a_demissioner).demissioner("Demissioner")
        

     # Getters
    @property # Decorator
    def list_etudiant (self): 
        return self._list_etudiant
    
    @property # Decorator
    def list_enseignant (self): 
        return self._list_enseignant
    
    @property # Decorator
    def list_personnel (self): 
        return self._list_personnel
    
    @property # Decorator
    def list_etudiant (self): 
        return self._list_etudiant
    
    @property # Decorator
    def nom (self): 
        return self._nom
    
    @property # Decorator
    def lieu (self): 
        return self._lieu
    
    @property # Decorator
    def annee_creation (self): 
        return self._annee_creation

    #setter

    @list_etudiant.setter
    def age (self, value): 
        self._list_etudiant = value 

    @list_enseignant.setter
    def age (self, value): 
        self._list_enseignant = value 

    @list_personnel.setter
    def age (self, value): 
        self._list_personnel = value

    @nom.setter
    def nom (self, value): 
        self._nom = value 

    @lieu.setter
    def age (self, value): 
        self._lieu = value 

    @lieu.setter
    def annee_creation (self, value): 
        self._annee_creation = value 

