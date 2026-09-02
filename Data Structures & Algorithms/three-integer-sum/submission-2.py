class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < len(nums) and l < r:
                check = nums[l] + nums[r]
                if -nums[i] == check:
                    newTriplet = [nums[i], nums[l], nums[r]]
                    res.add(tuple(newTriplet))
                    l += 1
                    r -= 1
                elif -nums[i] > check:
                    l += 1
                else:
                    r -= 1

        return list(res)