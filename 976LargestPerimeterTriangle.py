

from audioop import reverse


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        def checkTriangle(a:int,b:int,c:int) -> bool:
            if a+b>c and a+c>b and b+c>a:
                return True
            else:
                return False

        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            if checkTriangle(nums[i],nums[i+1],nums[i+2]): 
                return nums[i]+nums[i+1]+nums[i+2]
            else: 
                continue
        return 0