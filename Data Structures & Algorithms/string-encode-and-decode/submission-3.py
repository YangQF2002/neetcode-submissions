class Solution:
    # Character space is 256 valid ASCII
    # Lets choose 🔥 as separator? 

    def encode(self, strs: List[str]) -> str:
        # Edge case if absolutely nothing
        if len(strs) == 0: 
            return "🍎"

        return "🔥".join(strs)    
    
    def decode(self, s: str) -> List[str]: 
        if s == "🍎": 
            return []
        
        return s.split("🔥")
