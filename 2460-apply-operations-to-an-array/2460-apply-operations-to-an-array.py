class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left , right = 0 , 1
        while right < len(nums):
            if nums[left] == nums[right]:
                nums[left] *= 2
                nums[right] = 0
                right += 2
                left += 2
            else:
                left +=1
                right += 1
                
        zeros = nums.count(0)
        for i in range(zeros):
            nums.remove(0)
        for i in range(zeros):
            nums.append(0)
        return nums