class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLength = 0 

        for num in numsSet: 
            oneBelow = num - 1
        
            if oneBelow not in numsSet: 
                length = 1
                next = num + 1
                while next in numsSet: 
                    length += 1
                    next += 1

                maxLength = max(maxLength, length) 
                
        return maxLength 

                