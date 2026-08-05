class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n =len(height)
        for i in range(n):
            leftmax = 0
            rightmax = 0
            for j in range(i+1):
                if height[j] > leftmax:
                    leftmax = height[j]
            for j in range(i,n):
                if height[j] > rightmax:
                    rightmax = height[j]
                
            trapped = min(leftmax,rightmax) - height[i]

            if trapped > 0:
                water += trapped
        return water  

        