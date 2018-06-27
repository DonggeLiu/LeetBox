class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not (len(matrix) and len(matrix[0])):
            return False
        row, col = 0, len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            row, col = row + (matrix[row][col] <= target), col - (matrix[row][col] > target)
        return False
