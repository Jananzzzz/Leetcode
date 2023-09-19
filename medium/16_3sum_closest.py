# https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        # return the closest distance to the target
        def two_sum_closest(nums: list[int], target) -> int:
            if len(nums) < 2:
                return float('inf')
            res_sum = float('inf')
            low = 0
            high = len(nums) - 1
            min_diff = float('inf')
            while low < high:
                temp = nums[low] + nums[high]
                diff = abs(target - temp)
                if diff < min_diff:
                    min_diff = diff
                    res_sum = temp
                if temp > target:
                    high -= 1
                elif temp < target:
                    low += 1
                else:
                    return target
            return res_sum

        diff_list = []
        for i in range(len(nums) - 2):
            diff_list.append(nums[i] + two_sum_closest(nums[i+1:], target - nums[i]))
            diff_list = sorted(diff_list, key=lambda x: abs(target - x))
        return diff_list[0]

print(Solution.threeSumClosest(Solution(), nums=[0, 1, 2], target=3))
print(Solution.threeSumClosest(Solution(), nums = [-1,2,1,-4], target = 1))
print(Solution.threeSumClosest(Solution(), nums = [1, 1, 1, 0], target = 100))
print(Solution.threeSumClosest(Solution(), nums = [0,0,0], target = 1))
