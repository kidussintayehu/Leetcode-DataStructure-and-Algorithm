class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        srtd = sorted(nums)
        idx = {}
        ans = []
        for i  in range(len(srtd)):
            if srtd[i] not in idx:
                idx[srtd[i]] = i
            
        for i in range(len(nums)):
            ans.append(idx[nums[i]])
            
        return ans