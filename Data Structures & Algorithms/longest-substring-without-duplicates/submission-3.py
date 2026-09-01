# Two pointers 
# Start, End -> same side (sliding window)
# Keep shifting end until duplicate, then shift start until no duplicate?

# Duplicate check -> seen set() for fast O(1) queries 
# Add and remove from the set 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen_chars = set()
        length = 0 
        max_length = 0

        start = end = 0 
        while start < n and end < n:
            # Just need one of them to add the char 
            end_char = s[end]
    
            if end_char in seen_chars: 
                max_length = max(length, max_length)

                # Shrink the window 
                while start < end and end_char in seen_chars: 
                    start_char = s[start]
                    seen_chars.remove(start_char)
                    start += 1
                    length -= 1

            # Business as usual! 
            seen_chars.add(end_char)
            end += 1

            length += 1 
            max_length = max(length, max_length)
              
        return max_length   

