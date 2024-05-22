import re

def validMyInternationalPhone(phone_number, country_code):
  # Expressions régulières pour num fr et US
  regex_phone_number_fr = r"^\+33[0-9]{9}$"
  regex_phone_number_us = r"^\+1[0-9]{10}$"

  # Vérif du num de téléphone français
  if country_code == "FR" and re.match(regex_phone_number_fr, phone_number):
    return True

  elif country_code == "US" and re.match(regex_phone_number_us, phone_number):
    return True

  else:
    return False

#utilisation
numéro_fr_valide = "+33601234567"
numéro_fr_invalide = "+331234567"
numéro_us_valide = "+12123456789"
numéro_us_invalide = "+1123456789"

print(f"Numéro français '{numéro_fr_valide}' valide pour la France ? : {validMyInternationalPhone(numéro_fr_valide, 'FR')}")
print(f"Numéro français '{numéro_fr_invalide}' valide pour la France ? : {validMyInternationalPhone(numéro_fr_invalide, 'FR')}")
print(f"Numéro américain '{numéro_us_valide}' valide pour les Etats-Unis ? : {validMyInternationalPhone(numéro_us_valide, 'US')}")
print(f"Numéro américain '{numéro_us_invalide}' valide pour les Etats-Unis ? : {validMyInternationalPhone(numéro_us_invalide, 'US')}")
