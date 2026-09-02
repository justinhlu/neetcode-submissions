class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        res = 0
        for num in nums:
            numSet.add(num)
        
        for num in nums:
            if num-1 not in numSet:
                seq = []
                seq.append(num)
                currNum = num
                checkNum = currNum+1
                while checkNum in numSet:
                    seq.append(checkNum)
                    checkNum += 1
                
                res = max(res, len(seq))

        return res

