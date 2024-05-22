import random

class De:
    def __init__(self):
        pass

    def lancer(self):
        return random.randint(1, 6)

#implém
if __name__ == "__main__":
    de = De()
    
    print("Lance le dé 10 fois :")
    for i in range(10):
        resultat = de.lancer()
        print(f"Lancer {i+1}: {resultat}")