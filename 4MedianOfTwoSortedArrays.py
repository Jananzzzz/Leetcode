class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        for i in nums1:
            nums2.append(i)
        nums2.sort()
        k = len(nums2)
        
        if k%2 == 0:
            return (nums2[k//2-1] + nums2[k//2])/2
        if k%2 == 1:
            return nums2[k//2]