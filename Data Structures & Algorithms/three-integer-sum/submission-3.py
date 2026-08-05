class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 r = [nums[i],nums[j],nums[k]]
        #                 r.sort()
        #                 if r not in res:
        #                     res.append(r)
        # return res
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n-1
            while l < r:
                sums= nums[i] + nums[l] + nums[r]
                if sums == 0:
                    res.append([nums[i],nums[l],nums[r]])

                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while r > l and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sums < 0:
                    l += 1
                else:
                    r -= 1

        return res
            
