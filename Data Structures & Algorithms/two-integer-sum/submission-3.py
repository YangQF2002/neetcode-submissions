class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Complement number -> index mapping 
        complements = {}
        answer = []

        # Enumerate so can expose current index 
        for index, num in enumerate(nums): 
            complement = target - num

            # Found 
            if complement in complements: 
                lower_index = complements[complement]
                higher_index = index 
                answer = [lower_index, higher_index]
                break

            # Track history 
            # Suppose multiple valid answers exist (eg: [5, 5, 7], target = 12)
            # Then need a if num in complements check, so that we only take smallest index answer
            complements[num] = index

        return answer