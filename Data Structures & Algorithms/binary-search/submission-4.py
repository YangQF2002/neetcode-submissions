class Solution:
    # -1 0 2 4 6 8
    # 

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0 
        high = n - 1 

        while low <= high: 
            mid = (low + high) // 2
            mid_val = nums[mid] 

            if mid_val == target: 
                return mid 
            elif mid_val > target: 
                high = mid - 1 
            else: 
                low = mid + 1 
        
        return -1
