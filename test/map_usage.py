nums = [1, 2, 3, 4, 5]

def square(num):
    return num ** 2

squared_nums = map(square, nums)
print(squared_nums)
print(type(squared_nums))   # map
print(list(squared_nums))   # [1, 2, 3, 4, 5]
print(tuple(squared_nums))  # ()
# ISSUE: when you first turn a map object to a list, the map object will become empty

# correct practice

squared_nums = map(square, nums)
print(squared_nums)
print(type(squared_nums))

# store the map object as a list before converting it to a tuple
nums_list = list(squared_nums)
nums_tuple = tuple(nums_list)

print(nums_list)    # [1, 2, 3, 4, 5]
print(nums_tuple)   # (1, 2, 3, 4, 5)

