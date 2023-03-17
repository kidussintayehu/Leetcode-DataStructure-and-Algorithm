class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while i**2 <= c:
            sqr = i**2
            a=math.sqrt(c - sqr)
            if a == int(a):
                return True
            i += 1
            
        return False