class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        nums = sorted(nums)

        for i in range(len(nums)):
            l = 0
            r = len(nums)-1

            while l < r and l != i and r != i:
                currSum = nums[l] + nums[r] + nums[i]
                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    newTriplet = sorted([nums[l], nums[r], nums[i]])
                    res.add(tuple(newTriplet))
                    r -= 1
                    l += 1

        return list(res)