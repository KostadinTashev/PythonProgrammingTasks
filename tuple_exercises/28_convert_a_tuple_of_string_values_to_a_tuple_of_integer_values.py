tuple1 = (('333', '33'), ('1416', '55'))
tuple1 = tuple(tuple(int(x) for x in t) for t in tuple1)
print(tuple1)
