class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Consider starting numbers 
        # Number - 1 must not exist, use set for O(1) checks 
        numsSet = set(nums)
        maxLength = 0 

        for num in numsSet: 
            oneBelow = num - 1

            # If its a starting number
            # Try to build a sequence from it 
            if oneBelow not in numsSet: 
                length = 1
                next = num + 1
                while next in numsSet: 
                    length += 1
                    next += 1

                # Update the result
                maxLength = max(maxLength, length) 
                
        return maxLength 

                