# Simple, but O(nlogn) where n is number of num
from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = defaultdict(int)

        for num in nums: 
            freq_count[num] += 1
        
        items = list(freq_count.items()) 
        items.sort(key=lambda x: x[1], reverse=True)

        result = []
        count = 0
        for item in items: 
            if count == k: 
                break 

            result.append(item[0])
            count += 1

        return result
            
    