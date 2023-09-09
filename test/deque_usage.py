from collections import deque

my_deque = deque([1, 2, 3, 4, 5])
print(my_deque)
my_deque.append(6)
print(my_deque)
my_deque.appendleft(0)
print(my_deque)
pop_element = my_deque.pop()
print(my_deque)
left_pop = my_deque.popleft()
print(my_deque)

"""
deque([1, 2, 3, 4, 5])
deque([1, 2, 3, 4, 5, 6])
deque([0, 1, 2, 3, 4, 5, 6])
deque([0, 1, 2, 3, 4, 5])
deque([1, 2, 3, 4, 5])
"""