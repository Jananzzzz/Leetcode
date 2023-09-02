a = [1, 2, 3]
a.reverse()
print(a) # [3, 2, 1]

b = [1, 2, 3]
c = b.reverse()
print(c) # None
print(b) # [3, 2, 1]

# reverse without modify the original list

my_list = [1, 2, 3]
new_list = my_list[::-1]
print(new_list) # [3, 2, 1]