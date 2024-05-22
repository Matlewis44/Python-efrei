import random

class JeuDeDevinette:
    def __init__(self):
        self.nombre_mystere = random.randint(1, 100)
        self.essais_restants = 10

    def jouer(self):
        while self.essais_restants > 0:
            try:
                proposition = int(input("Entre une proposition (entre 1 et 100) : "))
                if proposition < 1 or proposition > 100:
                    raise ValueError
            except ValueError:
                print("Saisie invalide. Fourni un nombre entre 1 et 100 gros bêta :(")
                continue

            if proposition == self.nombre_mystere:
                print("Bien ouej ! Tu as su décelé le nombre mystère !")
                break
            elif proposition < self.nombre_mystere:
                print("Trop petit ! Essaie encore.")
            else:
                print("Trop grand ! Essaie encore.")

            self.essais_restants -= 1

        if self.essais_restants == 0:
            print(f"Eh non perdu ! Le nombre mystère était {self.nombre_mystere}.")

#implém
if __name__ == "__main__":
    jeu = JeuDeDevinette()
    jeu.jouer()