a = [1, 2, 3, 4]
b = [1, 2 ,3]
print(b.extend(a)) # None
print(b) # [1, 2, 3, 1, 2, 3, 4]

# same as append, extend is just an operation without any return value