class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0 
        high = len(s) - 1
        while low <= high: 
            while not s[low].isalnum():
                if low == len(s) - 1: 
                    break

                low += 1
                
                    
            while not s[high].isalnum():
                if high == 0:
                    break

                high -= 1
                
            if low <= high:
                if s[low].lower() == s[high].lower(): 
                    low += 1
                    high -= 1
                    continue 
                else: 
                    return False 
            else: 
                break
        
        return True 
            