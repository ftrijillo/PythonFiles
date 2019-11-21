import itertools

friends = ['Monique', 'Ashish', 'Devon', 'Bernie', 'Frank', 'Sheena']

print("Permutations:", list(itertools.permutations(friends, r=2)))
print("Combinations:", list(itertools.combinations(friends, r=2)))
