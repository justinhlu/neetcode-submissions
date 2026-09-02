class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        l = 0
        r = n - 1
        leftMax = height[l]
        rightMax = height[r]
        totalWater = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                totalWater += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                totalWater += rightMax - height[r]
        
        return totalWater


                