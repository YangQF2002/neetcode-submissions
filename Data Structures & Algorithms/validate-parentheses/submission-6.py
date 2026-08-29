# Pretty standard, O(n)
  
class Solution: 
    def isValid(self, s: str) -> bool:
        # Tracks opening braces 
        stack = []

        opening_braces = ["(", "{", "["]
        closing_braces = [")", "}", "]"]
        brace_mapping = {
            ")": "(", 
            "}": "{", 
            "]": "["
        }

        for brace in s: 
            if brace in opening_braces: 
                stack.append(brace)
            else: 
                # Closing brace
                # Must match most recent opening brace 
                if not stack or brace_mapping[brace] != stack[-1]: 
                    return False
                
                stack.pop()

        # At the end, should be empty     
        return not stack 

    