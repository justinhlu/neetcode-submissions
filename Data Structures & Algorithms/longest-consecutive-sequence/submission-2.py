class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i]-1 not in numSet:
                seq = []
                seq.append(nums[i])
                checkNum = nums[i] + 1
                while checkNum in numSet:
                    seq.append(checkNum)
                    checkNum += 1
                res = max(res, len(seq))

        return res
