class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        singleArray = []
        ans = []        
        

        
        for i in range(row):
            for j in range(col):
                singleArray.append(mat[i][j])
        if len(singleArray) != r * c:
            return mat      
        else:
            for k in range(0 , len(singleArray) , c):
                ans.append(singleArray[k: k + c ])

        return ans