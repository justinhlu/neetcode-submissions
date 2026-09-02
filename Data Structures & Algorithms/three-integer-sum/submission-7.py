class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # Dont forget to skip dupes
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums) - 1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur > 0:
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    newTrip = [nums[i], nums[l], nums[r]]
                    res.append(newTrip)
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
            
        return res