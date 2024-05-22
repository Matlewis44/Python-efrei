import random

class De:
    def lancer(self):
        return random.randint(1, 6)

class Joueur:
    def __init__(self, nom, solde_initial):
        self.nom = nom
        self.solde = solde_initial
        self.position = 0

    def payer(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            print(f"{self.nom} a payé {montant}")
        else:
            print(f"{self.nom} n'a pas assez d'argent pour payer {montant}")

class Case:
    def __init__(self, nom):
        self.nom = nom

class CaseAchetable(Case):
    def __init__(self, nom, prix_achat, loyer):
        super().__init__(nom)
        self.prix_achat = prix_achat
        self.loyer = loyer
        self.proprietaire = None

    def calculer_loyer(self):
        return self.loyer

class CaseSimple(Case):
    def __init__(self, nom):
        super().__init__(nom)

class Monopoly:
    def __init__(self, joueurs, cases):
        self.joueurs = joueurs
        self.cases = cases
        self.de = De()

    def jouer(self):
        while True:
            for joueur in self.joueurs:
                print(f"\nTour de {joueur.nom} :")
                nombre_case = self.de.lancer()
                print(f"{joueur.nom} a obtenu {nombre_case}")

                joueur.position = (joueur.position + nombre_case) % len(self.cases)
                current_case = self.cases[joueur.position]
                print(f"{joueur.nom} arrive sur la case {current_case.nom}")

                if isinstance(current_case, CaseAchetable):
                    if current_case.proprietaire is None:
                        print(f"{current_case.nom} est à vendre pour {current_case.prix_achat}")
                        choix_achat = input(f"{joueur.nom}, voulez-vous acheter {current_case.nom} ? (oui/non) : ")
                        if choix_achat.lower() == "oui" and joueur.solde >= current_case.prix_achat:
                            joueur.solde -= current_case.prix_achat
                            current_case.proprietaire = joueur
                            print(f"{joueur.nom} a acheté {current_case.nom}")
                    elif current_case.proprietaire != joueur:
                        loyer = current_case.calculer_loyer()
                        joueur.payer(loyer)
                        current_case.proprietaire.solde += loyer
                        print(f"{joueur.nom} a payé {loyer} à {current_case.proprietaire.nom} pour {current_case.nom}")

                if any(joueur.solde <= 0 for joueur in self.joueurs):
                    print(f"\nFin du jeu !")
                    vainqueur = max(self.joueurs, key=lambda j: j.solde)
                    print(f"Le vainqueur est {vainqueur.nom} avec un solde de {vainqueur.solde}")
                    return

#implém
joueurs = [Joueur("Hamilton", 1500), Joueur("Leclerc", 1000)]
cases = [
    CaseAchetable("Rue de la Paix", 2000, 50),
    CaseSimple("Gare"),
    CaseAchetable("Avenue Montaigne", 3000, 75),
    CaseSimple("Impôts"),
    CaseAchetable("Boulevard Haussmann", 4000, 100),
    CaseSimple("Prison"),
    CaseAchetable("Rue de Rivoli", 5000, 125),
    CaseSimple("Chance"),
    CaseAchetable("Champs-Elysées", 6000, 150),
]

jeu = Monopoly(joueurs, cases)
jeu.jouer()
