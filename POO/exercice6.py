class Personnage:
    def __init__(self, nom, sante, degats):
        self.nom = nom
        self.sante = sante
        self.degats = degats

    def attaquer(self, autre_personnage):
        print(f"{self.nom} attaque {autre_personnage.nom} et inflige {self.degats} dégâts.")
        autre_personnage.recevoir_degats(self.degats)

    def recevoir_degats(self, degats):
        self.sante -= degats
        print(f"{self.nom} reçoit {degats} dégâts. Santé restante : {self.sante}")

    def est_vivant(self):
        return self.sante > 0

class JeuDeCombat:
    def __init__(self, personnage1, personnage2):
        self.personnage1 = personnage1
        self.personnage2 = personnage2

    def jouer(self):
        tour = 1
        while self.personnage1.est_vivant() and self.personnage2.est_vivant():
            print(f"\n--- Tour {tour} ---")
            if tour % 2 != 0:
                self.personnage1.attaquer(self.personnage2)
            else:
                self.personnage2.attaquer(self.personnage1)
            
            tour += 1
        
        if self.personnage1.est_vivant():
            print(f"\n{self.personnage1.nom} a gagné le combat !")
        else:
            print(f"\n{self.personnage2.nom} a gagné le combat !")

#implém
personnage1 = Personnage("Optimus", 100, 15)
personnage2 = Personnage("Galvatron", 80, 20)

jeu = JeuDeCombat(personnage1, personnage2)
jeu.jouer()
