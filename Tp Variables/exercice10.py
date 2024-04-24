#definition de variables de chaque type
myBool = True
myInt = 42
myFloat = 3.14
myString = "Hello World!"
myComplex = 1j + 2j

def detect_type(variable):
  #fonction type() pour obtenir le type de la variable.
  typeVar = type(variable)
  if typeVar == bool:
    return "boolean"
  elif typeVar == int:
    return "entier"
  elif typeVar == float:
    return "décimal"
  elif typeVar == str:
    return "chaîne de caractères"
  elif typeVar == complex:
    return "complexe"
  else:
    return "type inconnu"

#fonction detect_type() qui prend une variable en paramètre
print(detect_type(myBool))
print(detect_type(myInt))
print(detect_type(myFloat))
print(detect_type(myString))
print(detect_type(myComplex))
