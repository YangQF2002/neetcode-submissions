# Order does not matter, just look at triplet groups 

# First, sort ASC 
# Then, fix one index, scan the remaining list for the next two indices

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        
        answer = []

        prev_start = None 
        for i in range(n):
            # Don't reuse the same starting point 
            if prev_start is not None and prev_start == nums[i]: 
                continue 

            low = i + 1 
            high = n - 1 
            target_sum = 0 - nums[i]

            # Note we exclude low == high
            # As we want distinct indices!! 
            while low < high: 
                cur_sum = nums[low] + nums[high] 
                if cur_sum == target_sum: 
                    answer.append([nums[i], nums[low], nums[high]])

                    # Move low and high until we see a different number 
                    prev = nums[low]
                    while nums[low] == prev and low < high:
                        low += 1

                    prev = nums[high]
                    while nums[high] == prev and low < high: 
                        high -= 1

                elif cur_sum < target_sum: 
                    low += 1
                else: 
                    high -= 1 
            
            prev_start = nums[i]
        
        return answer
                    