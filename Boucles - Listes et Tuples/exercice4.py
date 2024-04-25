objet = {"a": 42, "b": 42, "c": 42, "d": 42}

accumulateur = 1

for key, valeur in objet.items():
  if key != "d":
    accumulateur *= valeur
  else:
    accumulateur -= 42

print(accumulateur) # Affiche 74046
