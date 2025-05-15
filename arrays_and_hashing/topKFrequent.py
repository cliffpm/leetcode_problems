class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        res = [[]for i in range(len(nums)+1)] # N+1 buckets for bucket sort
        freq = Counter(nums)
        

        for num in freq:
            frequency = freq.get(num)
            res[frequency].append(num)


       # print (res)
        actual_res = []

        for i in range(len(res)-1, -1, -1):
            for num in res[i]:
                print(num)
                actual_res.append(num)
            if len(actual_res) == k:
                return actual_res

        return actual_res
        #Max Heap + Hashmap Solution: O(N + kLog(N))
        # res = []
        # min_heap = []
        # #heapq supports min heap, so to make max heap, reverse sign of priority
        # #faster to create array first, then heapify via floyds algorithm
        # for num in freq:
        #     min_heap.append((-freq.get(num), num))
        # heapq.heapify(min_heap)
        # i =0
        # while (i < k):
        #     res.append(heapq.heappop(min_heap)[1])
        #     i+=1
       # return res
