class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l , r = 0, 1
        for i in range(len(nums)):
            while r < len(nums):
                if nums[l] > nums[r]:
                    nums[l] , nums[r] = nums[r] , nums[l]
                l += 1
                r += 1
                
            l = 0
            r = 1