# currently there no good python solutions:
# the best way to reduce the opeartion time is guessing the testcase:
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        # these lines are guessing the testcase:
        cur = sum(num[:3])                  
        if cur >= target:                   
            return cur                     
        
        cur = sum(num[-3:])
        if cur < target:
            return cur
        # above guessing
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum1 = num[i] + num[j] + num[k]
                if sum1 == target:
                    return sum1
                
                if abs(sum1 - target) < abs(result - target):
                    result = sum1
                
                if sum1 < target:
                    j += 1
                elif sum1 > target:
                    k -= 1
            
        return result


# a TLE method:
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = sys.maxsize
        res = 0

        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                x = nums[i] + nums[left] + nums[right] 
                if x == target:
                    return target
                if x < target:
                    left += 1
                    if diff > target - x:
                        diff = target - x
                        res = x
                if x > target:
                    right -= 1   
                    if diff > x - target:
                        diff = x - target
                        res = x

        return res
'''

