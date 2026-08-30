# Sorted in non-decreasing order 
# Good basis to do two pointer, as we would know which pointer to shift 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0 
        high = len(numbers) - 1
        answer = None 

        while low <= high: 
            cur_sum = numbers[low] + numbers[high]
            if cur_sum == target: 
                # One-indexed 
                answer = [low + 1, high + 1]
                break 

            elif cur_sum < target:
                low += 1
            else: 
                high -= 1 
                
        return answer 
        