
class Personne: 
    number_instances = 0
    UNIVERSITE_NAME = "Universite PS"

    def __init__(self, prenom, age, fonction, planning):
        self._prenom = prenom
        self._age = age
        self._fonction = fonction
        self._planning = planning
    
    def demissioner(self, demission):
        if(demission == "Demissioner"):
            self._fonction = f"{self.prenom} est demissionaire"
    

    def recuperer_planning (self): 
        return self._planning

    # Getters
    @property # Decorator
    def prenom (self): 
        return self._prenom
    
    @property 
    def age (self): 
        return self._age
    
    @property 
    def fonction (self): 
        return self._fonction
    
    @property # Decorator
    def planning (self): 
        return self._planning
    

    # Setters
    @prenom.setter
    def prenom (self, value): 
        self._prenom = value

    @age.setter
    def age (self, value): 
        self._age = value 

    @fonction.setter
    def fonction (self, value): 
        self._fonction = value 

    @fonction.setter
    def planning (self, value): 
        self._planning = value 
    

    
class Planning: 
    number_instances = 0
    UNIVERSITE_NAME = "Universite PS"

    def __init__(self, horaire_entree:int = 8, horaire_sortie:int = 16):
        self._horaire_entree = horaire_entree
        self._horaire_sortie = horaire_sortie

    def aug_hor_ent(self, aug):
        self._horaire_entree += aug
    
    def aug_hor_sort(self, aug):
        self._horaire_sortie += aug

    def dim_hor_ent(self, dim):
        self._horaire_entree -= dim
    
    def dim_hor_sort(self, dim):
        self._horaire_sortie -= dim

    # Getters
    @property # Decorator
    def horaire_entree (self): 
        return self._horaire_entree
    
    @property # Decorator
    def horaire_sortie (self): 
        return self._horaire_sortie
    
    # Setters
    @horaire_entree.setter
    def horaire_entree (self, value): 
        self._horaire_entree = value

    @horaire_sortie.setter
    def horaire_sortie (self, value): 
        self._horaire_sortie = value


