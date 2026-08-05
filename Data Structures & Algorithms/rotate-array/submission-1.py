class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l,r = 0,len(nums) -1
        n = len(nums)
        k = k%n
        def rev(l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l,r = l+1,r-1
        
        rev(0,n-k-1)
        rev(n-k,n-1)
        rev(0,n-1)
