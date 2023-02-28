class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_value = max(arr)
        i , j = 0 , 1
        while j < len(arr):
            if arr[i] == max_value:
                break
            if arr[i] >= arr[j]:
                return False
            i += 1
            j+= 1
        if i == 0 or i == len(arr) - 1:
            return False
        
        while j < len(arr):
            if arr[i] <= arr[j]:
                return False
            i += 1
            j += 1
            
        return True