ageDuMec = int(input("Entrez votre âge : "))

def detectMyAgeByNight(age):
  if age < 0:
    print("Erreur : L'âge ne peut pas être négatif.")
  elif age < 18:
    print(f"Vous ne pouvez pas entrer, vous n'êtes pas majeur. Vous avez {age} ans.")
  else:
    print(f"Vous pouvez entrer, vous êtes majeur. Vous avez {age} ans.")


detectMyAgeByNight(ageDuMec)