class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (col > 0 and row > 0) and ( matrix[row][col] != matrix[row - 1][col - 1]):
                    return False
        return True                   