class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberFreq = {}
        for number in nums: 
            if numberFreq.get(number) is None: 
                numberFreq.update({number: 1})
            else: 
                numberFreq[number] += 1
        
        freqArray = [[] for _ in range(len(nums))]
        for item in numberFreq.items(): 
            index = item[1] - 1
            freqArray[index].append(item[0]) 


        result = []
        count = 0 
        for i in range(len(freqArray) - 1, -1, -1): 
            current = freqArray[i]
            result.extend(current) 
            count += len(current)
            if count == k: 
                break
        
        return result  


        