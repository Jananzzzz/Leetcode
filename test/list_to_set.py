a = [1, 2, 2, 3]
a = set(a)
print(a)

b = [{1, 2}, {2, 3}]
# b = set(b) # error: unhashable
# print(b)

c1 = [[1, 2], [2, 1]]
# c = set(c) # error: unhashable
# print(c)

c = set()
c.add(1)
print(c)
c.add(2)
print(c)
c.add(1)
print(c)
