import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        max_heap = [(-val, idx) for idx, val in enumerate(nums[:k])]
        heapq.heapify(max_heap)
        res.append(-max_heap[0][0])
        for i, num in enumerate(nums):
            if i < k:
                continue
            heapq.heappush(max_heap, (-num, i))
            while max_heap[0][1] < i - k + 1:
                heapq.heappop(max_heap)
            res.append(-max_heap[0][0])

        return res