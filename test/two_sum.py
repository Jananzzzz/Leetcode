test_list = [1, 2, 3, -2, 4, 5]
target = 3

res = []
table = set()
for i in test_list:
    if target - i in table:
        res.append([i, target - i])
    else:
        table.add(i)

print(res)