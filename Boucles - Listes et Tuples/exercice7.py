import datetime

# Obtenir l'année actuelle
annee_actuelle = datetime.datetime.now().year

# Créer une liste vide pour stocker les années
liste_annees = []

# Boucler de 1980 à l'année actuelle (incluse)
for annee in range(1980, annee_actuelle + 1):
  # Ajouter l'année à la liste
  liste_annees.append(annee)

# Afficher la liste des années
print(liste_annees)
