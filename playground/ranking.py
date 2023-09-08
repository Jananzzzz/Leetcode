# all kinds of ranking algorithm from low to high

# bubbling
def bubble(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        for j in range(i, 0, -1): 
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums

def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        min_location = nums[i:].index(min(nums[i:]))
        nums[i], nums[min_location + i] = nums[min_location + i], nums[i] 
    return nums

# iterative merge two sorted list             
def merge_sort(nums: list[int]) -> list[int]:

    def merge_two_sorted(a: list[int], b: list[int]) -> list[int]:
        if len(a) == 0: return b
        if len(b) == 0: return a
        new_list = []
        a_index = 0
        b_index = 0
        while True:
            if a[a_index] < b[b_index]:
                new_list.append(a[a_index])
                a_index += 1
                if a_index == len(a):
                    new_list.extend(b[b_index:])
                    break
            else:
                new_list.append(b[b_index])
                b_index += 1
                if b_index == len(b):
                    new_list.extend(a[a_index:])
                    break
        return new_list

    mid = len(nums) // 2
    if mid == 0:
        return nums[mid:]
    return merge_two_sorted(merge_sort(nums[:mid]), merge_sort(nums[mid:]))

def quick_sort(nums: list[int]) -> list[int]:

    if len(nums) == 1:
        return nums
    pivot = nums[0]
    left = [i for i in nums if i <= pivot] 
    right = [i for i in nums if i > pivot]
    if right == []:
        left = nums[1:]
        right = [nums[0]]
    return quick_sort(left) + quick_sort(right)

    

if __name__=="__main__":

    nums = [2, 3, 9, 3, 4, 10, 1111, 3, 7]

    print("quick sort: ", quick_sort(nums), "\n")
    # print("bubbling: ", bubble(nums), "\n")
    # print("insertion sort: ", insertion_sort(nums), "\n")
    # print("selection sort: ", selection_sort(nums), "\n")
    # print("merge two sorted list: ", merge_two_sorted([2, 3, 5, 7], [0, 2, 4, 7]), "\n")
    # print("merge two sorted list: ", merge_two_sorted([2], []), "\n")
    # print("merge sort: ", merge_sort(nums), "\n")
