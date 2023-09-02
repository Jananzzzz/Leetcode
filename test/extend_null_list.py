a = []
m = [[]]
b = [1, 2, 3]
b.extend(a)
print(b)    # [1, 2, 3]
b.extend(m)
print(b)    # [1, 2, 3, []]
b.extend(m[0])
print(b)    # [1, 2, 3, []]