class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        ans = []
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hashMap:
                ans = [i , hashMap[temp]]
                return ans
            hashMap[nums[i]] = i