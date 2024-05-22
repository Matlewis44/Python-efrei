import time

def calculate_time(func):
  def inner_function(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    total_time = end_time - start_time

    print(f"Temps d'exécution de la fonction '{func.__name__}': {total_time:.2f} secondes")
    return result

  return inner_function

# Exemple d'utilisation
@calculate_time
def ma_fonction(n):
  """
  Fonction d'exemple qui calcule le carré d'un nombre.
  """
  return n * n

ma_fonction(100)
