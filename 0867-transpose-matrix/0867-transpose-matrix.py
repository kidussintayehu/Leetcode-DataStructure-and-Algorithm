class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for col in range(len(matrix[0])):
                res.append([matrix[row][col]  for row in range(len(matrix)) ])
        return res
        
        