class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic , stack = {} , []
        result = []
        for num2 in nums2:
            while stack and stack[-1] < num2:
                dic[stack[-1]] = num2
                # stack[-1] = num2
                stack.pop()
            if stack:
                stack.append(num2)
                
            if not stack:
                stack.append(num2)
        
        for num in nums1:
            print(num)
            if num not in dic:
                result.append(-1)
            else:
                result.append(dic[num])
       
        return result
                
     