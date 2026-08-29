class Solution:
    # # Version 1 
    # def isAnagram(self, s: str, t: str) -> bool:
    #     # Char to freq mapping 
    #     freq_count = {}

    #     # Build 
    #     for char in s: 
    #         if char not in freq_count: 
    #             freq_count[char] = 1 
    #         else: 
    #             freq_count[char] += 1
        
    #     # Subtract
    #     for char in t: 
    #         if char not in freq_count: 
    #             return False 
    #         else: 
    #             freq_count[char] -= 1 

    #     # Check 
    #     # Can't just do sum == 0, as -1, 1 may give false positive 
    #     for value in freq_count.values(): 
    #         if value != 0: 
    #             return False 
        
    #     return True 

    # Version 2 (fancier, slightly less space, given only lowercase letters)
    def isAnagram(self, s: str, t: str) -> bool: 
        freq_count = 26 * [0]

        # Build 
        for char in s: 
            index = ord(char) - ord('a')
            freq_count[index] += 1
        
        # Check 
        for char in t: 
            index = ord(char) - ord('a')
            freq_count[index] -= 1

        for value in freq_count: 
            if value != 0: 
                return False 

        return True 



            



        