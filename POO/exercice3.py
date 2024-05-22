import random

class JeuDePendu:
    def __init__(self, mot):
        self.mot = mot.upper()
        self.mot_masque = ["_" for _ in range(len(self.mot))]
        self.lettres_incorrectes = []
        self.vies_restantes = 6

    def jouer(self):
        while self.vies_restantes > 0 and "_" in self.mot_masque:
            print(f"\nMot masqué : {' '.join(self.mot_masque)}")
            print(f"Lettres incorrectes : {' '.join(self.lettres_incorrectes)}")
            print(f"Vies restantes : {self.vies_restantes}")

            lettre = input("Fourni une lettre : ").upper()
            if len(lettre) != 1 or not lettre.isalpha():
                print("Saisie invalide. Il faut fournir une seule lettre.")
                continue

            if lettre in self.mot_masque:
                print("Cette lettre est déjà devinée.")
                continue

            if lettre in self.mot:
                for i, c in enumerate(self.mot):
                    if c == lettre:
                        self.mot_masque[i] = lettre
                print("Bonne lettre !")
            else:
                if lettre not in self.lettres_incorrectes:
                    self.lettres_incorrectes.append(lettre)
                    self.vies_restantes -= 1
                    print("Mauvaise lettre.")
                else:
                    print("Vous avez déjà essayé cette lettre.")

        if "_" not in self.mot_masque:
            print(f"Bravo c'est bien cela ! Mot trouvé : {self.mot}")
        else:
            print(f"Hélas vous avez perdu ! Le mot était : {self.mot}")

#implém
if __name__ == "__main__":
    mots = ["PYTHON", "PROGRAMMATION", "OPPORTUNISTE", "ALGORITHME", "INADVERTENCE"]
    mot_a_trouver = random.choice(mots)
    
    jeu = JeuDePendu(mot_a_trouver)
    jeu.jouer()
