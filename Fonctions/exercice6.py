def is_palindrome(chaine):
  # Converti chaîne en minuscules et supprimer les espaces
  chaine_sans_espaces = chaine.lower().replace(" ", "")

  # Vérifier si la chaîne inversée est égale à la chaîne d'origine
  return chaine_sans_espaces == chaine_sans_espaces[::-1]

# Exemples d'utilisation
mot1 = "radar"
mot2 = "bonbon"
mot3 = "bob"

print(f"{mot1} est-il un palindrome ? : {is_palindrome(mot1)}")
print(f"{mot2} est-il un palindrome ? : {is_palindrome(mot2)}")
print(f"{mot3} est-il un palindrome ? : {is_palindrome(mot3)}")
