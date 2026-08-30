# Naively we can sort -> O(nlogn)
# Better is two pointer scan, up till low > high 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Process the string 
        # Only keep alnum + case-insensitive 
        new_s = []
        for char in s: 
            if char.isalnum(): 
                new_s.append(char.lower()) 
        
        low = 0 
        high = len(new_s) - 1

        while low <= high: 
            low_char = new_s[low]
            high_char = new_s[high]

            if low_char != high_char: 
                return False 
            
            low += 1
            high -= 1

        return True 
            
