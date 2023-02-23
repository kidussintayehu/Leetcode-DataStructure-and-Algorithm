class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        for col_index in range(len(strs[0])):
            for row_index in range(1 , len(strs)):
                if strs[row_index][col_index] < strs[row_index - 1][col_index]:
                    result += 1
                    break
        
        return result
                        