import time

start_time = time.time()
print("int(8/3) equals to: ", int(8/3))             # 2
print("int(5/2) equals to: ", int(5/3))             # 1
print("int(3/2) equals to: ", int(3/2))             # 1
end_time = time.time()
print("Time elapsed: ", end_time - start_time)

# round down
start_time = time.time()
print("8//3 equals to: ", 8//3)
print("5//2 equals to: ", 5//2)
end_time = time.time()
print("Time elapsed: ", end_time - start_time)

# round up
print("3//2 equals to: ", -(-3//2))
print("5//2 equals to: ", -(-5//2))

print(int(0.3))
print(int(0.5))
print(int(0.7))