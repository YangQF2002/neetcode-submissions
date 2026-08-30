# output[i] = all nums except nums[i], no division 
# prefix_sum[i] = up to and excluding i 
# suffix_sum[i] = after i 

# [1, 2, 4, 6]
# prefix: [1, 1, 2, 8]
# suffix: [48, 24, 6, 1]
# multiply both: [48, 24, 12, 8]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        output = [1 for _ in range(n)]
        prefix = [1 for _ in range(n)] 
        suffix = [1 for _ in range(n)] 

        # Build prefix
        for i in range(1, n): 
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # Build suffix
        for i in range(n - 2, -1, -1): 
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Build output 
        for i in range(n): 
            output[i] = prefix[i] * suffix[i]

        return output


        