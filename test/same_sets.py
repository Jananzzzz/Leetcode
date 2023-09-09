a = (1, 2)
b = (2, 1)

print(a == b) # False
print(type(a)) # tuple

c = [1, 2]
d = [2, 1]
print(c == d) # False
print(set(c) == set(d)) # true
