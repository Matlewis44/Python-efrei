choix1 = input("Voulez-vous partir à l'aventure (1) ou rester chez vous (2) ? ")

if choix1 == "1":
  choix2 = input("Rencontrez-vous un dragon (1) ou un marcheur_blanc (2) ? ")
  if choix2 == "1":
    choix3 = input("Le dragon est-il amical (1) ou hostile (2) ? ")
    if choix3 == "1":
      print("Tel un Targaryen devenez ami avec le dragon et vivez de belles aventures !")
    else:
      print("Drakkaris - Le dragon vous brûle et vous dévore brutalement !")
  else:
    choix3 = input("Le marcheur_blanc est-il intelligent (1) ou stupide (2) ? ")
    if choix3 == "1":
      print("Le marcheur_blanc vous aide à trouver un trésor caché et vous devenez riche !")
    else:
      print("Le marcheur_blanc vous trompe et vous vole tout ce que vous possédez !")
else:
  choix2 = input("Restez-vous chez vous à regarder un film (1) ou à lire un livre (2) ? ")
  if choix2 == "1":
    choix3 = input("Le film est-il une comédie (1) ou un thriller (2) ? ")
    if choix3 == "1":
      print("Vous passez un bon moment de détente et oubliez tous vos soucis !")
    else:
      print("Le thriller vous tient en haleine jusqu'à la fin et vous avez du mal à dormir !")
  else:
    choix3 = input("Le livre est-il un roman (1) ou un essai (2) ? ")
    if choix3 == "1":
      print("Vous êtes transporté dans un autre monde et vivez des aventures extraordinaires par procuration !")
    else:
      print("L'essai vous donne : La grande réponse sur la vie, l’univers et le reste !")
