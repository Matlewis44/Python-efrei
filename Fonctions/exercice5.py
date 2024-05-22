import time

def afficher_heure_actuelle():
  """
  Fonction qui affiche l'heure actuelle en temps réel.
  """
  while True:
    # Obtenir l'heure actuelle
    heure_actuelle = time.localtime()

    # Formater l'heure en chaîne de caractères
    heure_str = time.strftime("%H:%M:%S", heure_actuelle)

    # Effacer affichage précédent
    print("\r", end="")

    # Affiche heure actuelle
    print(heure_str, end="")
    time.sleep(1)
