# Start, end pointers 
# Grow the window, until most freq char (dynamic anchor) is not able to anchor 
# Meaning that window_length - count of most freq > k 
# Then, shrink the window until <= k 
from collections import defaultdict 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        longest = 0

        start = end = 0  
        char_freq = defaultdict(int)

        # Main scan 
        while start < n and end < n: 
            # Put it in first 
            end_char = s[end]
            char_freq[end_char] += 1 
             
            # Then check 
            window_length = end - start + 1 
            highest_freq = max(char_freq.values())

            # Shrink if applicable 
            while window_length - highest_freq > k and window_length > 0: 
                window_length -= 1 
                start_char = s[start]
                char_freq[start_char] -= 1 
                start += 1 

                highest_freq = max(char_freq.values())

            # Always update after 
            end += 1
            longest = max(longest, window_length)

        return longest 
                