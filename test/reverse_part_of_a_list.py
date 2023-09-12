a = [1, 2, 3, 4, 5]

a.reverse()
print(a)

a.reverse()
print(a)

# can't use .reverse() to directly reverse part of a python list


a[:] = a[::-1]
print(a)