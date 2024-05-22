def tableGenerator(liste_data):
  """
  Fonction qui génère un tableau matriciel à partir d'une liste Python à plusieurs dimensions.

  Args:
    liste_data: La liste Python à plusieurs dimensions contenant les données du tableau.

  Returns:
    Une chaîne de caractères représentant le tableau matriciel formaté.
  """

  # Obtenir le nombre de colonnes
  nb_colonnes = len(liste_data[0])

  # Générer les titres des colonnes
  titres_colonnes = [f"| {titre} " for titre in liste_data[0]]
  titre_tableau = "".join(titres_colonnes) + "|\n"

  # Générer les lignes du tableau
  lignes_tableau = ""
  for ligne in liste_data[1:]:
    ligne_formatee = ""
    for valeur in ligne:
      ligne_formatee += f"| {valeur:<10} "
    lignes_tableau += ligne_formatee + "|\n"

  # Combiner les titres et les lignes
  tableau_formate = titre_tableau + lignes_tableau + "|"

  return tableau_formate

# Exemple d'utilisation
donnees = [
  ["", "Nom", "Prénom", "Âge"],
  ["Data1", "Alice", "Robert", 32],
  ["Data1","Bob", "Martin", 25],
  ["Data1","Charlie", "Dupont", 40],
]

print(tableGenerator(donnees))
