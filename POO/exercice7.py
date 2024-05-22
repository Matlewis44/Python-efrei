class Animal:
    def __init__(self, nom, nourriture_preferee):
        self.nom = nom
        self.nourriture_preferee = nourriture_preferee

    def manger(self):
        print(f"{self.nom} mange des {self.nourriture_preferee}.")

class Zoo:
    def __init__(self):
        self.animaux = []

    def ajouter_animal(self, animal):
        self.animaux.append(animal)

    def nourrir_animaux(self):
        for animal in self.animaux:
            animal.manger()

    def afficher_animaux(self):
        print("Liste des animaux du zoo :")
        for animal in self.animaux:
            print(f"- {animal.nom} : {animal.nourriture_preferee}")

#implém
zoo = Zoo()

zoo.ajouter_animal(Animal("Panda", "bambou"))
zoo.ajouter_animal(Animal("Makake", "bananes"))
zoo.ajouter_animal(Animal("Lion", "bonnes viandes"))

zoo.nourrir_animaux()
zoo.afficher_animaux()
