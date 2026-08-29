class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0 
    
        low = 0
        high = len(heights) - 1
        while low < high: 
            # Take a snapshot of the current area 
            # Update the result 
            lowerValue = min(heights[low], heights[high])
            area = lowerValue * (high - low)
            result = max(result, area)

            # Move the pointer that points to the lower height 
            # So that we can keep trying to maximize area
            if heights[low] < heights[high]:
                low += 1
            else: 
                high -= 1

        return result 

