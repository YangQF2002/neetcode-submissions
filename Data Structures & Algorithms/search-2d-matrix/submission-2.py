# No flattening version 

# low = 0, 0, high = r - 1, c - 1

# 2D index -> convert to 1D index 
# Index: (ri, ci) -> ri * num_cols + ci 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        low = 0 
        high = (r - 1) * c + (c - 1)

        while low <= high: 
            mid = (low + high) // 2
            mid_r = mid // c 
            mid_c = mid % c 

            mid_val = matrix[mid_r][mid_c]
            if mid_val == target: 
                return True 
            elif mid_val > target: 
                high = mid - 1 
            else: 
                low = mid + 1 

        return False 
