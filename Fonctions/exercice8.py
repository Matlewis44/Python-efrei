def fibonacci_recursive_avec_limite(n, limite):
  if limite == 0:
    return []
  elif limite == 1:
    return [0, 1]
  else:
    return [n, fibonacci_recursive_avec_limite(n + 1, limite - 1)] + fibonacci_recursive_avec_limite(n + 1, limite - 2)

# Exemple d'utilisation
limite = 5
resultat = fibonacci_recursive_avec_limite(0, limite)
print(f"Suite de Fibonacci jusqu'à la limite {limite} : {resultat}")
