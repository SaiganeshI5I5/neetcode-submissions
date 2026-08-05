class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n =len(heights)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         dist = j - i
        #         ht =min(heights[i],heights[j])
        #         area = dist * ht
        #         if area > max_area:
        #             max_area = area
        # return max_area
        l , r = 0 ,n-1
        while l < r:
            dist = r - l
            ht = min(heights[l],heights[r])
            area = dist * ht
            if area > max_area:
                    max_area = area

            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

