prix_initial = float(input("Entrez le prix initial de l'article: "))
remise_pourcentage = float(input("Entrez le pourcentage de remise: "))

remise = prix_initial * remise_pourcentage / 100
prix_final = prix_initial - remise

if prix_final > prix_initial / 2:
  print(f"Prix initial: {prix_initial:.2f}€")
  print(f"Remise: {remise:.2f}€")
  print(f"Prix final: {prix_final:.2f}€")
else:
  print("Erreur: la remise est trop élevée")
