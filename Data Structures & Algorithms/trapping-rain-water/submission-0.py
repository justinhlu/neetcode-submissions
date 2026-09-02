class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        totalWater = 0

        for i in range(n):
            leftMax = 0
            for j in range(i):
                leftMax = max(leftMax, height[j])
            
            rightMax = 0
            for j in range(i+1, n):
                rightMax = max(rightMax,height[j])
            
            waterLevel = min(leftMax, rightMax)

            if waterLevel > height[i]:
                totalWater += waterLevel - height[i]
            

        return totalWater