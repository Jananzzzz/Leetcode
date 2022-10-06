from multiprocessing.reduction import duplicate


class Solution:
    def threeSum(nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []
        ans = set()
        nums.sort()

        for i, target in enumerate(nums):
            if i > 0 and nums[i-1] == target:
                continue
            prev = set()
            for j in range(i+1, len(nums)):
                diff = -target - nums[j]
                if diff in prev:
                    ans.add((nums[j], diff, target))
                prev.add(nums[j])
        
        return ans 

# above is threeSum to zero
# below is threeSum to K (finalTarget) 
class Solution2:
    def threeSum(nums: list[int], finalTarget: int) -> list[list[int]]:
        if len(nums) < 3:
            return []
        ans = set()
        nums.sort()

        for i, target in enumerate(nums):
            if i > 0 and nums[i-1] == target:
                continue
            prev = set()
            for j in range(i+1, len(nums)):
                diff = finalTarget -target - nums[j]
                if diff in prev:
                    ans.add((nums[j], diff, target))
                prev.add(nums[j])
        
        return ans 

# list version(return with a list) 
# difference between list and set
# list           set
# []             ()
# duplicate      no duplicate
# append         add 





class Solution3:
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


x = Solution
res1 = x.threeSum([1,-1,0,0,2,-1])
print(res1)

y = Solution2
res2 = y.threeSum([1,2,-1,2,3,4,-2,0,0,3], 3)
print(res2)
print(type(res2))

y = Solution3
res3 = y.threeSum([1,2,-1,2,3,4,-2,0,0,3], 20)
print(res3)
print(type(res3))




