class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        start = 0  
        char_freq = defaultdict(int)
        max_freq = 0  # Tracks the historical peak frequency
        longest = 0

        for end in range(n): 
            # 1. Expand the window
            end_char = s[end]
            char_freq[end_char] += 1 
            
            # 2. Update the peak frequency dynamically (O(1))
            max_freq = max(max_freq, char_freq[end_char])

            # 3. Shrink by at most 1 step if the window becomes invalid
            # (window_length = end - start + 1)
            if (end - start + 1) - max_freq > k: 
                start_char = s[start]
                char_freq[start_char] -= 1 
                start += 1 
                # Note: max_freq is intentionally left unchanged here!

            # 4. Track the maximum valid window size seen so far
            longest = max(longest, end - start + 1)

        return longest