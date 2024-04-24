
from datetime import datetime

jour = datetime.today().weekday()

match jour:
    case 0:
        print("Nous sommes lundi")
    case 1:
        print("Nous sommes mardi")
    case 2:
        print("Nous sommes mercredi")
    case 3:
        print("Nous sommes jeudi")
    case 4:
        print("Nous sommes vendredi")
    case 5:
        print("Nous sommes samedi")
    case 6:
        print("Nous sommes dimanche")

