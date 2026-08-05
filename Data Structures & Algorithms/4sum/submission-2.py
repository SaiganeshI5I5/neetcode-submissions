class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # n = len(nums)
        # res = []

        # for a in range(n):
        #     for b in range(a + 1, n):
        #         for c in range(b + 1, n):
        #             for d in range(c + 1, n):
        #                 if nums[a] + nums[b] + nums[c] + nums[d] == target:
        #                     r = ([nums[a], nums[b], nums[c], nums[d]])
        #                     r.sort()
        #                     if r not in res:
        #                         res.append(r)
        # return res
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 3): 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = n - 1
                while l < r:
                    sums = nums[i] + nums[j] + nums[l] + nums[r]
                    if sums == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif sums < target: 
                        l += 1
                    else:
                        r -= 1
        return res