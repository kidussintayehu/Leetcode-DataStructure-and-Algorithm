class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt = {}
        ans = []
        size = 0
        for i in range(len(s) - 1, -1 , -1):
            if s[i] not in cnt:
                cnt[s[i]] = i
                
        # print(cnt)
        # end = cnt[s[0]]
        # for j in range(s):
        #     # end = max(end , cnt[s[0]])
        #     if cnt[s[j]] > end:
        #         end = cnt[s[j]]
        #     elif size == end:
        #         ans.append(size + 1)
        #         size = 0
        #         end = 
        #         size += 1
        right = cnt[s[0]]
        left = 0
        while right < len(s) and left < len(s):
            right = max(right , cnt[s[left]])
            if left == right:
                ans.append(right - size + 1)
                size = left + 1
                
            left += 1 
            
        return ans
                
            