class Solution:
    def isValid(self, s: str) -> bool:
        # We are always dependent on the latest open bracket 
        # In other words, we must ensure it is LIFO (matched by correct closing bracket)
        # Hence, we can use a stack here!
        stack = []
        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
            else: 
                # Encounter an extra closing bracket 
                if len(stack) == 0: 
                    return False 

                top = stack[-1]
                if (top == '(' and char == ')') or (top == '{' and char == '}') or (top == '[' and char == ']'):
                    stack.pop()
                else: 
                    return False
            
        # At the end, every open bracket must be closed
        if len(stack) != 0:
            return False 
        else: 
            return True
        
