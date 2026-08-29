class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the nums in ascending order first
        # Sorting is OK, since they want elements and not indexes
        nums.sort(); 
        results = []

        length = len(nums)
        for index, num in enumerate(nums):
            twoSumTarget = 0 - num 

            low = index + 1
            high = length - 1
            while low < high: 
                currSum = nums[low] + nums[high]
                if currSum == twoSumTarget:
                    triplet = [num, nums[low], nums[high]]
                    if triplet not in results: 
                        results.append(triplet)

                    low += 1
                    high -= 1 

                elif currSum > twoSumTarget:
                    high -= 1
                
                else: 
                    low += 1
            
        return results

