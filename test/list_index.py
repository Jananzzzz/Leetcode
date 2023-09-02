list0 = [[1, 2, 3], [4, 5, 6]]

# get list0 while removing the first and the last element of each sublist
list1 = [sublist[1:-1] for sublist in list0]
print(list1)