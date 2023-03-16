class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        idx = 1
        right = 1
        
        while right < n:
            if nums[right - 1] != nums[right]:
                nums[idx] = nums[right]
                idx += 1
            right += 1

        return idx
