import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        h = []
        for key, val in freq.items():
            heapq.heappush(h, (val, key))

            if len(h) > k:
                heapq.heappop(h)

        return [num for _, num in h]