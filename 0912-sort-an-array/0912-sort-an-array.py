class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        cnt = {}
        
        minVal, maxVal = min(nums), max(nums)
        
        for val in nums:
            cnt[val] = cnt.get(val, 0) + 1
            
        index = 0
        
        for val in range(minVal, maxVal + 1, 1):          
            while cnt.get(val , 0) > 0:
                nums[index] = val
                index += 1
                cnt[val] -= 1
                
        return nums