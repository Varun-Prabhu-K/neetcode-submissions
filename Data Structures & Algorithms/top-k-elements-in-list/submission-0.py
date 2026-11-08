class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        list1 = list(sorted(d.items(), key = lambda item: item[1], reverse=True))
        list2 = [item[0] for item in list1[:k]]
        return list2