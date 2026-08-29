class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for number in nums: 
            if seen.get(number) is None: 
                seen.update({number: 1})
            else: 
                return True 
        return False 
        
