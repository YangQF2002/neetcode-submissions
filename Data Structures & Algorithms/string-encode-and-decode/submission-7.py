class Solution:
    # Now lets extend it to work with all characters 
    # Each string -> length + delimiter + string
    DELIMITER = "$"

    def encode(self, strs: List[str]) -> str:
        result = []

        for string in strs: 
            str_len = len(string)
            encoded_str = f"{str_len}{Solution.DELIMITER}{string}" 
            result.append(encoded_str)
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        # Edge case, for input []
        if not s: 
            return []

        result = []

        # List join is faster than string concat
        # As every concat need to copy prev string 
        str_len = []
        is_on_str = False 
        cur_str = []

        i = 0
        while i < len(s): 
            cur_char = s[i]

            # Collect str_len
            if cur_char != Solution.DELIMITER and not is_on_str: 
                str_len.append(cur_char)
                i += 1 

            # Encounter delimiter 
            elif cur_char == Solution.DELIMITER and not is_on_str: 
                # Edge case 
                # For len = 0, the last one is not captured
                numerical_len = int("".join(str_len))
                if numerical_len == 0: 
                    result.append("")
                    i += 1
                    continue 
                
                is_on_str = True
                i += 1 
            
            # On actual string 
            else: 
                numerical_len = int("".join(str_len))
                count = 0 
                while count < numerical_len: 
                    cur_str.append(s[i]) 
                    count += 1 
                    i += 1 

                # Track and reset 
                result.append("".join(cur_str))  
                is_on_str = False 
                cur_str.clear()
                str_len.clear()
        
        return result
            