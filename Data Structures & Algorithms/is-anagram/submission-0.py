class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCollection = {}
        for char in s: 
            if charCollection.get(char) is None: 
                charCollection.update({char : 1})
            else: 
                charCollection[char] += 1
        
        for char in t: 
            if charCollection.get(char) is None or charCollection.get(char) == 0: 
                return False 
            else:
                charCollection[char] -= 1 
        
        if max(charCollection.values()) > 0:
            return False 
        
        return True 