my_list= ["1/2", "2/3", "3/5"]

print([tuple(map(int, fraction.split("/"))) for fraction in my_list])

new_list = [fraction.split('/') for fraction in my_list]
print(new_list)


nums_list = list(map(int, "2/5".split("/")))
tuple_list = tuple(map(int, "2/5".split("/")))
print(nums_list)
print(tuple_list)