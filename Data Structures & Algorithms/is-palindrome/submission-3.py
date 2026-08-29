class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0 
        high = len(s) - 1
        while low <= high: 
            # Keep pushing the low pointer up 
            while low <= high and not s[low].isalnum():
                low += 1
            
            # Keep pushing the high pointer down 
            while low <= high and not s[high].isalnum():
                high -= 1
                
            if low <= high:
                # Compare the two alnums
                if s[low].lower() == s[high].lower(): 
                    low += 1
                    high -= 1
                    continue 
                else: 
                    return False 
            else: 
                break
        
        return True 
            
