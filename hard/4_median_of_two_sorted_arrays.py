# https://leetcode.com/problems/median-of-two-sorted-arrays/description/


# [1, 2, 3, 5, 10, 13, 15, 19]
# [2, 4, 5, 8, 10, 12, 19]

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1) # what an elegant solution
        n = n1 + n2
        left = (n1 + n2 + 1) // 2 # half of the array
        low, high = 0, n1
        
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            
            l1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            r1 = float('inf') if mid1 == n1 else nums1[mid1]
            r2 = float('inf') if mid2 == n2 else nums2[mid2]
            
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0.0


print(Solution.findMedianSortedArrays(Solution(), nums1=[1, 1, 1, 1, 2, 3, 5, 10, 13, 15, 19], nums2=[2, 4, 5, 8, 10, 12, 19]))
print(Solution.findMedianSortedArrays(Solution(), nums1 = [1,3], nums2 = [2]))
