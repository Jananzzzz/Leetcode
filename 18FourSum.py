def kSum(nums: List[int], target: int, k: int) -> list[list[int]]:
    res = []
    
    if not nums:
        return res
        
    average_value = target//k
    if average_value > nums[-1] or average_value < nums[0]:
        return res
        
    if k == 2:         # reach the bottom of the recursion
        return twoSum(nums, target)
        
    for i in range(len(nums)):
        if i == 0 or nums[i-1] != nums[i]:
            for subset in kSum(nums[i+1:], target -= nums[i], k - 1):
                res.append([nums[i]]+subset]
    
    return res


def twoSum(nums: list[int], target: int) -> list[list[int]]:

    nums = sorted(nums)
    res = []

    lo = 0
    hi = len(nums)-1
    while lo < hi:
        if nums[lo] + nums[hi] < target: # or (lo > 0 and nums[lo] == nums[lo - 1]):
            lo += 1
        elif nums[lo] + nums[hi] >  target: # or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
            hi -= 1
        else:
            res.append([nums[lo], nums[hi]])
            lo += 1
            hi -= 1

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> list[list[int]]:
            res = []

            if not nums:
                return res

            average_value = target//k
            if average_value > nums[-1] or average_value < nums[0]:
                return res

            if k == 2:         # reach the bottom of the recursion
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i+1:], target - nums[i], k - 1):
                        res.append([nums[i]]+subset)

            return res
                                   
        def twoSum(nums: list[int], target: int) -> list[list[int]]:
    
            nums = sorted(nums)
            res = []

            lo = 0
            hi = len(nums)-1
            while lo < hi:
                if nums[lo] + nums[hi] < target: # or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif nums[lo] + nums[hi] >  target: # or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

            return res
                                
        nums.sort()
        return kSum(nums, target, 4)
                         





'''
# call the threeSum function 
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        ans = []

        # threesum function here
        def threeSum(nums: list[int], finalTarget: int) -> list[list[int]]:
            if len(nums) < 3:
                return []
            ans = []
            nums.sort()

            for i, target in enumerate(nums):
                if i > 0 and nums[i-1] == target:
                    continue
                prev = set()
                for j in range(i+1, len(nums)):
                    diff = finalTarget -target - nums[j]
                    if diff in prev:
                        ans.append([nums[j], diff, target])
                    prev.add(nums[j])

            # remove duplicate:
            newlist = []
            for i in ans:
                if i not in newlist:
                    newlist.append(i)
            ans = newlist

            return ans 


        for i in range(len(nums)-3):
            if i>0 and nums[i-1] == nums[i]:
                continue
            # if threeSum(nums[i+1:], target-nums[i]) != []:
            threesum = threeSum(nums[i+1:], target-nums[i])
            for j in threesum:
                j.append(nums[i])
                ans.append(j)

        return ans 
'''       