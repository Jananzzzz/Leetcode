# given 4 different integer range from 1 t0 10
# return a way to calculate 24 using the 4 numbers and + - * / ( )

import itertools

def my_permutations(nums: list[int], position, ending):
    if position == ending:
        print(nums)
    else:
        for index in range(position, ending):
            nums[index], nums[position] = nums[position], nums[index] 
            my_permutations(nums, position+1, ending)
            nums[index], nums[position] = nums[position], nums[index] 

def calculate_24(nums: list[int, 4]):

    return False


nums = [1, 2, 3, 4]
result = [c for c in itertools.permutations(nums, 4)]
print(result)
# my_permutations(nums, 0, len(nums))


