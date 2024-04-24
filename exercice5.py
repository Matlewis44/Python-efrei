# Variable déterminant si une autre variable existe ou prend la valeur 42
try:
    existing_var: any
#si elle n’existe pas elle prend la valeur 42 à la place
except NameError:
    existing_var = 42