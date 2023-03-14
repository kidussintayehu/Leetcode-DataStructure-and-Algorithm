class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i] , nums[i + 1] = nums[i + 1] , nums[i]
        
        ans = []
        
        for idx , val in enumerate(nums):
            if val == target:
                ans.append(idx)
        
        return ans