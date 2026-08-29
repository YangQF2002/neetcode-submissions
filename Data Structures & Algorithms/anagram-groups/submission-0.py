class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroup = {}
        for string in strs: 
            charCollection = self.createCharCollection(string)
            if anagramGroup.get(charCollection) is None:
                anagramGroup.update({charCollection : [string]})
            else: 
                anagramGroup[charCollection].append(string)
        
        return anagramGroup.values(); 

    # Helper method 
    def createCharCollection(self, target: str) -> tuple[int]: 
        # Creating a "fixed" size array of length 26
        charCollection = [0] * 26 
        for char in target:
            index = ord(char) - 97 
            charCollection[index] += 1; 

        return tuple(charCollection)  

        
# Keys is limited to just lowercase english letters 
# Just used a fix size array (26); index is the key 
        