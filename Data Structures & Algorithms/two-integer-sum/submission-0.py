class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = None; 
        for index, number in enumerate(nums):
            complement = target - number 
            if seen.get(complement) is not None:
                result = [seen.get(complement), index]
                break 
            
            seen.update({number : index}) 
        
        return result 


            

        