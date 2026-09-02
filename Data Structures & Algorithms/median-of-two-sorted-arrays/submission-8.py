class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        merged = nums1 + nums2
        merged.sort()

        if len(merged) % 2 == 0:
            index = (l1 + l2) // 2
            return (merged[index] + merged[index-1]) / 2.0
        else:
            index = (l1 + l2) // 2

            return merged[index]