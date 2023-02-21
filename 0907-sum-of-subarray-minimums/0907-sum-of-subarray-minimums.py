class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        MOD = 10 ** 9 + 7
        ans = 0
        for i in range(len(arr) + 1):
                while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]  ): 
                    mid = stack.pop()
                    prev_smaller = mid + 1 if not stack else mid  - stack[-1]
                    next_smaller = i - mid
                    contribution = arr[mid] * next_smaller  * prev_smaller 
                    ans = ans + contribution
                stack.append(i)
        
        return ans % MOD