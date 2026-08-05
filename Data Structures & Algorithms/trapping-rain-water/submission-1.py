class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n =len(height)
        # for i in range(n):
        #     leftmax = 0
        #     rightmax = 0
        #     for j in range(i+1):
        #         if height[j] > leftmax:
        #             leftmax = height[j]
        #     for j in range(i,n):
        #         if height[j] > rightmax:
        #             rightmax = height[j]
                
        #     trapped = min(leftmax,rightmax) - height[i]

        #     if trapped > 0:
        #         water += trapped
        # return water
        start = 0
        end = len(height) - 1

        leftMax = 0
        rightMax = 0
        totalWater = 0

        while start < end:

            leftMax = max(leftMax, height[start])
            rightMax = max(rightMax, height[end])

            if leftMax < rightMax:
                totalWater += leftMax - height[start]
                start += 1
            else:
                totalWater += rightMax - height[end]
                end -= 1

        return totalWater
                



        