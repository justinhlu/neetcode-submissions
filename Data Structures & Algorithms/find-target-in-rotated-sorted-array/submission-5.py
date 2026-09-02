class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1

        def binary_search(l,r) -> int:
            while l <= r:
                mid = (l+r) // 2

                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid -1 
                else:
                    return mid
            return -1
        
        l = 0
        r = len(nums) - 1
        pivot = -1
        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = l

        res = binary_search(0, pivot)

        if res != -1:
            return res
        
        return binary_search(pivot, len(nums)-1)