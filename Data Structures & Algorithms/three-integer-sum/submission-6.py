class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            l = 0
            r = len(nums) - 1

            while l < r and l != i and r != i:
                mySum = nums[i] + nums[l] + nums[r]

                if mySum < 0:
                    l += 1
                elif mySum > 0:
                    r -= 1
                else:
                    newTriplet = sorted([nums[i], nums[l], nums[r]])
                    res.add(tuple(newTriplet))
                    l += 1
                    r -= 1


        return list(res)