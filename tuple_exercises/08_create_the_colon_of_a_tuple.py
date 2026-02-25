from copy import deepcopy

tuplex = ("HELLO", 5, [], True)
print(tuplex)

tuplex_colon = deepcopy(tuplex)

tuplex_colon[2].append(100)
print(tuplex_colon)

print(tuplex)