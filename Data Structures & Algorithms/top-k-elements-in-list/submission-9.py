from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = defaultdict(int)
        for num in nums:
            freq_count[num] += 1

        # Bucket sort; n buckets for frequencies from 1 .. n
        # Each bucket can be an array of numbers (no need sort)
        n = len(nums)
        buckets = [[] for _ in range(n)] 

        for (num, freq) in freq_count.items(): 
            index = freq - 1
            buckets[index].append(num)

        # Get top K 
        result = []
        count = 0 
        for i in range(n - 1, -1, -1):
            if count == k: 
                break 

            current_bucket = buckets[i]

            # Empty 
            if not current_bucket: 
                continue 

            result.extend(buckets[i])
            count += len(current_bucket)

        return result