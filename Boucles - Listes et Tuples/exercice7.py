nbr = [5, 4, 3, 2, 1]

est_trie = False

while not est_trie:
  est_trie = True
  for i in range(len(nbr) - 1):
    if nbr[i] > nbr[i + 1]:
      nbr[i], nbr[i + 1] = nbr[i + 1], nbr[i]
      est_trie = False

print(nbr) # Affiche [1, 2, 3, 4, 5]
