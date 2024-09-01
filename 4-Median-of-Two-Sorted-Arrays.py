class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()

        n = len(nums3)
        mid = n // 2

        if n % 2 != 0:
            return float(nums3[mid])
        else:
            return float((nums3[mid-1] + nums3[mid]) / 2)