# Best - O(m * n)
# Signature of a word as an array of freq counts 
from collections import defaultdict 

class Solution:
    def getWordSignature(self, word: str) -> Tuple[int]: 
        freq_count = [0] * 26
        for char in word: 
            index = ord(char) - ord("a")
            freq_count[index] += 1 

        # Dict keys must be immutable 
        return tuple(freq_count)
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        anagrams = defaultdict(list)

        for word in strs: 
            word_sig = self.getWordSignature(word)
            anagrams[word_sig].append(word)

        return list(anagrams.values())
            
    
