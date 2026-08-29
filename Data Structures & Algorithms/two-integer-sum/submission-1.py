class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Complement number -> index mapping 
        complements = {}
        answer = []

        # Enumerate so can expose current index 
        for index, num in enumerate(nums): 
            complement = target - num

            if complement in complements: 
                lower_index = complements[complement]
                higher_index = index 
                answer = [lower_index, higher_index]
                break

            if num not in complements: 
                complements[num] = index

        return answer