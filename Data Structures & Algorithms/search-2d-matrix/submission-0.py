class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m , n = len(matrix), len(matrix[0])

        start = 0
        end = m * n - 1

        while start <= end:
            mid = (start + end) // 2

            row, col = mid // n, mid % n
            
            if matrix[row][col] > target:
                end = mid - 1
            elif matrix[row][col] < target:
                start = mid + 1
            else:
                return True
        
        return False