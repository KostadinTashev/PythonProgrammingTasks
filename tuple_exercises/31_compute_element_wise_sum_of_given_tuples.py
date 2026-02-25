t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1)

elementwise_sum = tuple(sum(x) for x in zip(t1, t2, t3))

print("Element-wise sum of the said tuples:")
print(elementwise_sum)