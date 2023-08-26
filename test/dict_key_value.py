dict = {
    1: "first element",
    2: "second element",
    3: "third element",
}

print(dict.keys())          # dict_keys([1, 2, 3])
print(dict.values())        # dict_values(['first element', ..., 'third element'])
print(type(dict.keys()))    # <class 'dict_keys'>
print(list(dict.keys()))    # [1, 2, 3]