class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 1
        cnt = 1
        s = chars[0]
        while i < len(chars):
            prev = chars[i - 1]
            cur = chars[i]
            if prev == cur:
                cnt += 1
            else:
                if cnt != 1:
                    s += str(cnt)
                    cnt = 1
                s += cur
                    
            i += 1
        if cnt > 1:
            s += str(cnt)
            
        for i in range(len(s)):
            chars[i] = s[i]
            
        return len(s)
            
            