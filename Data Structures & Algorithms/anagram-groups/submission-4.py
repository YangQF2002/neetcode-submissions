# Best - O(m * n)
# Signature of a word as an array of freq counts 

class Solution:
    def getWordSignature(self, word: str) -> Tuple[int]: 
        freq_count = [0] * 26
        for char in word: 
            index = ord(char) - ord("a")
            freq_count[index] += 1 

        return tuple(freq_count)
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        anagrams = {}

        for word in strs: 
            word_sig = self.getWordSignature(word)
            if word_sig not in anagrams: 
                anagrams[word_sig] = [word]
            else: 
                anagrams[word_sig].append(word)

        return list(anagrams.values())
            
    
