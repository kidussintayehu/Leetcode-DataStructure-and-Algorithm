class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [ 0 ]* len(temperatures)
        for i , temp in enumerate(temperatures):
            if not stack:
                stack.append([temp, i])   
            if stack[-1][0] > temp:
                stack.append([temp, i])
            else:
                while stack and temp > stack[-1][0]:
                    x = stack.pop()
                    ans[x[1]] = i - x[1]
                stack.append([temp , i])
        
        return ans
        
            