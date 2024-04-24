import random

rand = random.randint(0, 30)

if rand <= 10:
  print(f'{rand} Cool')
elif rand <= 20:
  print(f'{rand} Tepid')
else:
  print(f'{rand} Warm')
