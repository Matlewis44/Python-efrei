def computeSurfaceM2(base, hauteur):
  if not isinstance(base, (int, float)) or not isinstance(hauteur, (int, float)):
    return "Erreur: Les arguments doivent être des nombres."

  surface = base * hauteur
  return f"Votre surface est de {surface:.2f} m2"

print(computeSurfaceM2(50, 70))
