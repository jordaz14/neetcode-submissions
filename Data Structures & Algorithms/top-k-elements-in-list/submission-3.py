import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        h = []
        for key, val in freqMap.items():
            heapq.heappush(h, (val, key))

            if len(h) > k:
                heapq.heappop(h)

        ans = []
        for item in h:
            ans.append(item[1])
        
        return ans