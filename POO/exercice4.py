import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"


class PaquetDeCartes:
    def __init__(self):
        self.cartes = []
        for couleur in ["Coeur", "Carreau", "Pique", "Trefle"]:
            for valeur in ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]:
                self.cartes.append(Carte(valeur, couleur))

    def melanger(self):
        random.shuffle(self.cartes)

    def distribuer(self, nombre_cartes_par_joueur, joueurs):
        cartes_distribuees = {joueur: [] for joueur in joueurs}
        for i in range(nombre_cartes_par_joueur):
            for joueur in joueurs:
                carte = self.cartes.pop()  # Retire la carte du paquet
                cartes_distribuees[joueur].append(carte)  # Associe la carte au joueur
        return cartes_distribuees

#implém
paquet = PaquetDeCartes()
paquet.melanger()

nombre_joueurs = 2
nombre_cartes_par_joueur = 5

joueurs = ["Hamilton", "Verstappen"]

cartes_distribuees = paquet.distribuer(nombre_cartes_par_joueur, joueurs)

for joueur, cartes in cartes_distribuees.items():
    print(f"{joueur} a reçu :")
    for carte in cartes:
        print(carte)
