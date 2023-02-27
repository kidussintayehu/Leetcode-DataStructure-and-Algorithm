class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:    
        i = len(arr) - 1
        temp = 0
        g = -1
        while i >= 0:
            temp = arr[i]
            arr[i] = g
            if g < temp:
                g = temp
            i -= 1
            
        return arr