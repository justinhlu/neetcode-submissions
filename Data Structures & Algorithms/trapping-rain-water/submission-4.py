class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        maxWater = 0
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        while l <= r:
            if leftMax < rightMax:
                leftMax = max(leftMax, height[l])
                maxWater += leftMax - height[l]
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                maxWater += rightMax - height[r]
                r -= 1
        
        return maxWater