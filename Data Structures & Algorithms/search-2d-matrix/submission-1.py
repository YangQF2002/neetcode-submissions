# Flattened version 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix) 
        c = len(matrix[0])

        flattened = []
        for ri in range(r): 
            for ci in range(c): 
                cell = matrix[ri][ci]
                flattened.append(cell)
        
        low = 0 
        high = len(flattened) - 1

        while low <= high: 
            mid = (low + high) // 2
            mid_val = flattened[mid]

            if mid_val == target: 
                return True 
            elif mid_val > target: 
                high = mid - 1 
            else: 
                low = mid + 1
        
        return False 
    



        

        