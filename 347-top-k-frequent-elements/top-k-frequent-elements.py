class Solution:
    def topKFrequent(self, nums, k):

        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # Count occurrences
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Place numbers in buckets by frequency
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Gather top k frequent
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
