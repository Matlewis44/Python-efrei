age = int(input("Entrez votre âge: "))

if age < 0:
  print("Vous n'êtes pas encore né !")
elif age < 18:
  print(f"Vous ne pouvez pas entrer vous n'êtes pas majeur vous avez {age} ans!")
else:
  if age >= 42:
    print("Vous êtes le nouveau patron de la boîte !")
  else:
    print(f"Vous pouvez entrer vous êtes majeur vous avez {age} ans!")
