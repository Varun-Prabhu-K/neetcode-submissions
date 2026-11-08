class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        b = [[] for _ in range(len(nums) + 1)]
        for j, v in d.items():
            b[v].append(j)
        r = []
        for i in range(len(b) - 1, 0, -1):
            for n in b[i]:
                r.append(n)
                if len(r) == k:
                    return r