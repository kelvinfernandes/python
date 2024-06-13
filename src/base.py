
class Personne: 
    number_instances = 0
    UNIVERSITE_NAME = "Universite PS"

    def __init__(self, prenom, age, fonction):
        self._prenom = prenom
        self._age = age
        self._fonction = fonction
    
    def demissioner(self, demission):
        if(demission == "Demissioner"):
            self._fonction = f"{self.prenom} est demissionaire"

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
    

    
class Planning: ...

    #getter
    #setter


