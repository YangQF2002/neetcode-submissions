class Solution:
    # Version 1 
    def isAnagram(self, s: str, t: str) -> bool:
        # Char to freq mapping 
        freq_count = {}

        # Build 
        for char in s: 
            if char not in freq_count: 
                freq_count[char] = 1 
            else: 
                freq_count[char] += 1
        
        # Check 
        for char in t: 
            if char not in freq_count: 
                return False 
            else: 
                freq_count[char] -= 1 
        
        for value in freq_count.values(): 
            if value != 0: 
                return False 
        
        return True 


            



        