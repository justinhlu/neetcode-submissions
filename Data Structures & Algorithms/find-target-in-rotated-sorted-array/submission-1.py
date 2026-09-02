class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        res = -1
        pivot = -1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l
        
        def binary_search(left, right) -> int:
            res = -1
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid

            return res

        res = binary_search(0, pivot-1)

        if res != -1:
            return res
        
        return binary_search(pivot, len(nums)-1)

        return res