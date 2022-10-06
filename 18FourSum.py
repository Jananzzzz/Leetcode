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
        