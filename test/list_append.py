a = [1, 2, 3, 4]
b = [1, 2, 3]
c = [[1, 2], [3, 4]]

a1 = a.append(b)
a2 = a.append(b[:])
a3 = c.append(a)
a4 = a.append(5)

print(a1)   # None
print(a2)   # None
print(a3)   # None
print(a4)   # None
print(a)    # [1, 2, 3, 4, [1, 2, 3], 5]

# Conclusion: list.append() returns None, and it modifies the list in place.
# list.append() can append a list as an element to another list.

list0 = [1, 2, 3]
list1 = [4, 5, 6]

list2 = list1.append(list0)
print(list2)              # None
print(list1)                 # [4, 5, 6, [1, 2, 3]]

# the list.append() method is just an operation on the list, it does not return a new list.