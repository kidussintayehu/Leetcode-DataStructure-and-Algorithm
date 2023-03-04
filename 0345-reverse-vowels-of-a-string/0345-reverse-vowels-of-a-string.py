class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        l, r = 0 , len(lst) - 1
        vowels = "aeiouAEIOU"
        while l < r:
            if lst[l] not in vowels:
                l += 1
            elif lst[r] not in vowels:
                r -= 1
            else:
                lst[l] , lst[r] = lst[r] , lst[l]
                l += 1
                r -= 1
        
        return "".join(lst)
                
        