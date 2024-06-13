from personne import Personne

class Etudiant(Personne): 
    def __init__(self, prenom, age, fonction,planning, date_inscription, annee_scolaire, notes):
        #heritage unique
        #super().__init__(prenom)
        #heritage multiple
        Personne.__init__(self, prenom, age, fonction, planning)
        self._date_inscription = date_inscription
        self._annee_scolaire = annee_scolaire
        self._notes = notes
    
    def valider_annee(self, a_valide): 
        if(a_valide):
            self._annee_scolaire += 1

    def redoubler(self, a_redouble): 
        if(a_redouble):
            self._annee_scolaire -= 1

    def consulter_notes(self): 
        return self._notes

    @property 
    def date_inscription (self): 
        return self._date_inscription
    
    @property 
    def annee_scolaire (self): 
        return self._annee_scolaire
    
    @property 
    def notes (self): 
        return self._notes

    # Setters
    @date_inscription.setter
    def date_inscription (self, value): 
        self._date_inscription = value
    
    @annee_scolaire.setter
    def annee_scolaire (self, value): 
        self._annee_scolaire = value

    @notes.setter
    def notes (self, value): 
        self._notes = value



    #getter
    #setter

