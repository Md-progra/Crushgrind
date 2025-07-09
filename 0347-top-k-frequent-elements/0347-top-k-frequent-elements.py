from collections import Counter
from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Count the frequency of each element using a hash map.
Iterate over the frequency map, adding each element along with its frequency as a tuple to a min-heap.
If the heap exceeds size k, we remove the smallest item, which is automatically done because of the heap's properties. This ensures we only keep the k most frequent elements in the heap.
After processing all elements, we're left with a heap containing k elements with the highest frequency.
We convert this heap into a list containing just the elements (not the frequencies) to return as our final answer.
        """
        frequency_map = Counter(nums)
        min_heap = []
        for num,freq in frequency_map.items():
            heappush(min_heap,(freq,num))
            if len(min_heap) > k:
                heappop(min_heap)

        k_frequents = [in_tuple[1] for in_tuple in min_heap]
        return k_frequents

        