import random

#générer un nombre aléatoire entre 1 et 42
rand = random.randint(1, 42)
#comparaison rand à 42 et on stocke le résultat (True ou False) dans la variable reponse42.
reponse42 = rand == 42

#affichera True si c'est 42 sinon False
print(reponse42)
